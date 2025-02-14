from django.db import models
from user_app.models import *
from django.core.validators import MinValueValidator,MaxValueValidator
from customer_app.models import *
from django.core.exceptions import ValidationError
from django.db.models import Q


# Create your models here.
class restaurant_model(models.Model):
    bussiness_name = models.CharField(max_length=20, null=True, blank=True)
    resturent = models.OneToOneField(User_profile, on_delete=models.CASCADE, blank=True, null=True)
    phone_number=models.IntegerField(null=True,blank=True)
    image = models.ImageField(upload_to='upload images/')
    status = models.CharField(default="Active", max_length=20, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)


class Room(models.Model):
    ROOMSTYPE_CHOICES = [
        ('Single', 'single'),
        ('Double', 'double'),
        ('Suite', 'suite'),  # Corrected the spelling of "Suite"
    ]

    image = models.ImageField(upload_to='upload_images/', null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)  # Adding a 'name' field to uniquely identify the room
    category = models.CharField(max_length=20, choices=ROOMSTYPE_CHOICES)
    description = models.TextField()
    capacity = models.IntegerField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    lock = models.ForeignKey(restaurant_model, on_delete=models.CASCADE, null=True, blank=True)
    facilities=models.CharField(max_length=100,null=True,blank=True)

    connect=models.ForeignKey(User_profile,on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return f"{self.number} - {self.category}"  # Updated __str__ method


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)
    guest_name = models.CharField(max_length=100, null=True, blank=True)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    number_of_guests = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    user = models.ForeignKey(User_profile, on_delete=models.CASCADE, null=True, blank=True)

    def get_available_rooms(check_in_date, check_out_date):
        """
        This function retrieves all rooms that are not booked during the provided check-in and check-out dates.
        """
        # Get all rooms that do not have any overlapping bookings during the given date range
        available_rooms = Room.objects.exclude(
            booking__check_in_date__lt=check_out_date,
            booking__check_out_date__gt=check_in_date
        )

        return available_rooms

    # Updated to use User model

    def __str__(self):
        return f"Booking by {self.guest_name} for {self.user.username}"

    def calculate_total_price(self):
        """
        Calculate the total price of the booking based on the number of nights and price per night.
        """
        days = (self.check_out_date - self.check_in_date).days
        if days < 1:
            raise ValueError("Check-out date must be after the check-in date.")
        return self.room.price_per_night * days


class Dish(models.Model):
    CATEGORY_CHOICES = [
        ('appetizer', 'Appetizer'),
        ('main_course', 'Main Course'),
        ('dessert', 'Dessert'),
        ('beverage', 'Beverage'),
    ]

    AVAILABILITY_CHOICES = [
        ('available', 'Available'),
        ('not_available', 'Not Available'),
    ]

    name = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    availability = models.CharField(max_length=15, choices=AVAILABILITY_CHOICES, default='available')
    image = models.ImageField(upload_to='upload images/')
    connect = models.ForeignKey(User_profile, on_delete=models.CASCADE, blank=True, null=True)
    lock = models.ForeignKey(restaurant_model, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(default="Active", max_length=20, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name


class BookDish(models.Model):
    # Assuming a User is booking the dish
    user = models.ForeignKey(User_profile, on_delete=models.CASCADE, blank=True, null=True)

    # The dish being booked
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, blank=True, null=True)

    # Number of dishes booked
    quantity = models.PositiveIntegerField(default=1)

    # Date and time when the booking is made
    booking_date = models.DateTimeField()

    # Any special requests for the dish
    special_requests = models.TextField(blank=True, null=True)

    # Status of the booking (using choices for better control)

    # Total price will be calculated based on dish price and quantity
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # Time when the booking was created
    created_at = models.DateTimeField(auto_now_add=True)

    # Time when the booking was last updated
    updated_at = models.DateTimeField(auto_now=True)

    # Automatically calculate total price based on quantity and dish price
    def save(self, *args, **kwargs):
        if self.dish:
            self.total_price = self.dish.price * self.quantity
        super(BookDish, self).save(*args, **kwargs)

    def __str__(self):
        return f"Booking for {self.dish.name} by {self.user.username if self.user else 'Guest'}"


class mycomplaints(models.Model):
    customer = models.ForeignKey(
        User_profile,  # Replace with the actual model name if it's different
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )  # Link complaint to the customer

    restaurant = models.ForeignKey(
        restaurant_model,  # Replace with actual model name if different
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )  # Link complaint to the restaurant

    message = models.TextField(null=True, blank=True)  # Customer complaint message

    date = models.DateField(null=True, blank=True)  # Date when complaint was sent

    reply = models.TextField(null=True, blank=True)  # Restaurant's reply to the complaint

    reply_date = models.DateField(null=True, blank=True)  # Date when the reply was sent

    is_active = models.BooleanField(default=True)  # Whether the complaint is still active (open)

    created_at = models.DateTimeField(auto_now_add=True)  # When the complaint was created

    updated_at = models.DateTimeField(auto_now=True)  # Last time the complaint was updated

    def __str__(self):
        # Ensure 'username' and 'name' fields exist in 'User_profile' and 'restaurant_model' respectively
        # If those fields do not exist, you should adjust the fields in the `__str__()` method.
        return f"Complaint by {self.customer.username if self.customer else 'Unknown Customer'} to {self.restaurant.bussiness_name if self.restaurant else 'Unknown Restaurant'}"


class Review(models.Model):
    user = models.ForeignKey(
        User_profile,
        on_delete=models.CASCADE,
        null=True,  # Optional: Only use if you want reviews without users
        blank=True
    )
    restaurant = models.ForeignKey(
        restaurant_model,  # Replace with the correct restaurant model name
        on_delete=models.CASCADE,
        null=True,  # Optional: Only use if you want reviews without restaurants
        blank=True
    )
    rating = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(1), MaxValueValidator(5)]  # Ensure ratings are between 1 and 5
    )
    comment = models.TextField(blank=True, null=True)  # Optional comment
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Handle cases where user or restaurant might be null
        user_name = self.user.username if self.user else 'Anonymous User'
        restaurant_name = self.restaurant.bussiness_name if self.restaurant else 'Unnamed Restaurant'
        return f"Review by {user_name} for {restaurant_name} - Rating: {self.rating}"