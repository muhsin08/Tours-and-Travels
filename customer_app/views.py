from time import timezone
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

            return HttpResponse('successfully saved')

        return render(request, 'customer_app/register_cust.html', {'fry':slot})

class homepage(View):
    def get(self, request):
        return render(request, 'customer_template/homepage.html')
class view_packages(View):
    def get(self,request):
        package_tour=travel_package.objects.all()
        return render(request,'customer_template/view_packages.html',{'pack':package_tour})
class view_videos(View):
    def get(self,request):
        my_videos=VR_vedios.objects.all()
        return render(request,'customer_template/view_VR_videos.html',{'my_videos':my_videos})
class upcom_fest_view(View):
    def get(self,request):
        festivals = Festival.objects.all()
        return render(request, 'customer_template/view_festivals.html', {'festivals': festivals})
class trending_place_view(View):
    def get(self,request):
        trend_place = add_turistplaces.objects.all()
        return render(request, 'customer_template/view_trendingplace.html', {'trend_place': trend_place})
class add_feedback(View):
    def get(self,request):
        feed=send_feedback.objects.filter(is_active=True)
        return render(request,'customer_template/send_feedback.html',{"feed":feed})
    def post(self, request):
        tour_feedback = feedbackform(request.POST)

        if tour_feedback.is_valid():
            tour_feedback.save()
            return HttpResponse("successfully saved")

        return render(request, 'customer_template/send_feedback.html', {"tour_feedback": tour_feedback})
class add_booking(View):
    def get(self, request):
        return render(request, 'customer_template/add_booking.html')
    def post(self, request):
        if 'login_id' not in request.session:
            messages.error(request, 'Session expired. Please log in again.')
            return redirect('user_app:userlogin')
        try:
            login = User_profile.objects.get(id=request.session['login_id'])
            customer = customer_model.objects.filter(customer=login).first()
            if not customer:
                messages.error(request, 'You are not authorized to upload a tutorial.')
                return redirect('user_app:userlogin')
        except User_profile.DoesNotExist:
            messages.error(request, 'Invalid session. Please log in again.')
            return redirect('user_app:userlogin')
        book = booking_forms(request.POST, request.FILES)
        if book.is_valid():
            c = book.save(commit=False)
            c.lock = customer
            c.connect = login
            c.save()
            messages.success(request, 'Booking added successfully.')
            return redirect('view_booking')
        else:
            messages.error(request, ' Please try again.')
        return render(request, 'customer_template/add_booking.html')
class add_complaints(View):
    def get(self,request):
        comp=send_feedback.objects.filter(is_active=True)
        return render(request,'customer_template/complaints_agent.html',{"comp":comp})
    def post(self, request):
        agent_complaint = complaint_agents(request.POST)

        if agent_complaint.is_valid():
            agent_complaint.save()
            return HttpResponse("successfully saved")

        return render(request, 'customer_template/complaints_agent.html', {"agent_complaint": agent_complaint})
class rest_complaints(View):
    def get(self,request):
        comp=mycomplaints.objects.filter(is_active=True)
        return render(request,'customer_template/complaints_rest.html',{"comp":comp})
    def post(self, request):
        rest_complaint = complaint_rest(request.POST)

        if rest_complaint.is_valid():
            rest_complaint.save()
            return HttpResponse("successfully saved")

        return render(request, 'customer_template/complaints_rest.html', {"rest_complaint": rest_complaint})
class view_reply(View):
    def get(self,request):
        replies=send_feedback.objects.all()
        return render(request,'customer_template/view_replies.html',{'replies':replies})
class view_reply_rest(View):
    def get(self,request):
        rest_reply=mycomplaints.objects.all()
        return render(request,'customer_template/view_restreply.html',{'rest_reply':rest_reply})
class view_reply_travel(View):
    def get(self,request):
        travel_reply=complaints.objects.all()
        return render(request,'customer_template/view_travelreply.html',{'travel_reply':travel_reply})


#booking


class view_bookings(View):
    def get(self, request):
        try:
            content = request.session.get('login_id')
            content_media = booking.objects.filter(connect=content)
        except User_profile.DoesNotExist:
            return HttpResponse("User profile not found for the current user", status=404)
        return render(request, 'customer_template/view_prvs_booking.html', {'mybook': content_media})