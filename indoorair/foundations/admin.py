from django.contrib import admin

# Register your models here.
from .models import Instrument, TimeSeriesDatum, Sensor , Data

admin.site.register(Instrument)
admin.site.register(TimeSeriesDatum)
admin.site.register(Sensor)
admin.site.register(Data)
