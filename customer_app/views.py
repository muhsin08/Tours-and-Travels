from gc import get_objects
from time import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from manager_app.serializers import VRVideosSerializer
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.decorators import login_required



from travelagent_app.forms import *
from user_app .models import *
from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from customer_app.models import *
from customer_app.forms import *
from manager_app .models import *
from manager_app .forms import *
from travelagent_app .forms import *
from restaurant_app .models import *
from restaurant_app .forms import *
from django.contrib import messages
from django.shortcuts import get_object_or_404


# from manager_app.models import feedback
from travelagent_app .models import *

# Create your views here.

class customer_book(View):
    def get(self, request):
        my_customer = customer_model.objects.filter(is_active=True)
        return render(request, 'customer_template/register_cust.html',{'form':my_customer})

    def post(self, request):
        slot = customer_form(request.POST)
        if slot.is_valid():
            new = slot.save(commit=False)
            life = User_profile.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password'],
                email=request.POST['email'],
                user_type='CUSTOMER'
            )
            new.customer = life
            new.save()

            redirect_url = reverse('user_app:userlogin')  # Make sure 'MainPageView' is the correct URL name

            # Return the script with the redirection
            return HttpResponse(f'''
                           <script>alert("Registration successful.");
                           window.location="{redirect_url}";
                           </script>
                       ''')

        return render(request,'customer_app/register_cust.html', {'fry':slot})

class homepage(View):
    def get(self, request):
        return render(request, 'customer_template/homepage.html')
class view_packages(View):
    def get(self,request):
        package_tour=travel_package.objects.all()
        return render(request,'customer_template/view_packages.html',{'pack':package_tour})
class ViewPackagesAPIView(APIView):
    def get(self, request):
        package_tour = travel_package.objects.all()
        return Response({'packages': package_tour.values()})

class BookNowAPIView(APIView):
    def get(self, request, id):
        # Get the travel package object by ID
        package = get_object_or_404(travel_package, pk=id)

        # Return the package details as a JSON response
        package_data = {
            "id": package.id,
            "name": package.name,
            "description": package.description,
            "price": package.price,
            "category": package.category,
            "image_url": package.image.url if package.image else None,
            "available_slots": package.available_slots,
        }

        return Response(package_data, status=status.HTTP_200_OK)
class view_videos(View):
    def get(self,request):
        my_videos=VR_vedios.objects.all()
        return render(request,'customer_template/view_VR_videos.html',{'my_videos':my_videos})
class VRVideosAPIView(APIView):
    def get(self, request):
        my_videos = VR_vedios.objects.all()
        serializer = VRVideosSerializer(my_videos, many=True)
        return Response(serializer.data)
class upcom_fest_view(View):
    def get(self,request):
        festivals = Festival.objects.all()
        return render(request, 'customer_template/view_festivals.html', {'festivals': festivals})
class trending_place_view(View):
    def get(self,request):
        trend_place = AddTouristPlace.objects.all()
        return render(request, 'customer_template/view_trendingplace.html', {'trend_place': trend_place})


class add_feedback(View):
    def get(self, request):
        # Render the feedback form on GET request
        return render(request, 'customer_template/send_feedback.html')

    def post(self, request):
        # Check if user is logged in
        if 'login_id' not in request.session:
            messages.error(request, 'Session expired. Please log in again.')
            return redirect('user_app:userlogin')

        try:
            # Fetch user profile and associated customer data
            login = User_profile.objects.get(id=request.session['login_id'])
            customer = customer_model.objects.filter(customer=login).first()

            # If no associated customer, show error message
            if not customer:
                messages.error(request, 'You are not authorized to upload a package.')
                return redirect('user_app:userlogin')
        except User_profile.DoesNotExist:
            messages.error(request, 'Invalid session. Please log in again.')
            return redirect('user_app:userlogin')

        # Process the feedback form submission
        agent = feedbackform(request.POST, request.FILES)
        if agent.is_valid():
            c = agent.save(commit=False)
            c.lock = customer
            c.connect = login
            c.save()
            messages.success(request, 'Feedback added successfully.')
            return redirect('view_reply')  # Redirect after successful feedback submission
        else:
            # Return the form with errors if the submission is invalid
            messages.error(request, 'There was an error with your submission. Please check the form and try again.')
            return render(request, 'customer_template/send_feedback.html', {'tour_feedback': agent})

class view_reply(View):
    def get(self, request):
        try:
            content = request.session.get('login_id')
            content_media = send_feedback.objects.filter(connect=content)
        except User_profile.DoesNotExist:
            return HttpResponse("User profile not found for the current user", status=404)
        return render(request, 'customer_template/view_replies.html', {'replies': content_media})



#booking




  # Assuming your form is imported correctly


class AddComplaints(View):
    def get(self, request, id):
        restaurant = get_object_or_404(restaurant_model, pk=id)
        return render(request, "customer_template/complaints_rest.html", {"restaurant": restaurant})

    def post(self, request, id):
        # Check if the user is logged in
        if 'login_id' not in request.session:
            messages.error(request, 'You must be logged in to submit a complaint.')
            return redirect("user_app:userlogin")

        user_id = request.session.get('login_id')
        customer = get_object_or_404(User_profile, pk=user_id)
        restaurant = get_object_or_404(restaurant_model, pk=id)

        # Handle the complaint form
        data = rest_complaintform(request.POST)
        if data.is_valid():
            complaint = data.save(commit=False)
            complaint.customer = customer
            complaint.restaurant = restaurant
            complaint.save()  # Save the complaint with related customer and restaurant

            redirect_url = reverse('view_restreply')  # Make sure 'MainPageView' is the correct URL name

            # Return the script with the redirection
            return HttpResponse(f'''
                                      <script>alert("Registration successful.");
                                      window.location="{redirect_url}";
                                      </script>
                                  ''')
        return render(request, "customer_template/complaints_rest.html", {"restaurant": restaurant, "form": data})


class restaurant_view(View):
    def get(self,request):
        my_rest = restaurant_model.objects.all()
        return render(request, 'customer_template/homepage.html', {'my_rest': my_rest})
class explore_rest(View):
    def get(self, request, id):
        card_rest = restaurant_model.objects.get(pk=id)
        return render(request, 'customer_template/explore_rest.html', {
            'det': card_rest,


        })
class dishes_view(View):
    def get(self,request,id):
        dish_item=get_object_or_404(restaurant_model,pk=id)
        food=Dish.objects.filter(lock=dish_item,availability="available")
        return render(request,'customer_template/dish_view.html',{"dish_item":dish_item,"food":food})
class rooms_view(View):
    def get(self,request,id):
        rooms = get_object_or_404(restaurant_model, pk=id)
        available=Room.objects.filter(lock=rooms)
        return render(request,'customer_template/rooms_view.html',{"rooms":rooms,"available":available})
class submit_review(View):
    def get(self, request):
        return render(request, 'customer_template/submit_review.html')

    def post(self, request):
        user_id = request.session.get('login_id')
        if not user_id:
            return redirect('user_app:userlogin')

        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        if rating:
            review.objects.create(
                user_id=user_id,rating=int(rating),comment=comment
            )
            redirect_url = reverse('')  # Make sure 'MainPageView' is the correct URL name

            # Return the script with the redirection
            return HttpResponse(f'''
                                                 <script>alert("Registration successful.");
                                                 window.location="{redirect_url}";
                                                 </script>
                                             ''')
        return render(request, 'customer_template/submit_review.html', {'error': 'Please select a rating.'})


# views.py
class SearchSpot(View):
    def get(self, request):
        spot = request.GET.get('spot')  # This should match the input name in the HTML form
        context = {}

        if spot:
            # You can filter by the name or description of the AddSpot
            spots = AddSpot.objects.filter(name__icontains=spot) | AddSpot.objects.filter(description__icontains=spot)

            # Check if any spots are found
            if spots.exists():
                context['spots'] = spots
                context['spot'] = spot
            else:
                context['error'] = f"No results found for the spot: {spot}"
        else:
            context['error'] = "Please provide a spot to search."

        return render(request, 'customer_template/homepage.html', context)
class explore_spot(View):
    def get(self, request, id):
        card_spot = AddSpot.objects.get(pk=id)
        return render(request, 'customer_template/explore_spot.html', {
            'det': card_spot,


        })
class trvelagent_view(View):
    def get(self,request):
        my_travel = travelagent_model.objects.all()
        return render(request, 'customer_template/view_travelagent.html', {'my_travel': my_travel})
class explore_travel(View):
    def get(self, request, id):
        card_travel = travelagent_model.objects.get(pk=id)
        return render(request, 'customer_template/explore_agent.html', {
            'det': card_travel,


        })

class Package_view(View):
    def get(self,request,id):
        pack_item=get_object_or_404(travelagent_model,pk=id)
        trip=travel_package.objects.filter(lock=pack_item)
        return render(request,'customer_template/pack.html',{"pack_item":pack_item,"trip":trip})

class travelComplaints(View):
    def get(self, request, id):
        travels = get_object_or_404(travelagent_model, pk=id)
        return render(request, "customer_template/complaints_agent.html", {"travels": travels})

    def post(self, request, id):
        # Check if the user is logged in
        if 'login_id' not in request.session:
            messages.error(request, 'You must be logged in to submit a complaint.')
            return redirect("user_app:userlogin")

        user_id = request.session.get('login_id')
        customer = get_object_or_404(User_profile, pk=user_id)
        travelagent = get_object_or_404(travelagent_model, pk=id)

        # Handle the complaint form
        data = travel_complaintform(request.POST)
        if data.is_valid():
            complaint = data.save(commit=False)
            complaint.customer = customer
            complaint.travelagent = travelagent
            complaint.save()  # Save the complaint with related customer and restaurant

            return HttpResponse("Complaint successfully saved")

        return render(request, "customer_template/complaints_agent.html", {"restaurant": travelagent, "form": data})

class Send_review(View):
    def get(self, request, id):
        reviews = get_object_or_404(restaurant_model, pk=id)
        return render(request, "customer_template/submit_review.html", {"reviews": reviews})

    def post(self, request, id):
        # Check if the user is logged in
        if 'login_id' not in request.session:
            messages.error(request, 'You must be logged in to submit a complaint.')
            return redirect("user_app:userlogin")

        user_id = request.session.get('login_id')
        user = get_object_or_404(User_profile, pk=user_id)
        restaurant = get_object_or_404(restaurant_model, pk=id)

        # Handle the complaint form
        data = review_forms(request.POST)
        if data.is_valid():
            my_review = data.save(commit=False)
            my_review.user = user
            my_review.restaurant = restaurant
            my_review.save()  # Save the complaint with related customer and restaurant

            redirect_url = reverse('Send_review')  # Make sure 'MainPageView' is the correct URL name

            # Return the script with the redirection
            return HttpResponse(f'''
                                                           <script>alert("Registration successful.");
                                                           window.location="{redirect_url}";
                                                           </script>
                                                       ''')
        return render(request, "customer_template/submit_review.html", {"restaurant": restaurant, "form": data})
class Travel_review(View):
    def get(self, request, id):
        review = get_object_or_404(travelagent_model, pk=id)
        return render(request, "customer_template/travelreview.html", {"reviews": review})

    def post(self, request, id):
        # Check if the user is logged in
        if 'login_id' not in request.session:
            messages.error(request, 'You must be logged in to submit a complaint.')
            return redirect("user_app:userlogin")

        user_id = request.session.get('login_id')
        user = get_object_or_404(User_profile, pk=user_id)
        travelagent = get_object_or_404(travelagent_model, pk=id)

        # Handle the complaint form
        data = reviewforms(request.POST)
        if data.is_valid():
            my_review = data.save(commit=False)
            my_review.user = user
            my_review.travelagent = travelagent
            my_review.save()  # Save the complaint with related customer and restaurant

            redirect_url = reverse('Travel_review')  # Make sure 'MainPageView' is the correct URL name

            # Return the script with the redirection
            return HttpResponse(f'''
                                                                      <script>alert("Registration successful.");
                                                                      window.location="{redirect_url}";
                                                                      </script>
                                                                  ''')
        return render(request, "customer_template/travelreview.html", {"travelagent": travelagent, "form": data})
class view_restreply(View):
    def get(self, request):
        try:
            content = request.session.get('login_id')
            content_media = mycomplaints.objects.filter(customer=content)
        except User_profile.DoesNotExist:
            return HttpResponse("User profile not found for the current user", status=404)
        return render(request, 'customer_template/view_restreply.html', {'reply': content_media})
class view_travelreply(View):
    def get(self, request):
        try:
            content = request.session.get('login_id')
            content_media = Complaints.objects.filter(customer=content)
        except User_profile.DoesNotExist:
            return HttpResponse("User profile not found for the current user", status=404)
        return render(request, 'customer_template/view_travelreply.html', {'reply': content_media})
def available_rooms_view(request):
    check_in_date = request.GET.get('check_in_date')
    check_out_date = request.GET.get('check_out_date')

    if check_in_date and check_out_date:
        check_in_date = datetime.strptime(check_in_date, "%Y-%m-%d")
        check_out_date = datetime.strptime(check_out_date, "%Y-%m-%d")

        # Get available rooms that are not already booked in the selected dates
        available_rooms = Room.objects.exclude(
            booking__check_in_date__lt=check_out_date,
            booking__check_out_date__gt=check_in_date
        )
    else:
        available_rooms = Room.objects.all()  # If no dates are provided, show all rooms

    return render(request, 'customer_template/rooms_view.html', {'available_rooms': available_rooms})

class room_booking(View):
    def get(self, request, id):
        rooms = get_object_or_404(Room, pk=id)
        return render(request, "customer_template/book_rooms.html", {"rooms": rooms})

    def post(self, request, id):
        # Check if the user is logged in
        if 'login_id' not in request.session:
            messages.error(request, 'You must be logged in to book a room.')
            return redirect("user_app:userlogin")

        user_id = request.session.get('login_id')
        users = get_object_or_404(User_profile,pk=user_id)
        room = get_object_or_404(Room,pk=id)

        # Handle the room booking form
        form = BookingForm(request.POST)
        if form.is_valid():
            # Get the form data
            check_in_date = form.cleaned_data['check_in_date']
            check_out_date = form.cleaned_data['check_out_date']
            number_of_guests = form.cleaned_data['number_of_guests']

            # Ensure dates are valid
            if check_in_date >= check_out_date:
                messages.error(request, 'Check-out date must be later than check-in date.')
                return render(request, "customer_template/book_rooms.html", {"rooms": room, "form": form})

            # Calculate the total price
            days_stayed = (check_out_date - check_in_date).days
            if days_stayed <= 0:
                messages.error(request, 'Stay duration must be at least one day.')
                return render(request, "customer_template/book_rooms.html", {"rooms": room, "form": form})

            total_price = room.price_per_night * number_of_guests

            # Save the booking
            booking = form.save(commit=False)
            booking.user = users
            booking.room = room
            booking.total_price = total_price  # Save calculated total price
            booking.save()

            redirect_url = reverse('view_roombook')  # Make sure 'MainPageView' is the correct URL name

            # Return the script with the redirection
            return HttpResponse(f'''
                                                               <script>alert("add successful.");
                                                               window.location="{redirect_url}";
                                                               </script>
                                                           ''')

        return render(request, "customer_template/book_rooms.html", {"rooms": room, "form": form})
class view_roombook(View):
    def get(self, request):
        try:
            content = request.session.get('login_id')
            content_media = Booking.objects.filter(user=content)
        except User_profile.DoesNotExist:
            return HttpResponse("User profile not found for the current user", status=404)
        return render(request, 'customer_template/view_roombook.html', {'my': content_media})

# Assuming you have a form to handle the dish booking

class DishBookingView(View):
    def get(self, request, id):
        # Get the dish object based on the provided ID
        dish = get_object_or_404(Dish, pk=id)
        return render(request, "customer_template/book_dish.html", {"dish": dish})

    def post(self, request, id):
        # Check if the user is logged in
        if 'login_id' not in request.session:
            messages.error(request, 'You must be logged in to book a dish.')
            return redirect("user_app:userlogin")

        user_id = request.session.get('login_id')
        user = get_object_or_404(User_profile, pk=user_id)
        dish = get_object_or_404(Dish, pk=id)

        # Handle the dish booking form
        form = Bookdish_Form(request.POST)
        if form.is_valid():
            # Get the form data
            quantity = form.cleaned_data['quantity']
            special_requests = form.cleaned_data['special_requests']

            # Ensure quantity is valid (positive integer)
            if quantity <= 0:
                messages.error(request, 'Quantity must be at least 1.')
                return render(request, "customer_template/book_dish.html", {"dish": dish, "form": form})

            # Calculate the total price based on quantity and dish price
            total_price = dish.price * quantity

            # Create a new booking instance
            booking = form.save(commit=False)
            booking.user = user
            booking.dish = dish
            booking.total_price = total_price  # Save calculated total price
            booking.save()

            redirect_url = reverse('view_dishbooking')  # Ensure this is the correct URL for viewing bookings

            # Return the script with the redirection
            return HttpResponse(f'''
                                                               <script>alert("Booking successful.");
                                                               window.location="{redirect_url}";  // redirect after successful booking
                                                               </script>
                                                           ''')

        return render(request, "customer_template/book_dish.html", {"dish": dish, "form": form})
class view_dishbooking(View):
    def get(self, request):
        try:
            content = request.session.get('login_id')
            content_media = BookDish.objects.filter(user=content)
        except User_profile.DoesNotExist:
            return HttpResponse("User profile not found for the current user", status=404)
        return render(request, 'customer_template/view_dishbook.html', {'book': content_media})


class PackageBooking(View):
    def get(self, request, id):
        # Get the travel package object based on the provided ID
        travel_packages = get_object_or_404(travel_package, pk=id)
        return render(request, "customer_template/add_booking.html", {"travel_package": travel_packages})

    def post(self, request, id):
        # Check if the user is logged in
        if 'login_id' not in request.session:
            messages.error(request, 'You must be logged in to book a package.')
            return redirect("user_app:userlogin")  # Adjust this to your actual login URL

        user_id = request.session.get('login_id')
        users = get_object_or_404(User_profile, pk=user_id)
        travel_packages = get_object_or_404(travel_package, pk=id)

        # Handle the package booking form
        form = packbook_form(request.POST)
        if form.is_valid():
            # Get the form data
            number_of_people = form.cleaned_data['number_of_people']
            booking_date = form.cleaned_data['booking_date']
            travel_dates = form.cleaned_data['travel_dates']  # Ensure travel_dates is included

            # Ensure number_of_people is valid (positive integer)
            if number_of_people <= 0:
                messages.error(request, 'Number of people must be at least 1.')
                return render(request, "customer_template/add_booking.html", {"travel_package": travel_packages, "form": form})

            # Calculate the total price based on the number of people and package price
            total_price = travel_packages.price * number_of_people

            # Create a new booking instance
            booking = form.save(commit=False)
            booking.user = users
            booking.package = travel_packages
            booking.total_amount = total_price  # Save calculated total price
            booking.save()

            redirect_url = reverse('view_bookings')  # Ensure this is the correct URL for viewing bookings

            # Return the script with the redirection
            return HttpResponse(f'''
                                                                         <script>alert("Booking successful.");
                                                                         window.location="{redirect_url}";  // redirect after successful booking
                                                                         </script>
                                                                     ''')

        return render(request, "customer_template/add_booking.html", {"travel_package": travel_packages, "form": form})



class view_bookings(View):
    def get(self, request):
        try:
            content = request.session.get('login_id')
            content_media = Booking_package.objects.filter(user=content)
        except User_profile.DoesNotExist:
            return HttpResponse("User profile not found for the current user", status=404)
        return render(request, 'customer_template/view_prvs_booking.html', {'mybook': content_media})
class PaymentProcess(View):
    def get(self, request,id):
        pyments= get_object_or_404(Booking_package, pk=id)
        return render(request,'customer_template/pyments.html',{'pay':pyments})


