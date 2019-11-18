from django.http import HttpResponse, JsonResponse
# from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.models import User # STEP 1: Import the user
from django.contrib.auth import authenticate, login,logout


def retrieve_page(request):
   user = request.user
   context = {
       'user': user,
   }
   return render(request, "sensor/retrieve.html", context)
