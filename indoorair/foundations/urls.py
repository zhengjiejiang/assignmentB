from django.urls import path

from . import views

urlpatterns = [
    path('instrument', views.instrument, name='instrument'),

]




# path   网站的前缀
