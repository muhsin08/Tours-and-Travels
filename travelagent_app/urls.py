from django.urls import path
from .views import *
urlpatterns = [
path('travelagent/',travel_agent.as_view(),name="travelagent"),
path('packages/',travel_packages.as_view(),name="travelpackage"),
path('package_view/',view_package.as_view(),name="package_view"),
path('edit/<int:id>/',editpackage.as_view(),name="edit"),
path('delete/<int:id>/',deletepackage.as_view(),name="delete"),
path('view_complaint/',view_complaint.as_view(),name="view_complaint"),
path('reply_complaint/<int:id>/', reply_complaint.as_view(), name="reply_complaint"),
]