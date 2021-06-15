from django.contrib import admin
from .models import Doctor, Patient


class PatientInline(admin.TabularInline):
    model = Patient
    extra = 0


class DoctorAdmin(admin.ModelAdmin):
    inlines = [PatientInline]


admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient)