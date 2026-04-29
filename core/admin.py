from django.contrib import admin
from .models import Patient, Doctor, MedicalRecord, Appointment, Ward, Medicine

admin.site.site_header = "County Health System Admin"
admin.site.site_title = "County Health Portal"
admin.site.index_title = "Hospital Management Dashboard"

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number')
    search_fields = ('first_name', 'last_name', 'phone_number')

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'stock_quantity', 'expiry_date')
    list_filter = ('expiry_date',)

admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(MedicalRecord)
admin.site.register(Ward)
