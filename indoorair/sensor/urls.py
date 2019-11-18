from django.urls import path

from . import views

urlpatterns = [
    path('retrieve', views.retrieve_page, name='retrieve_page'),




]




# path   网站的前缀
