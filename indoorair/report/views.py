from django.http import HttpResponse, JsonResponse
import csv
# from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.models import User # STEP 1: Import the user
from django.contrib.auth import authenticate, login,logout
from foundations.models import Sensor,TimeSeriesDatum
from rest_framework import response,status,views


def report_list_page(request):
    return render(request, "report/list.html",{})

def report_01_page(request):
    return render(request, "report/report_01.html", {})




class Report_01Api(views.APIView):
    def post(self, request):
        report_01 = Report.objects.create(
        contents = random_string_generator(size=1000, chars=string.ascii_lowercase + string.digits))

        return response.Response(
            status = status.HTTP_200_OK,
            data = {
                'result' : ' Successfully!'
            }
        )

def report_01_temp (request):
    # Create the HttpResponse object with the appropriate CSV header.
    data = TimeSeriesDatum.objects.filter(
        sensor__name = "Temperature",
        sensor__instrument__user = request.user,
    )



    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="temperature_data.csv"'
    writer = csv.writer(response)
    writer.writerow(['sensor_id','time', 'value' ])
    # writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    # writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])
    for datum in data:
        writer.writerow([datum.sensor.id,datum.time,datum.value])



    return response
















class ListApi(views.APIView):
    def get(self, request):
        data = TimeseriesDatum.objects.filter(user=request.user)
        results = []
        for datum in data.all():
            results.append({
                'id': instrument.id,
                'name': instrument.name,
            })
        return response.Response(
            status = status.HTTP_200_OK,
            data = {
                'result' : ' Successfully !'
                }
            )
