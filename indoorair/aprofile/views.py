from django.http import JsonResponse
from django.shortcuts import render

def retrieve_profile_page(request):
    return render(request, "aprofile/retrieve.html",{},)

def update_profile_page(request):
    return render(request, "aprofile/update.html",{},)
def update_profile_api(request):

  return JsonResponse({

       })
def retrieve_profile_api(request):

  return JsonResponse({ })
