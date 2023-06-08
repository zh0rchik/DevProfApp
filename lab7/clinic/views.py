from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Doctor, Patient, MedicalCard, Visit, MedicalRecord

#Врачи
class DoctorListView(ListView):
    model = Doctor
    template_name = 'doctor_list.html'
    context_object_name = 'doctors'

class DoctorCreateView(CreateView):
    model = Doctor
    template_name = 'doctor_create.html'
    fields = ['full_name', 'specialty', 'room_number']
    success_url = reverse_lazy('doctor_list')

class DoctorUpdateView(UpdateView):
    model = Doctor
    template_name = 'doctor_update.html'
    fields = ['full_name', 'specialty', 'room_number']
    success_url = reverse_lazy('doctor_list')

class DoctorDeleteView(DeleteView):
    model = Doctor
    template_name = 'doctor_delete.html'
    success_url = reverse_lazy('doctor_list')

#Пациенты
class PatientListView(ListView):
    model = Patient
    template_name = 'patient_list.html'
    context_object_name = 'patients'

class PatientCreateView(CreateView):
    model = Patient
    template_name = 'patient_create.html'
    fields = ['full_name', 'phone_number', 'preferred_doctors']
    success_url = reverse_lazy('patient_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        patient = self.object
        text = f'Медицинская карта для пациента {patient.full_name}, номер {patient.phone_number}'
        MedicalCard.objects.create(patient=patient, text=text)
        return response

    def get_success_url(self):
        return reverse_lazy('patient_list')

# Класс для редактирования пациента
class PatientUpdateView(UpdateView):
    model = Patient
    template_name = 'patient_update.html'
    fields = ['full_name', 'phone_number']
    success_url = reverse_lazy('patient_list')

# Класс для удаления пациента
class PatientDeleteView(DeleteView):
    model = Patient
    template_name = 'patient_delete.html'
    success_url = reverse_lazy('patient_list')


# Медицинская карта
class MedicalCardListView(ListView):
    model = MedicalCard
    template_name = 'medicalcard_list.html'
    context_object_name = 'medicalcards'
    
class MedicalCardCreateView(CreateView):
    model = MedicalCard
    template_name = 'medicalcard_create.html'
    fields = ['patient', 'text']
    success_url = reverse_lazy('medicalcard_list')

class MedicalCardUpdateView(UpdateView):
    model = MedicalCard
    template_name = 'medicalcard_update.html'
    fields = ['patient', 'text']
    success_url = reverse_lazy('medicalcard_list')

class MedicalCardDeleteView(DeleteView):
    model = MedicalCard
    template_name = 'medicalcard_confirm_delete.html'  # Может быть пустым или не использоваться
    success_url = reverse_lazy('medicalcard_list')

# Посещение
class VisitListView(ListView):
    model = Visit
    template_name = 'visit_list.html'
    context_object_name = 'visits'

class VisitCreateView(CreateView):
    model = Visit
    template_name = 'visit_create.html'
    fields = ['patient', 'doctor', 'reason', 'duration']
    success_url = reverse_lazy('visit_list')

class VisitUpdateView(UpdateView):
    model = Visit
    template_name = 'visit_update.html'
    fields = ['patient', 'doctor', 'reason', 'duration']
    success_url = reverse_lazy('visit_list')
    pk_url_kwarg = 'pk'

class VisitDeleteView(DeleteView):
    model = Visit
    template_name = 'visit_confirm_delete.html'
    success_url = reverse_lazy('visit_list')

# Медицинская запись
class MedicalRecordListView(ListView):
    model = MedicalRecord
    template_name = 'medicalrecord_list.html'
    context_object_name = 'records'

class MedicalRecordCreateView(CreateView):
    model = MedicalRecord
    template_name = 'medicalrecord_create.html'
    fields = ['visit', 'text']
    success_url = reverse_lazy('medicalrecord_list')

class MedicalRecordUpdateView(UpdateView):
    model = MedicalRecord
    template_name = 'medicalrecord_update.html'
    fields = ['visit', 'text']
    success_url = reverse_lazy('medicalrecord_list')

class MedicalRecordDeleteView(DeleteView):
    model = MedicalRecord
    template_name = 'medicalrecord_delete.html'
    success_url = reverse_lazy('medicalrecord_list')