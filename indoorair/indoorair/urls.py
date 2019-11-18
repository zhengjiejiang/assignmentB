# insta_project/urls.py
from django.contrib import admin
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('',include('gateway.urls')),
    path('',include('dashboard.urls')),
    path('',include('aprofile.urls')),
    path('',include('instrument.urls')),
    path('',include('report.urls')),
    path('',include('sensor.urls')),


]
