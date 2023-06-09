from django.db import models
from django.contrib.auth.models import Group

group_name = 'Пациенты'
if not Group.objects.filter(name=group_name).exists():
    group_buyers = Group.objects.create(name=group_name)


group_name = 'Врачи'
if not Group.objects.filter(name=group_name).exists():
    group_managers = Group.objects.create(name=group_name)

class Patient(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    preferred_doctors = models.ManyToManyField('Doctor', through='PreferredDoctor', related_name='preferred_patients')

class Doctor(models.Model):
    full_name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    room_number = models.CharField(max_length=10)

class Visit(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    reason = models.CharField(max_length=255)
    duration = models.IntegerField()

class MedicalRecord(models.Model):
    visit = models.OneToOneField(Visit, on_delete=models.CASCADE)
    text = models.TextField()

class MedicalCard(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    text = models.TextField()

class PreferredDoctor(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)