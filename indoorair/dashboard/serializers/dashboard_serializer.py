from rest_framework import serializers
from django.contrib.auth.models import User # STEP 1: Import the user
from django.contrib.auth import authenticate, login,logout
from rest_framework.validators import UniqueValidator




class DashboardSerializer(serializers.BaseSerializer):
    def to_representation(self,obj):
        print(instruments)
        return{
        'avg_temperature': 20,
        'avg_pressure': 20,
        'avg_co2': 20,
        'avg_tvoc': 20,
        'avg_humidity': 20,
        }
