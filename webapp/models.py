from django.db import models
import datetime
# from ES.settings import MEDIA_ROOT, MEDIA_URL
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


#===============================================================
#========================  Civil_Status  =============================
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


