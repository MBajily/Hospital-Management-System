from django import forms 
from api.models import *

from django.forms import inlineformset_factory
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#=====================================================
#=================== Patient Form ====================
#=====================================================
class PatientForm(forms.ModelForm):
	class Meta:
		model = Patient
		fields = ['nationality_id', 'phone', 'email']
		widgets = {
			'nationality_id': forms.TextInput(attrs={'name':'first_name', 'class': 'form-control', 'id': 'inputName', 'required': 'True'}),
			'phone': forms.TextInput(attrs={'name':'last_name', 'class': 'form-control', 'id': 'inputName', 'required': 'True'}),
			'email': forms.EmailInput(attrs={'name':'email', 'class':"form-control", 'id':"inputEmail", 'placeholder':"Email", 'data-error':"Bruh, that email address is invalid", 'required':'True'}),
		}


#=====================================================
#===================== Kin Form ======================
#=====================================================
class KinForm(forms.ModelForm):
	class Meta:
		model = Kin
		fields = ['full_name', 'address', 'relationship', 'phone', 'email']
		widgets = {
			'full_name': forms.TextInput(attrs={'name':'first_name', 'class': 'form-control', 'id': 'inputName', 'required': 'True'}),
			'address': forms.Textarea(attrs={'class': 'form-control', 'id': 'inputName', 'placeholder': 'Cina Saffary', 'required': 'True'}),
			'relationship': forms.Select(attrs={'name':'relationship', 'class': "form-select form-select-lg mb-3", 'required': 'True'}),
			'phone': forms.TextInput(attrs={'name':'last_name', 'class': 'form-control', 'id': 'inputName', 'required': 'True'}),
			'email': forms.EmailInput(attrs={'name':'email', 'class':"form-control", 'id':"inputEmail", 'placeholder':"Email", 'data-error':"Bruh, that email address is invalid", 'required':'True'}),
		}


#=====================================================
#================== Hospital Form ====================
#=====================================================
class HospitalForm(forms.ModelForm):
	class Meta:
		model = Hospital
		fields = ['name', 'email', 'logo']
		widgets = {
			'name': forms.TextInput(attrs={'name':'name', 'class': 'form-control', 'id': 'inputName', 'required': 'True'}),
			'email': forms.EmailInput(attrs={'name':'email', 'class':"form-control", 'id':"inputEmail", 'placeholder':"Email", 'data-error':"Bruh, that email address is invalid", 'required':'True'}),
			'logo': forms.FileInput(attrs={'name':'logo', 'id':"input-file-to-destroy", 'class':"dropify", 'data-allowed-formats':"portrait square", 'data-max-file-size':"2M", 'data-max-height':"2000", 'required':'True'})
			# 'username': forms.TextInput(attrs={'name':'username', 'type':"text", 'class': "form-control", 'id': "validationCustom08", 'placeholder':"Primary Number", 'oninput':"check(this)", 'required':'True'}),
			# 'password': forms.TextInput(attrs={'name':'password', 'type':"password", 'class': "form-control", 'id': "validationCustom08", 'placeholder':"Primary Number", 'oninput':"check(this)", 'required':'True'}),
		}


#=====================================================
#==================== Stuff Form =====================
#=====================================================
class StuffForm(forms.ModelForm):
	class Meta:
		model = Stuff
		fields = ['name', 'email', 'role', 'password']
		widgets = {
			'name': forms.TextInput(attrs={'name':'name', 'class': 'form-control', 'id': 'inputName', 'required': 'True'}),
			'email': forms.EmailInput(attrs={'name':'email', 'class':"form-control", 'id':"inputEmail", 'placeholder':"Email", 'data-error':"Bruh, that email address is invalid", 'required':'True'}),
			'role': forms.TextInput(attrs={'name':'role', 'class': 'form-control', 'id': 'inputName', 'required': 'True'}),
			# 'username': forms.TextInput(attrs={'name':'username', 'type':"text", 'class': "form-control", 'id': "validationCustom08", 'placeholder':"Primary Number", 'oninput':"check(this)", 'required':'True'}),
			'password': forms.TextInput(attrs={'name':'password', 'type':"password", 'class': "form-control", 'id': "validationCustom08", 'placeholder':"Primary Number", 'oninput':"check(this)", 'required':'True'}),
		}


#=====================================================
#============ Medical Examination Form ===============
#=====================================================
class MedicalExaminationForm(forms.ModelForm):
	class Meta:
		model = Medical_Examination
		fields = ['type', 'result', 'note', 'file']
		widgets = {
			'type': forms.Select(attrs={'name':'type', 'class': "form-select form-select-lg mb-3", 'required': 'True'}),
			'result': forms.Textarea(attrs={'class': 'form-control', 'id': 'inputName', 'placeholder': 'Cina Saffary', 'required': 'True'}),
			'note': forms.Textarea(attrs={'class': 'form-control', 'id': 'inputName', 'placeholder': 'Cina Saffary', 'required': 'True'}),
			# 'date': forms.DateInput(attrs={'name':'date', 'class':"form-control", 'placeholder':"yyyy-mm-dd", 'id':"datepicker", 'required':"True", 'data-date-format':"yyyy-mm-dd"}),
			'file': forms.FileInput(attrs={'name':'file', 'id':"input-file-to-destroy", 'class':"dropify", 'data-allowed-formats':"portrait square", 'data-max-file-size':"2M", 'data-max-height':"2000", 'required':'True'})
		}		