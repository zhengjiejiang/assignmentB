from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('contact', views.contact, name='contact'),
    path('api/version', views.api_version, name='api_version'),

]


# path   网站的前缀
