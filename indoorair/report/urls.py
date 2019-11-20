from django.urls import path

from . import views
urlpatterns = [

path('reports',views.report_list_page, name = 'report_list_page'),
path('report/api/1',views.report_01_temp, name = 'report_api_01'),
path('report/1',views.report_01_page, name = 'report_01_page'),
path('api/report_01',views.Report_01Api.as_view()),

]




# path   网站的前缀
