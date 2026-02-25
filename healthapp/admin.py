from django.contrib import admin
from healthapp.models import patient,Myappointment

from healthapp.models import*
#you can import using an asterisk(*)

# Register your models here.
admin.site.register(patient)
admin.site.register(Myappointment)