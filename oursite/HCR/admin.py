from django.contrib import admin
from HCR.models import Appointment, Doctor, Patient
# from HCR.dao import *

admin.site.register(Appointment)
admin.site.register(Doctor)
admin.site.register(Patient)

# admin.site.register(PatientDAO)
# admin.site.register(AppointmentDAO)
# admin.site.register(DoctorDAO)