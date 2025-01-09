from django.urls import path
from .views import *
urlpatterns = [
    path('addtourist_places/', my_tour.as_view(), name="tourist_places"),
    path('manage_place/', view_touristplace.as_view(), name="manage_place"),
    path('manager_app/Edit_place/<int:mk>/', editplaces.as_view(), name="Edit_place"),
    path('manager_app/Delete_place/<int:mk>/', deleteplaces.as_view(), name="delete_place"),
    path('add_spots/', my_spot.as_view(), name="add_spots"),
    path('spot_view/', view_spot.as_view(), name="spot_view"),
    path('spot_edit/<int:sk>/', editspot.as_view(), name='spot_edit'),
    path('delete_spot/<int:sk>/', deletespot.as_view(), name='Delete_spot'),
    path('add_festivals/', upcoming_festivals.as_view(), name="add_festivals"),
    path('view_festivals/', view_festivals.as_view(), name="view_festivals"),
    path('fest_edit/<int:fk>/', editfestivals.as_view(), name='fest_edit'),
    path('delete_fest/<int:fk>/', deletefestivals.as_view(), name='Delete_fest'),
    path('add_videos/', add_VRvideos.as_view(), name="add_videos"),
    path('add_hotel/', add_hotels.as_view(), name="add_hotel"),
    path('view_hotels/', view_Hotel.as_view(), name="view_hotels"),
    path('hotel_edit/<int:hk>/', edithotel.as_view(), name='hotel_edit'),
    path('delete_hotel/<int:hk>/', deletehotel.as_view(), name='delete_hotel'),
    path('tour_package/', tourism_packages.as_view(), name="tour_package"),
    path('manage_tour/', view_my_package.as_view(), name="manage_tour"),
    path('edit_tour/<int:td>/', edit_package.as_view(), name="edit_tour"),
    path('delete_tour/<int:td>/', delete_package.as_view(), name="delete_tour"),
    path('view_user/', view_user.as_view(), name="view_user"),
    path ('view_feedback/',view_feedback.as_view(),name="view_feedback"),
    path('reply_feeback/<int:id>/', reply_feeback.as_view(), name="reply_feeback"),
    path('view_userbooking/',view_userbooking.as_view(),name="view_userbooking"),
    path('verify/',Verify.as_view(),name="verify"),
    path('verification/<int:id>/',Verify.as_view(),name="verification")

]
