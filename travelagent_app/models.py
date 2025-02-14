from django.db import models
from user_app.models import *
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class travelagent_model(models.Model):
    phone_number=models.IntegerField(null=True,blank=True)
    bussiness_name=models.CharField(max_length=20,null=True,blank=True)
    image = models.ImageField(upload_to='upload images/')
    travelagent = models.OneToOneField(User_profile, on_delete=models.CASCADE, blank=True, null=True)
    tax_identification_number=models.IntegerField(null=True,blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

class travel_package(models.Model):
    PACKAGE_TYPES = [
        ('family', 'Family'),
        ('luxury', 'Luxury'),
        ('honeymoon', 'Honeymoon'),
        ('adventure', 'Adventure'),
    ]

    name=models.CharField(max_length=20,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_days = models.IntegerField(null=True,blank=True)
    available_from = models.DateField()
    available_to = models.DateField()
    package_type = models.CharField(max_length=50, choices=PACKAGE_TYPES)
    destinations = models.CharField(max_length=20,null=True,blank=True)
    image = models.ImageField(upload_to='upload images/')
    connect=models.ForeignKey(User_profile,on_delete=models.CASCADE,blank=True,null=True)
    lock=models.ForeignKey(travelagent_model,on_delete=models.CASCADE,null=True,blank=True)
    status = models.CharField(default="Active", max_length=20, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

class Booking_package(models.Model):
    package = models.ForeignKey(travel_package, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User_profile, on_delete=models.CASCADE, blank=True, null=True)
    booking_date = models.DateField(blank=True, null=True)
    number_of_people = models.IntegerField(blank=True, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    travel_dates = models.DateField(null=True, blank=True)  # Add this if not already in the model and is required

    def save(self, *args, **kwargs):
        # Calculate the total amount based on the number of people and the package price
        if self.package and self.number_of_people:
            self.total_amount = self.package.price * self.number_of_people
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Booking for {self.user.username} - {self.package.name}"
class Payment(models.Model):
    PAYMENT_METHODS = [
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
        ('paypal', 'PayPal'),
        ('bank_transfer', 'Bank Transfer'),
    ]

    user = models.ForeignKey(User_profile, on_delete=models.CASCADE,null=True,blank=True)
    booking = models.ForeignKey(Booking_package, on_delete=models.CASCADE,null=True,blank=True)  # link payment to a booking
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS,null=True,blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField(null=True,blank=True)
    def __str__(self):
        return f"Payment of {self.amount} for booking {self.booking.id} by {self.user.username}"

class Complaints(models.Model):
    customer = models.ForeignKey(
        User_profile,  # Ensure this is the correct model name
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )  # Link complaint to the customer

    travelagent = models.ForeignKey(
        travelagent_model,  # Ensure this is the correct model name
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )  # Link complaint to the travel agent

    message = models.TextField(null=True, blank=True)

    date = models.DateField(null=True, blank=True)

    reply = models.TextField(null=True, blank=True)

    reply_date = models.DateField(null=True, blank=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # Make sure that 'username' and 'bussiness_name' are actual fields in your models
        return f"Complaint by {self.customer.username if self.customer else 'Unknown Customer'} to {self.travelagent.bussiness_name if self.travelagent else 'Unknown Travel Agent'}"
class Reviews(models.Model):
    user = models.ForeignKey(
        User_profile,
        on_delete=models.CASCADE,
        null=True,  # Optional: Only use if you want reviews without users
        blank=True
    )
    travelagent = models.ForeignKey(
        travelagent_model,  # Replace with the correct travel agent model name
        on_delete=models.CASCADE,
        null=True,  # Optional: Only use if you want reviews without a travel agent
        blank=True
    )
    rating = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(1), MaxValueValidator(5)]  # Ensure ratings are between 1 and 5
    )
    comment = models.TextField(blank=True, null=True)  # Optional comment
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Handle cases where user or travel agent might be null
        user_name = self.user.username if self.user else 'Anonymous User'
        travelagent_name = self.travelagent.bussiness_name if self.travelagent else 'Unnamed Travel Agent'
        return f"Review by {user_name} for {travelagent_name} - Rating: {self.rating}"
