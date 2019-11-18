from django.urls import path

from . import views
urlpatterns = [

path('list',views.list_page, name = 'list_page'),
path('api/list',views.list_api, name = 'list_api'),

]




# path   网站的前缀
