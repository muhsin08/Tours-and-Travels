from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from travelagent_app .models import *
from travelagent_app .forms import *
from customer_app .models import *
from user_app .models import *
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib import messages



# Create your views here.
class my_tour(View):
    def get(self,request):
        tourist=add_turistplaces.objects.filter(is_active=True)
        return render(request,'manager_template/add_touristplaces.html',{"tour":tourist})

    def post(self, request):
        tour_place = turistplace_form(request.POST, request.FILES)

        if tour_place.is_valid():
            tour_place.save()
            return HttpResponse('''
                 <script>
                     alert("Places successfully added");
                     window.location.href = "manage_place";  // redirect to the 'manage_place' URL
                 </script>
             ''')

        return render(request, 'manager_template/add_touristplaces.html', {'tour_place': tour_place})
class view_touristplace(View):
    def get(self,request):
        data_places=add_turistplaces.objects.all()
        return render(request,'manager_template/manage_tourist_place.html',{'place':data_places})
class editplaces(View):
    def get(self,request,mk):
        edit_place=add_turistplaces.objects.get(pk=mk)
        earth=turistplace_form(instance=edit_place)
        return render(request,'manager_template/edit_places.html',{'area':earth})

    def post(self, request, mk):
        edit_tour = add_turistplaces.objects.get(pk=mk)
        long = turistplace_form(request.POST, request.FILES, instance=edit_tour)
        if long.is_valid():
            long.save()
            return redirect("manage_place")
        return render(request,'manager_template/edit_places.html',{'area':long})

class deleteplaces(View):
        def get(self, request, mk):
            delete_dish = add_turistplaces.objects.get(pk=mk)
            return render(request, 'manager_template/delete_place.html')

        def post(self, request, mk):
            deleteplace_ = add_turistplaces.objects.get(pk=mk)
            deleteplace_.delete()
            return redirect("manage_place")
class my_spot(View):
    def get(self,request):
        spots=add_Spot.objects.filter(is_active=True)
        return render(request,'manager_template/add_spot.html',{"spot":spots})

    def post(self, request):
        tour_spot = SpotForm(request.POST, request.FILES)

        if tour_spot.is_valid():
            tour_spot.save()
            return HttpResponse("successfully saved")

        return render(request, 'manager_template/add_spot.html', {'tour_spot': tour_spot})
class view_spot(View):
    def get(self,request):
        data_spot=add_Spot.objects.all()
        return render(request,'manager_template/manage_spot.html',{'spoty':data_spot})
class editspot(View):
    def get(self,request,sk):
        edit_spot=add_Spot.objects.get(pk=sk)
        down=SpotForm(instance=edit_spot)
        return render(request,'manager_template/edit_spot.html',{'south':down})

    def post(self, request, sk):
        edit_myspot = add_Spot.objects.get(pk=sk)
        near = SpotForm(request.POST, request.FILES, instance=edit_myspot)
        if near.is_valid():
            near.save()
            return redirect("spot_view")
        return render(request,'manager_template/edit_spot.html',{'south':near})

class deletespot(View):
        def get(self, request, sk):
            delete_spot = add_Spot.objects.get(pk=sk)
            return render(request, 'manager_template/delete_spot.html')

        def post(self, request, sk):
            deletespot = add_Spot.objects.get(pk=sk)
            deletespot.delete()
            return redirect("spot_view")
class upcoming_festivals(View):
    def get(self,request):
        fest=Festival.objects.filter(is_active=True)
        return render(request,'manager_template/add_festivals.html',{"fest":fest})

    def post(self, request):
        tour_fest = festival_form(request.POST, request.FILES)

        if tour_fest.is_valid():
            tour_fest.save()
            return HttpResponse("successfully saved")

        return render(request, 'manager_template/add_festivals.html', {'tour_fest': tour_fest})

class view_festivals(View):
    def get(self,request):
        data_fest=Festival.objects.all()
        return render(request,'manager_template/manage_festivals.html',{'festy':data_fest})
class editfestivals(View):
    def get(self,request,fk):
        edit_fest=Festival.objects.get(pk=fk)
        upcom=festival_form(instance=edit_fest)
        return render(request,'manager_template/edit_festivals.html',{'enjoy':upcom})

    def post(self, request, fk):
        edit_myfest = Festival.objects.get(pk=fk)
        upcome = festival_form(request.POST, request.FILES, instance=edit_myfest)
        if upcome.is_valid():
            upcome.save()
            return redirect("view_festivals")
        return render(request,'manager_template/edit_festivals.html',{'enjoy':upcome})

class deletefestivals(View):
        def get(self, request, fk):
            delete_fest = Festival.objects.get(pk=fk)
            return render(request, 'manager_template/delete_festivals.html')

        def post(self, request, fk):
            deletefest= Festival.objects.get(pk=fk)
            deletefest.delete()
            return redirect("view_festivals")
class add_VRvideos(View):
    def get(self,request):
        videos=VR_vedios.objects.filter(is_active=True)
        tour_spot=add_Spot.objects.all()
        return render(request,'manager_template/add_VR_videos.html',{'video':videos,'spots':tour_spot})
    def post(self,request):
        tour_videos=VR_videosform(request.POST, request.FILES)
        if tour_videos.is_valid():
            tour_videos.save()
            return HttpResponse("seccessfully saved")
        tour_spot = add_Spot.objects.all()
        return render (request,'manager_template/add_VR_videos.html',{'video':tour_videos,'spots':tour_spot})
class add_hotels(View):
    def get(self,request):
        hot=hotel.objects.filter(is_active=True)
        return render(request,'manager_template/add_hotel.html',{"hot":hot})

    def post(self, request):
        tour_hotels = hotel_form(request.POST, request.FILES)

        if tour_hotels.is_valid():
            tour_hotels.save()
            return HttpResponse("successfully saved")

        return render(request, 'manager_template/add_hotel.html', {'tour_hotels': tour_hotels})
class view_Hotel(View):
    def get(self,request):
        data_hotel=hotel.objects.all()
        return render(request,'manager_template/manage_hotel.html',{'tasty':data_hotel})
class edithotel(View):
    def get(self,request,hk):
        edit_food=hotel.objects.get(pk=hk)
        hot_food=hotel_form(instance=edit_food)
        return render(request,'manager_template/edit_hotels.html',{'joy':hot_food})

    def post(self, request, hk):
        edit_myhot = hotel.objects.get(pk=hk)
        up_hot = hotel_form(request.POST, request.FILES, instance=edit_myhot)
        if up_hot.is_valid():
            up_hot.save()
            return redirect("view_hotels")
        return render(request,'manager_template/edit_hotels.html',{'joy':up_hot})

class deletehotel(View):
        def get(self, request, hk):
            deletehot = hotel.objects.get(pk=hk)
            return render(request, 'manager_template/delete_hotels.html')

        def post(self, request, hk):
            deletehot= hotel.objects.get(pk=hk)
            deletehot.delete()
            return redirect("view_hotels")
class tourism_packages(View):
    def get(self, request):
        tour_packages = travel_package.objects.filter(is_active=True)
        return render(request, 'manager_template/add_tour_package.html', {'packages': tour_packages})
    def post(self, request):
        my_pack = packages_form(request.POST, request.FILES)

        if my_pack.is_valid():
            my_pack.save()
            return HttpResponse("successfully saved")

        return render(request, 'manager_template/add_tour_package.html', {'my_pack': my_pack})
class view_my_package(View):
    def get(self,request):
        data_package=travel_package.objects.all()
        return render(request,'manager_template/manage_tour_pack.html',{'pack':data_package})
class edit_package(View):
    def get(self, request,td):
        editpackage = travel_package.objects.get(pk=td)
        form_ = packages_form(instance=editpackage)
        return render(request, 'manager_template/edit_tour_pack.html', {'data': form_})
    def post(self,request,td):
        edit_package=travel_package.objects.get(pk=td)
        form=packages_form(request.POST,request.FILES,instance=edit_package)
        if form.is_valid():
            form.save()
            return redirect("manage_tour")
        return render(request,'manager_template/edit_tour_pack.html',{'data': form})
class delete_package(View):
    def get(self,request,td):
        deletepackge=travel_package.objects.get(pk=td)
        return render(request,'manager_template/delete_tour_pack.html',)
    def post(self,request,td):
        delete_packge=travel_package.objects.get(pk=td)
        delete_packge.delete()
        return redirect("manage_tour")
class view_user(View):
    def get(self,request):
        user=customer_model.objects.all()
        my_user=User_profile.objects.all()
        return render(request,'manager_template/view_user.html',{'user':user ,'my_user':my_user})
class view_feedback(View):
    def get(self,request):
        feedback=send_feedback.objects.all()
        return render(request,'manager_template/view_feedbacks.html',{'feedback':feedback})
class reply_feeback(View):
    def get(self,request,id):
        feedb= get_object_or_404(send_feedback, pk=id)
        form=replyform(instance=feedb)
        return render(request,'manager_template/reply_feedback.html',{'form':form})
    def post(self,request,id):
        feedb=get_object_or_404(send_feedback,pk=id)
        form=replyform(request.POST,instance=feedb)
        if form.is_valid():
            reply=form.save(commit=False)
            reply.save()
            return HttpResponse("reply send")
        return render(request,'restaurant_template/reply_mycomplaint.html',{'form':form})
class view_userbooking(View):
    def get(self,request):
        data_booking=booking.objects.all()
        return render(request,'manager_template/view_userbooking.html',{'book':data_booking})
class Verify(View):
    def get(self,request):
        user_status=User_profile.objects.filter(user_type='TRAVELAGENT',status='pending')
        return render(request,'manager_template/verify_travelagent.html',{'user_status':user_status})
    def post(self,request,id):
        user_data=get_object_or_404(User_profile,id=id)
        new_status=request.POST.get('status')
        other=['verified','rejected']
        if new_status not in other:
            messages.error(request,"status not changed")
            return redirect('verify')
        user_data.status=new_status
        user_data.save()
        messages.success(request,f"{user_data.username} profile {user_data.status} sucessfully")
        return redirect('verify')