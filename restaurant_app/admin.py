from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(restaurant_model)
admin.site.register(Room)
admin.site.register(Dish)
admin.site.register(Review)
admin.site.register(mycomplaints)
admin.site.register(Booking)
admin.site.register(BookDish)