from django.http import HttpResponse, JsonResponse
# from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.models import User # STEP 1: Import the user
from django.contrib.auth import authenticate, login,logout
from foundations.models import Sensor,TimeSeriesDatum
from rest_framework import response,status,views


def list_page(request):
    return render(request, "list/list.html",{},)

def list_api(request):

  return JsonResponse({

       })

def report_01_page(request):
    return render(request, "report/report_01.html", {})




class Report_01Api(views.APIView):
    def post(self, request):
        report_01 = Report.objects.create(
        contents = random_string_generator(size=1000, chars=string.ascii_lowercase + string.digits))

        return response.Response(
            status = status.HTTP_200_OK,
            data = {
                'result' : 'get Successfully!'
            }
        )


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
                'result' : ' get Successfully !'
                }
            )
