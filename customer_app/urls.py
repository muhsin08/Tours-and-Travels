from django.urls import path
from .views import *
urlpatterns = [
    path('customer/', customer_book.as_view(), name="customer"),
    path('home_view/', homepage.as_view(), name="home_view"),
    path('packages/', view_packages.as_view(), name="packages"),
    path('videos/', view_videos.as_view(), name="videos"),
    path('upcom_fest/',upcom_fest_view.as_view(),name="upcom_fest"),
    path('view_trend_place/',trending_place_view.as_view(),name="view_trend_place"),
    path('sendfeedback/',add_feedback.as_view(),name="sendfeedback"),
    path('add_bookings/', add_booking.as_view(), name="add_bookings"),
    path('view_booking/',view_bookings.as_view(),name="view_booking"),
    path('add_complaints/',add_complaints.as_view(),name="add_complaints"),
    path('rest_complaints/',rest_complaints.as_view(),name="rest_complaints"),
    path('view_reply/',view_reply.as_view(),name="view_reply"),
    path('view_reply_rest/',view_reply_rest.as_view(),name="view_reply_rest"),
    path('view_reply_travel/',view_reply_travel.as_view(),name="view_reply_travel")
]