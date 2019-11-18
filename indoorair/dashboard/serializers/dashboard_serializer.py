from rest_framework import serializers
from django.contrib.auth.models import User # STEP 1: Import the user
from django.contrib.auth import authenticate, login,logout
from rest_framework.validators import UniqueValidator




class DashboardSerializer(serializers.BaseSerializer):
    def to_representation(self,obj):
        print(instruments)
        results = []
        for instrument in instruments:
            results.append({
            ' name ' : instrument.name,
            })
        
