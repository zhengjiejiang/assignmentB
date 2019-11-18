from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status, response, views
from dashboard.serializer import AvgSeriliazer



def dashboard_page(request):
    return render(request, "dashboard/dashboard.html", {})





class DashboardApi(views.APIView):
    def post(self, request):
        serializer = AddSeriliazer(data= request.data)
        serializer.is_valid(raise_exception =True)
        serializer.save()
        data = serializer.objects.all()
        return JsonResponse(data)





def api_dashboard(request):
    return JsonResponse({
         'avg_temperature': 20,
         'avg_pressure': 20,
         'avg_co2': 20,
         'avg_tvoc': 20,
         'avg_humidity': 20,
    })
