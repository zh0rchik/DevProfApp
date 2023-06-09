from django.contrib import admin
from django.urls import path
from clinic.views import *

urlpatterns = [
    #path('profile/', profile, name='profile'),
    path('logout/', logout_view, name='logout'),
    path('exp', exp, name='exp'),
    path('register', register, name='register'),
    path('', login, name='login'),

    path('admin/', admin.site.urls),

    path('doctors/', DoctorListView.as_view(), name='doctor_list'),
    path('doctors/<int:pk>/update/', DoctorUpdateView.as_view(), name='doctor_update'),
    path('doctors/create/', DoctorCreateView.as_view(), name='doctor_create'),
    path('doctors/<int:pk>/delete/', DoctorDeleteView.as_view(), name='doctor_delete'),

    path('patients/', PatientListView.as_view(), name='patient_list'),
    path('patients/create/', PatientCreateView.as_view(), name='patient_create'),
    path('patients/<int:pk>/update/', PatientUpdateView.as_view(), name='patient_update'),
    path('patients/<int:pk>/delete/', PatientDeleteView.as_view(), name='patient_delete'),

    path('medicalcards/', MedicalCardListView.as_view(), name='medicalcard_list'),
    path('medicalcards/create/', MedicalCardCreateView.as_view(), name='medicalcard_create'),
    path('medicalcards/<int:pk>/update/', MedicalCardUpdateView.as_view(), name='medicalcard_update'),
    path('medicalcards/<int:pk>/delete/', MedicalCardDeleteView.as_view(), name='medicalcard_delete'),

    path('visits/', VisitListView.as_view(), name='visit_list'),
    path('visits/create/', VisitCreateView.as_view(), name='visit_create'),
    path('visits/<int:pk>/update/', VisitUpdateView.as_view(), name='visit_update'),
    path('visits/<int:pk>/delete/', VisitDeleteView.as_view(), name='visit_delete'),

    path('medicalrecords/', MedicalRecordListView.as_view(), name='medicalrecord_list'),
    path('medicalrecords/create/', MedicalRecordCreateView.as_view(), name='medicalrecord_create'),
    path('medicalrecords/<int:pk>/update/', MedicalRecordUpdateView.as_view(), name='medicalrecord_update'),
    path('medicalrecords/<int:pk>/delete/', MedicalRecordDeleteView.as_view(), name='medicalrecord_delete'),
]