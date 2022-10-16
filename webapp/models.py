from django.db import models
import datetime
# from ES.settings import MEDIA_ROOT, MEDIA_URL
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


#===============================================================
#=====================  Civil Status  ==========================
#===============================================================
class Civil_Status(models.Model):
	Genders = (
		('Male', 'Male - ذكر'),
		('Female', 'Female - أنثى')
	)
	Nationality = (
		('Sudanese', 'Sudanese - سوداني'),
		('Non-sudanese', 'Non-sudanese - غير سوداني')
	)

	nationality_id = models.AutoField(primary_key=True)
	full_name = models.CharField(max_length=200, null=True)
	birth = models.DateField()
	gender = models.CharField(max_length=200, null=True, choices=Genders)
	nationality = models.CharField(max_length=200, null=True, choices=Nationality)

	def __str__(self):
		return self.full_name



#===============================================================
#========================  Patients  ===========================
#===============================================================
class Patient(models.Model):
	id = models.AutoField(primary_key=True)
	nationality_id = models.ForeignKey(Civil_Status, null=True, on_delete=models.SET_NULL)
	phone = models.CharField(max_length=20)
	email = models.EmailField(max_length=200, null=True)

	def __str__(self):
		return self.nationality_id



#===============================================================
#=====================  Kin of patient  ========================
#===============================================================
class Kin(models.Model):
	Relationships = (
		('Father', 'Father'),
		('Mother', 'Mother'),
		('Husband', 'Husband'),
		('Wife', 'Wife'),
		('Son', 'Son'),
		('Daughter', 'Dauther'),
		('Brother', 'Father'),
		('Sister', 'Sister'),
		('Uncle', 'Uncle'),
		('aunt', 'aunt'),
		('Grandfather', 'Grandfather'),
		('grandmother', 'grandmother'),
		('Step Father', 'Step Father'),
		('Step Mother', 'Step Mother'),
		)
	id = models.AutoField(primary_key=True)
	full_name = models.CharField(max_length=200)
	address = models.CharField(max_length=1000, null=True)
	phone = models.CharField(max_length=20)
	patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
	relationship = models.CharField(max_length=200, choices=Relationships)

	def __str__(self):
		return "{} for {}".format(self.full_name)



#===============================================================
#========================  Hospital  ===========================
#===============================================================
class Hospital(models.Model):
	hospital_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=200, unique=True)
	username = models.CharField(max_length=50, unique=True)
	logo = models.ImageField(null=True, blank=True)
	password = models.CharField(max_length=100)

	def __str__(self):
		return self.name



#===============================================================
#========================  Hospital's Stuff  ===========================
#===============================================================
class Stuff(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=200, unique=True)
	username = models.CharField(max_length=50, unique=True)
	role = models.CharField(max_length=100, null=True)
	password = models.CharField(max_length=100)
	hospital = models.ForeignKey(Hospital, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.name