from django.http import HttpResponse, JsonResponse
# from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.models import User # STEP 1: Import the user
from django.contrib.auth import authenticate, login,logout


def list_page(request):
    return render(request, "list/list.html",{},)

def list_api(request):

  return JsonResponse({

       })
