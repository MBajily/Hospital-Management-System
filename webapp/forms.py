from django import forms 
from api.models import *

from django.forms import inlineformset_factory
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#=====================================================
#===================== Kin Form ======================
#=====================================================
class CivilStatusForm(forms.ModelForm):
	class Meta:
		model = Civil_Status
		fields = ['nationality_id', 'full_name', 'birth', 'gender']
		widgets = {
			'nationality_id': forms.TextInput(attrs={'name':'nationality_id', 'class': 'form-control', 'id': 'inputName', 'required': 'True', 'disabled': 'True'}),
			'full_name': forms.Textarea(attrs={'name':'full_name', 'class': 'form-control', 'id': 'inputName', 'placeholder': 'Cina Saffary', 'required': 'True', 'disabled': 'True'}),
			'birth': forms.TextInput(attrs={'name':'birth', 'class': 'form-control', 'id': 'inputName', 'required': 'True', 'disabled': 'True'}),
			'gender': forms.TextInput(attrs={'name':'gender', 'class': 'form-control', 'id': 'inputName', 'required': 'True', 'disabled': 'True'}),
		}


#=====================================================
#=================== Patient Form ====================
#=====================================================
class PatientForm(forms.ModelForm):
	class Meta:
		model = Patient
		fields = ['phone', 'email']
		widgets = {
			'phone': forms.TextInput(attrs={'name':'phone', 'class': 'form-control', 'id': 'inputName', 'required': 'True'}),
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
		fields = ['type', 'report', 'result']
		widgets = {
			'type': forms.Select(attrs={'name':'type', 'class': "form-select form-select-lg mb-3", 'required': 'True'}),
			# 'result': forms.Textarea(attrs={'class': 'form-control', 'id': 'inputName', 'placeholder': 'Cina Saffary', 'required': 'True'}),
			'report': forms.Textarea(attrs={'class': 'form-control', 'id': 'inputName', 'placeholder': 'Cina Saffary', 'required': 'False'}),
			# 'date': forms.DateInput(attrs={'name':'date', 'class':"form-control", 'placeholder':"yyyy-mm-dd", 'id':"datepicker", 'required':"True", 'data-date-format':"yyyy-mm-dd"}),
			'result': forms.FileInput(attrs={'name':'file', 'id':"input-file-to-destroy", 'class':"dropify", 'data-allowed-formats':"portrait square", 'data-max-file-size':"2M", 'data-max-height':"2000", 'required':'True'})
		}		


#=====================================================
#============ Basic Health State Form ===============
#=====================================================
class BasicHealthStateForm(forms.ModelForm):
	class Meta:
		model = Basic_Health_State
		fields = ['heart_rate', 'oxygen_saturation', 'body_temperature', 'glucose_level']
		widgets = {
			'type': forms.Select(attrs={'name':'type', 'class': "form-select form-select-lg mb-3", 'required': 'True'}),
			'heart_rate': forms.TextInput(attrs={'name':'heart_rate', 'class': 'form-control', 'id': 'inputName', 'placeholder': 'Cina Saffary', 'required': 'False'}),
			'oxygen_saturation': forms.TextInput(attrs={'name':'oxygen_saturation', 'class': 'form-control', 'id': 'inputName', 'placeholder': 'Cina Saffary', 'required': 'False'}),
			'body_temperature': forms.TextInput(attrs={'name':'body_temperature', 'class': 'form-control', 'id': 'inputName', 'placeholder': 'Cina Saffary', 'required': 'False'}),
			'glucose_level': forms.TextInput(attrs={'name':'glucose_level', 'class': 'form-control', 'id': 'inputName', 'placeholder': 'Cina Saffary', 'required': 'False'}),
			# 'date': forms.DateInput(attrs={'name':'date', 'class':"form-control", 'placeholder':"yyyy-mm-dd", 'id':"datepicker", 'required':"True", 'data-date-format':"yyyy-mm-dd"}),
		}		