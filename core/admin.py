from django.contrib import admin
from .models import Patient, Doctor, MedicalRecord, Appointment, Ward

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(MedicalRecord)
admin.site.register(Appointment)
admin.site.register(Ward)
