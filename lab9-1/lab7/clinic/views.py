
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import RegistrationForm
from .models import Doctor, Patient, MedicalCard, Visit, MedicalRecord

from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.auth import login as user_login


def is_doc(user):
    return user.groups.filter(name='Врачи').exists()
# Врачи

class DoctorListView(ListView):
    model = Doctor
    context_object_name = 'doctors'
    if is_doc:
        template_name = 'doctor_list.html'
    else:
        template_name = 'exp.html'

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


# Пациенты
class PatientListView(ListView):
    model = Patient
    context_object_name = 'patients'
    if not(is_doc):
        template_name = 'doctor_list.html'
    else:
        template_name = 'exp.html'


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
    if not(is_doc):
        template_name = 'medicalcard_list.html'
    else:
        template_name = 'exp.html'


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
    if not(is_doc):
        template_name = 'medicalrecord_list.html'
    else:
        template_name = 'exp.html'


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


def exp(request):
    return render(request, 'exp.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']

            # Создание пользователя
            user = User.objects.create_user(username=username, email=email, password=password)

            # Назначение пользователя в соответствующую группу
            if role == 'patient':
                group = Group.objects.get(name='Пациенты')
            else:
                group = Group.objects.get(name='Врачи')
            user.groups.add(group)

            # Вход пользователя после успешной регистрации
            user_login(request, user)

            return redirect('visit_list')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            user_login(request, user)
            return redirect('visit_list')
        else:
            return render(request, 'login.html', {'error_message': 'Неправильное имя пользователя или пароль.'})
    return render(request, 'login.html')
