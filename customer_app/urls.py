from . import views

from django.urls import path
from .views import *
urlpatterns = [
    path('customer/', customer_book.as_view(), name="customer"),
    path('home_view/', homepage.as_view(), name="home_view"),
    path('packages/', view_packages.as_view(), name="packages"),
    path('PackageBooking/<int:id>/', PackageBooking.as_view(), name='PackageBooking'),
    path('view_bookings/',view_bookings.as_view(),name="view_bookings"),
    path('PaymentProcess/<int:id>/',PaymentProcess.as_view(),name="PaymentProcess"),

    path('api/view-packages/', ViewPackagesAPIView.as_view(), name='view_packages_api'),
    path('book-now/<int:id>/', BookNowAPIView.as_view(), name='book_now_api'),
    path('videos/', view_videos.as_view(), name="videos"),
    path('api/vr-videos/', VRVideosAPIView.as_view(), name='vr_videos_api'),
    path('upcom_fest/',upcom_fest_view.as_view(),name="upcom_fest"),
    path('view_trend_place/',trending_place_view.as_view(),name="view_trend_place"),
    path('sendfeedback/',add_feedback.as_view(),name="sendfeedback"),
    path('view_reply/',view_reply.as_view(),name="view_reply"),
    path('restaurant_view/',restaurant_view.as_view(),name="restaurant_view"),
    path('explore_rest/<int:id>/',explore_rest.as_view(),name="explore_rest"),
    path('dishes_view/<int:id>/',dishes_view.as_view(),name="dishes_view"),
    path('DishBookingView/<int:id>/',DishBookingView.as_view(),name="DishBookingView"),
    path('view_dishbooking/',view_dishbooking.as_view(),name="view_dishbooking"),
    path('rooms_view/<int:id>/',rooms_view.as_view(),name="rooms_view"),
    path('availability/',views.available_rooms_view,name="available_rooms"),
    path('room_booking/<int:id>/',room_booking.as_view(), name='room_booking'),
    path('view_roombook/',view_roombook.as_view(),name="view_roombook"),
    path('add_complaints/<int:id>/',AddComplaints.as_view(),name="add_complaints"),
    path('view_restreply/',view_restreply.as_view(),name="view_restreply"),
    path('search/', SearchSpot.as_view(), name='search_spot'),
    path('explore_spot/<int:id>/',explore_spot.as_view(),name="explore_spot"),
    path('trvelagent_view/', trvelagent_view.as_view(), name="trvelagent_view"),
    path('explore_travel/<int:id>/',explore_travel.as_view(),name="explore_travel"),
    path('Package_view/<int:id>/', Package_view.as_view(), name="Package_view"),
    path('travelComplaints/<int:id>/',travelComplaints.as_view(),name="travelComplaints"),
    path('Send_review/<int:id>/',Send_review.as_view(),name="Send_review"),
    path('Travel_review/<int:id>/',Travel_review.as_view(),name="Travel_review"),
    path('view_travelreply/', view_travelreply.as_view(), name="view_travelreply"),

]