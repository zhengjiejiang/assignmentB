from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login_page, name='login_page'),
    path('register', views.register_page, name='register_page'),
    path('api/login', views.LoginSerializerAPI.as_view(), name='login_api'),
    path('api/register', views.RegisterSerializerAPI.as_view(), name='register_api'),
    path('register/ok', views.registered_success_page, name='registered_page'),
    path('api/logout',views.post_logout_api, name = 'logout_api'),



]




# path   网站的前缀
