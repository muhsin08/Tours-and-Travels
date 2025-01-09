from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from restaurant_app.models import *
from restaurant_app.forms import *
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class resturent_food(View):
    def get(self, request):
        my_resturent = restaurant_model.objects.filter(is_active=True)
        return render(request, 'restaurant_template/register.html',{'form':my_resturent})

    def post(self, request):
        item = restaurant_form(request.POST)
        if item.is_valid():
            kitchen = item.save(commit=False)
            dish = User_profile.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password'],
                email=request.POST['email'],
                user_type='RESTAURANT'
            )
            kitchen.resturent = dish
            kitchen.save()

            return HttpResponse('''<script>alert(" Registration successfully.");window.location="restaurant_app/home_page"</script>''')

        return render(request, 'restaurant_template/register.html', {'fry':item})
class MainPageView(View):

    def get(self, request):
        return render(request, 'restaurant_template/homepage.html')
class rooms_availabilty(View):
    def get(self, request):
        return render(request, 'restaurant_template/add_room.html')

    def post(self, request):
        if 'login_id' not in request.session:
            messages.error(request, 'Session expired. Please log in again.')
            return redirect('user_app:userlogin')

        try:
            login = User_profile.objects.get(id=request.session['login_id'])
            restaurant = restaurant_model.objects.filter(resturent=login).first()
            if not restaurant:
                messages.error(request, 'You are not authorized to upload a package.')
                return redirect('user_app:userlogin')
        except User_profile.DoesNotExist:
            messages.error(request, 'Invalid session. Please log in again.')
            return redirect('user_app:userlogin')

        agent = RoomFacilitiesForm(request.POST)
        if agent.is_valid():
            c = agent.save(commit=False)
            c.lock = restaurant
            c.connect = login
            c.save()
            messages.success(request, 'Rooms added successfully.')
            return redirect('rooms_view')
        else:
            messages.error(request, 'There was an error with your submission.')
            return render(request, 'restaurant_template/add_room.html', {'set': agent})


class view_rooms(View):
    def get(self, request):
        try:
            content = request.session.get('login_id')
            content_media = Room.objects.filter(connect=content)
        except User_profile.DoesNotExist:
            return HttpResponse("User profile not found for the current user", status=404)
        return render(request, 'restaurant_template/manage_rooms.html', {'play': content_media})


class editrooms(View):
    def get(self, request, id):
        items = get_object_or_404(Room, pk=id)
        return render(request, 'restaurant_template/rooms_edit.html', {'try': items})

    def post(self, request, id):
        items = get_object_or_404(Room, pk=id)
        item = RoomFacilitiesForm(request.POST, request.FILES, instance=items)
        if item.is_valid():
            data = item.save(commit=False)
            data.connect = User_profile.objects.get(id=request.session['login_id'])
            data.save()
            messages.success(request, 'Rooms edited sucessfully')
            return redirect('rooms_view')
        return render(request, 'restaurant_template/edit_dish.html', {'try': items})


class deleterooms(LoginRequiredMixin, View):
    def get(self, request, id):
        item = get_object_or_404(Room, id=id)
        return render(request, 'restaurant_template/rooms_delete.html')

    def post(self, request, id):
        item = get_object_or_404(Dish, id=id)
        item.delete()
        messages.success(request, 'Rooms deleted successfully.')
        return redirect('rooms_view')

class dish_items(View):
    def get(self, request):
        return render(request, 'restaurant_template/add_dish_items.html')

    def post(self, request):
        if 'login_id' not in request.session:
            messages.error(request, 'Session expired. Please log in again.')
            return redirect('user_app:userlogin')

        try:
            login = User_profile.objects.get(id=request.session['login_id'])
            restaurant = restaurant_model.objects.filter(resturent=login).first()
            if not restaurant:
                messages.error(request, 'You are not authorized to upload a package.')
                return redirect('user_app:userlogin')
        except User_profile.DoesNotExist:
            messages.error(request, 'Invalid session. Please log in again.')
            return redirect('user_app:userlogin')

        agent = DishForm(request.POST, request.FILES)
        if agent.is_valid():
            c = agent.save(commit=False)
            c.lock = restaurant
            c.connect = login
            c.save()
            messages.success(request, 'Dishes added successfully.')
            return redirect('dish_view')
        else:
            messages.error(request, 'There was an error with your submission.')
            return render(request, 'restaurant_template/add_dish_items.html', {'items': agent})


class view_dish(View):
    def get(self, request):
        try:
            content = request.session.get('login_id')
            content_media = Dish.objects.filter(connect=content)
        except User_profile.DoesNotExist:
            return HttpResponse("User profile not found for the current user", status=404)
        return render(request, 'restaurant_template/manage_dish_item.html', {'fry': content_media})


class editdish(View):
    def get(self, request, id):
        items = get_object_or_404(Dish, pk=id)
        return render(request, 'restaurant_template/edit_dish.html', {'menu': items})

    def post(self, request, id):
        items = get_object_or_404(Dish, pk=id)
        item = DishForm(request.POST, request.FILES, instance=items)
        if item.is_valid():
            data = item.save(commit=False)
            data.connect = User_profile.objects.get(id=request.session['login_id'])
            data.save()
            messages.success(request, 'Dishes edited sucessfully')
            return redirect('dish_view')
        return render(request, 'restaurant_template/edit_dish.html', {'menu': items})


class deletedish(LoginRequiredMixin, View):
    def get(self, request, id):
        item = get_object_or_404(Dish, id=id)
        return render(request, 'restaurant_template/delete_dish.html')

    def post(self, request, id):
        item = get_object_or_404(Dish, id=id)
        item.delete()
        messages.success(request, 'Dishes deleted successfully.')
        return redirect('dish_view')
class view_mycomplaint(View):
    def get(self,request):
        comp=mycomplaints.objects.all()
        return render(request,'restaurant_template/view_mycomplaint.html',{'comp':comp})
class reply_mycomplaint(View):
    def get(self,request,id):
        comp = get_object_or_404(mycomplaints, pk=id)
        form=reply_mycomplaints(instance=comp)
        return render(request,'restaurant_template/reply_mycomplaint.html',{'form':form})
    def post(self,request,id):
        compl=get_object_or_404(mycomplaints,pk=id)
        form=reply_mycomplaints(request.POST,instance=compl)
        if form.is_valid():
            reply=form.save(commit=False)
            reply.save()
            return HttpResponse("reply send")
        return render(request,'restaurant_template/reply_mycomplaint.html',{'form':form})




    #rooms#

