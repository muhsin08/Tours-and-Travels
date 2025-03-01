from django.urls import path
from .views import *

urlpatterns = [
path('restaurant/',resturent_food.as_view(),name="restaurant"),
path('MainPageView/',MainPageView.as_view(),name="MainPageView"),
path('logout/',RestaurantLogoutView.as_view(), name='logout'),
path('rooms/',rooms_availabilty.as_view(),name="rooms"),
path('rooms_view/',view_rooms.as_view(),name="rooms_view"),
path('Edit/<int:id>/',editrooms.as_view(),name="Edit"),
path('Delete/<int:id>/',deleterooms.as_view(),name="Delete"),
path('dish/',dish_items.as_view(),name="dishs"),
path('dish_view/',view_dish.as_view(),name="dish_view"),
path('restaurant/dish_edit/<int:id>/', editdish.as_view(), name='dish_edit'),
path('restaurant/delete_dish/<int:id>/',deletedish.as_view(), name='Delete_dish'),
path('view_complaints/',view_complaints.as_view(),name="view_complaints"),
path('reply_mycomplaint/<int:id>/',reply_mycomplaint.as_view(),name="reply_mycomplaint"),
path('view_review/',view_review.as_view(),name="view_review")
    ]
