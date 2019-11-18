from django.urls import path

from . import views
urlpatterns = [

path('list',views.list_page, name = 'list_page'),
path('api/list',views.ListApi, name = 'list_api'),
path('report_01',views.report_01_page, name = 'report_01_page'),
path('api/report_01',views.Report_01Api.as_view()),

]




# path   网站的前缀
