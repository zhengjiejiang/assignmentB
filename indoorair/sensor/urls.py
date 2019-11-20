from django.urls import path

from . import views

urlpatterns = [
    path('sensor/id:', views.sensor_retrieve_page, name='sensor_retrieve_page'),
    # path('sensor/api/<int:id>',views.retrieve_api, name = 'retrieve_api'),




]




# path   网站的前缀
