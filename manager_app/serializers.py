from rest_framework import serializers
from .models import *

class VRVideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = VR_vedios
        fields = '__all__'  # Or list specific fields you want to expose