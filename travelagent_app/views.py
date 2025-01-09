from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from travelagent_app.forms import *
from .models import *
from user_app .models import User_profile
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your viewstravel_package here.

class travel_agent(View):
    def get(self, request):
        my_travelagent = travelagent_model.objects.filter(is_active=True)
        return render(request, 'travelagent_template/register_tvl.html',{'form':my_travelagent})

    def post(self, request):
        tripp = travelagent_form(request.POST)
        if tripp.is_valid():
            place = tripp.save(commit=False)
            trend = User_profile.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password'],
                email=request.POST['email'],
                user_type='TRAVELAGENT'
            )
            place.travelagent = trend
            place.save()
            return HttpResponse('''<script>alert("Registration added successfully.");window.location="turfapp/view/"</script>''')



        return render(request, 'travelagent_template/register_tvl.html', {'form':tripp})


class travel_packages(View):
    def get(self, request):
        return render(request, 'travelagent_template/pckages_add.html')

    def post(self, request):
        if 'login_id' not in request.session:
            messages.error(request, 'Session expired. Please log in again.')
            return redirect('user_app:userlogin')

        try:
            login = User_profile.objects.get(id=request.session['login_id'])
            travelagent = travelagent_model.objects.filter(travelagent=login).first()
            if not travelagent:
                messages.error(request, 'You are not authorized to upload a package.')
                return redirect('user_app:userlogin')
        except User_profile.DoesNotExist:
            messages.error(request, 'Invalid session. Please log in again.')
            return redirect('user_app:userlogin')

        agent = packages_form(request.POST, request.FILES)
        if agent.is_valid():
            c = agent.save(commit=False)
            c.lock = travelagent
            c.connect = login
            c.save()
            messages.success(request, 'Package added successfully.')
            return redirect('package_view')
        else:
            messages.error(request, 'There was an error with your submission.')
            return render(request, 'travelagent_template/pckages_add.html', {'form': agent})


class view_package(View):
    def get(self, request):
        try:
            content = request.session.get('login_id')
            content_media = travel_package.objects.filter(connect=content)
        except User_profile.DoesNotExist:
            return HttpResponse("User profile not found for the current user", status=404)
        return render(request, 'travelagent_template/manage_packages.html', {'pack': content_media})


class editpackage(View):
    def get(self,request,id):
        items=get_object_or_404(travel_package,pk=id)
        return render(request,'travelagent_template/package_edit.html',{'data':items})
    def post(self,request,id):
        items=get_object_or_404(travel_package,pk=id)
        item=packages_form(request.POST,request.FILES,instance=items)
        if item.is_valid():
            data=item.save(commit=False)
            data.connect = User_profile.objects.get(id=request.session['login_id'])
            data.save()
            messages.success(request,'packages edited sucessfully')
            return redirect('package_view')
        return render(request,'travelagent_template/package_edit.html',{'data':items})


class deletepackage(LoginRequiredMixin, View):
    def get(self, request, id):
        item = get_object_or_404(travel_package, id=id)
        return render(request, 'travelagent_template/package_delete.html')
    def post(self, request, id):
        item = get_object_or_404(travel_package, id=id)
        item.delete()
        messages.success(request, 'package deleted successfully.')
        return redirect('package_view')

class view_complaint(View):
    def get(self,request):
        comp=complaints.objects.all()
        return render(request,'travelagent_template/view_complaints.html',{'comp':comp})
class reply_complaint(View):
    def get(self,request,id):
        comp = get_object_or_404(complaints, pk=id)
        form=reply_complaints(instance=comp)
        return render(request,'travelagent_template/reply_complaints.html',{'form':form})
    def post(self,request,id):
        compl=get_object_or_404(complaints,pk=id)
        form=reply_complaints(request.POST,instance=compl)
        if form.is_valid():
            reply=form.save(commit=False)
            reply.save()
            return HttpResponse("reply send")
        return render(request,'travelagent_template/reply_complaints.html',{'form':form})





                              #Delete Posts




                       #Edit Post

