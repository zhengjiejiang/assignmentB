from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse



def index_page(request):
    return render(request, 'homepage/index.html', {

    })

def contact(request):
    return render(request, 'homepage/contact.html', {

    })


def api_version(request):
    return JsonResponse({'version': 'Melody'})
