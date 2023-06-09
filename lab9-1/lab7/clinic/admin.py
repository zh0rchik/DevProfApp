from django.contrib import admin
from .models import Patient, Doctor, Visit, MedicalRecord, MedicalCard, PreferredDoctor

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Visit)
admin.site.register(MedicalRecord)
admin.site.register(MedicalCard)
admin.site.register(PreferredDoctor)