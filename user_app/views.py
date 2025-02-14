from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.views import View
import json
import datetime

from django.http import HttpResponse
from django.http import HttpResponseBadRequest
# Create your views here.
class manager_home_load(View):
    def get(self,request):
        return render(request,'manager_template/homepage.html')
class restaurant_home_load(View):
    def get(self,request):
        return render(request,'restaurant_template/homepage.html')
class travelagent_home_load(View):
    def get(self,request):
        return render(request,'travelagent_template/homepage.html')
class customer_home_load(View):
    def get(self,request):
        return render(request,'customer_template/homepage.html')
class User_login(View):
    template_name ="login.html"
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        user_type = ""
        response_dict = {"success": False}
        landing_page_url = {
            "MANAGER": "user_app:loadmanager",
            "RESTAURANT": "user_app:loadrestaurant",
            "TRAVELAGENT": "user_app:loadtravelagent",
            "CUSTOMER": "user_app:loadcustomer",
        }
        username = request.POST.get("username")
        password = request.POST.get("password")
        authenticated = authenticate(username=username, password=password)
        try:
            user = User_profile.objects.get(username=username)
            request.session['login_id'] = user.id
            if user.status in ["pending", "rejected"] and user.user_type in ["TRAVELAGENT"]:
                    response_dict[
                        "reason"] = f"your {user.user_type.lower()} account status is {user.status}."
                    messages.error(request, response_dict["reason"])
                    return render(request, 'login.html', {"error_message": response_dict["reason"]})

        except User_profile.DoesNotExist:
            response_dict[
                "reason"
            ] = "No account found for this username. Please signup."
            messages.error(request, response_dict["reason"])
        if not authenticated:
            response_dict["reason"] = "Invalid credentials."
            messages.error(request, response_dict["reason"])
            return redirect(request.GET.get("from") or "user_app:userlogin")

        else:

            session_dict = {"real_user": authenticated.id}
            token, c = Token.objects.get_or_create(
                user=user, defaults={"session_dict": json.dumps(session_dict)}
            )

            user_type = authenticated.user_type

            request.session["data"] = {
                "user_id": user.id,
                "user_type": user.user_type,
                "token": token.key,
                "username": user.username,
                "status": user.is_active,
            }
            request.session["user"] = authenticated.username
            request.session["token"] = token.key
            request.session["status"] = user.is_active
            return redirect(landing_page_url[user_type])
        return redirect(request.GET.get("from") or loadlogin)
