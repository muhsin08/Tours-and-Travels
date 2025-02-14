from django.urls import path
from .views import *
app_name='user_app'
urlpatterns = [
    path('', User_login.as_view(), name='userlogin'),
    path('manager/',manager_home_load.as_view(),name="loadmanager"),
    path('rastaurant/',restaurant_home_load.as_view(), name='loadrestaurant'),
    path('customer/',customer_home_load.as_view(),name='loadcustomer'),
    path('travel_agengt/',travelagent_home_load.as_view(),name='loadtravelagent')
    ]