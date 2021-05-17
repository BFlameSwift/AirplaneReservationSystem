from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Flight)

class BackgroundAdmin(admin.ModelAdmin):

    # exclude = ('plane_capacity',)
    list_display = ('flight_number','flight_type',
                    'origination','destination','starting_time','arrival_time',
                    'flight_price','plane_type',)
    exclude = ('plane_capacity')
