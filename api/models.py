from django.db import models
import datetime
from Seha.settings import MEDIA_ROOT, MEDIA_URL
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.utils import timezone
import random
import secrets
import uuid

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
	nationality_id = models.CharField(primary_key=True, max_length=20, unique=True)
	full_name = models.CharField(max_length=200, null=True)
	birth = models.DateField()
	gender = models.CharField(max_length=200, null=True, choices=Genders)

	@property
	def age(self):
		if self.birth is None:
			self.birth = datetime.datetime.now().date()
		return int((datetime.datetime.now().date() - self.birth).days / 365.25)
	def __str__(self):
		return self.full_name



#===============================================================
#========================  Patients  ===========================
#===============================================================
class Patient(models.Model):
	id = models.AutoField(primary_key=True)
	civil_status = models.ForeignKey(Civil_Status, null=True, on_delete=models.SET_NULL)
	phone = models.CharField(max_length=20)
	email = models.EmailField(max_length=200, null=True)
	date = models.DateField(auto_now_add=True, blank=True)

	# def __str__(self):
	# 	return self.civil_status.nationality_id



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
	email = models.EmailField(max_length=200, unique=True, null=True)
	patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
	relationship = models.CharField(max_length=200, choices=Relationships)

	def __str__(self):
		return "{} for {}".format(self.full_name)



#===============================================================
#========================  Hospital  ===========================
#===============================================================
class Hospital(models.Model):
	hospital_id = models.IntegerField(primary_key=True, editable=False)
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=200, unique=True)
	logo = models.ImageField(null=True, blank=True)
	# username = models.CharField(max_length=50, unique=True)
	password = models.UUIDField(max_length=9, default=uuid.uuid4)
	active = models.BooleanField(null=False, default=True)
	date = models.DateField(auto_now_add=True, blank=True)

	def __str__(self):
		return self.name



#===============================================================
#====================  Hospital's Stuff  =======================
#===============================================================
class Stuff(models.Model):
	id = models.IntegerField(primary_key=True, default=random.randint(10000000000,90000000000), editable=False)
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=200, unique=True)
	hospital = models.ForeignKey(Hospital, null=True, on_delete=models.SET_NULL)
	role = models.CharField(max_length=100, null=True)
	# username = models.CharField(max_length=50, unique=True)
	password = models.UUIDField(max_length=9, default=uuid.uuid4)
	

	def __str__(self):
		return self.name



#===============================================================
#=================  Medical Examinations  ======================
#===============================================================
class Medical_Examination(models.Model):

	Types = (
		("Biopsy","Biopsy"),
		("Colonoscopy","Colonoscopy"),
		("CT scan","CT scan"),
		("CT scans and radiation exposure in children and young people","CT scans and radiation exposure in children and young people"),
		("Electrocardiogram (ECG)","Electrocardiogram (ECG)"),
		("Electroencephalogram (EEG)","Electroencephalogram (EEG)"),
		("Gastroscopy","Gastroscopy"),
		("Eye tests","Eye tests"),
		("Hearing test","Hearing test"),
		("MRI scan","MRI scan"),
		("PET scan","PET scan"),
		("Ultrasound","Ultrasound"),
		("X-rays","X-rays"),
		)

	id = models.AutoField(primary_key=True)
	patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
	type = models.CharField(max_length=200, choices=Types)
	report = models.CharField(max_length=1000, null=True, blank=True)
	date = models.DateField(auto_now_add=True, null=True)
	result = models.FileField()
	# stuff = models.ForeignKey(Stuff, null=True, on_delete=models.SET_NULL)
	hospital = models.ForeignKey(Hospital, null=True, on_delete=models.SET_NULL)


	def __str__(self):
		return self.patient.civil_status.full_name


#===============================================================
#=================  Basic Health State  ======================
#===============================================================
class Basic_Health_State(models.Model):

	Types = (
		("Heart Rate","Heart Rate"),
		("Oxygen Saturation","Oxygen Saturation"),
		("Body Temperature","Body Temperature"),
		("Glucose Level","Glucose Level"),
		)

	id = models.AutoField(primary_key=True)
	patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
	heart_rate = models.IntegerField(null=False, default=0)
	oxygen_saturation = models.IntegerField(null=False, default=0)
	body_temperature = models.IntegerField(null=False, default=0)
	glucose_level = models.IntegerField(null=False, default=0)
	date = models.DateTimeField(auto_now_add=True)
	# stuff = models.ForeignKey(Stuff, null=True, on_delete=models.SET_NULL)
	hospital = models.ForeignKey(Hospital, null=True, on_delete=models.SET_NULL)


	def __str__(self):
		return self.patient.civil_status.full_name


#===============================================================
#=================  Basic Health State  ======================
#===============================================================
class Prescription(models.Model):

	Types = (
		("Heart Disease","Heart Disease"),
		("Skin Care","Skin Care"),
		("Diabetes Disease","Diabetes Disease"),
		)

	id = models.AutoField(primary_key=True)
	patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
	name = models.TextField(null=False)
	type = models.CharField(max_length=200, choices=Types)
	start_date = models.DateField()
	end_date = models.DateField()
	date = models.DateTimeField(auto_now_add=True)
	note = models.CharField(max_length=1000, null=True, blank=True)
	# stuff = models.ForeignKey(Stuff, null=True, on_delete=models.SET_NULL)
	hospital = models.ForeignKey(Hospital, null=True, on_delete=models.SET_NULL)

	@property
	def duration(self):
		if self.end_date is None:
			return None
		return int((self.end_date - self.start_date).days)

	def __str__(self):
		return self.patient.civil_status.full_name