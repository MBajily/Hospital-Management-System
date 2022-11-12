import os
import secrets
from django.shortcuts import render, redirect
from api.models import *
import datetime
from .forms import *
from .filters import *
# from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponse, JsonResponse


import csv
#================ Export As PDF ======================
# from io import BytesIO
# from django.http import HttpResponse
# from django.template.loader import get_template
# from django.views import View
# from xhtml2pdf import pisa
#=====================================================


#=====================================================



#=====================================================
#=================== Dashboard =======================
#=====================================================
#------------------- Dashboard -----------------------
@login_required(login_url='login')
def dashboard(request):
	main_menu = 'dashboard'
	sub_menu = ''

	hospitals_count = Hospital.objects.all().count()
	patients_count = Patient.objects.all().count()
	medical_examinations_count = Medical_Examination.objects.all().count()
	recent_hospitals = Hospital.objects.filter(active=1).order_by('-date')[:5]
	recent_patients = Patient.objects.order_by('-date')[:5]

	context = {'title':'Dashboard', 'main_menu':main_menu, 
			   'sub_menu':sub_menu, 'hospitals_count':hospitals_count,
			   'patients_count':patients_count, 'medical_examinations_count':medical_examinations_count,
			   'recent_hospitals':recent_hospitals, 'recent_patients':recent_patients}
	
	return render(request, 'ministry/dashboard/dashboard.html', context)
#-----------------------------------------------------
#=====================================================
#=====================================================
#=====================================================


#=====================================================
#================ Medical History ====================
#=====================================================
#---------------- Medical History --------------------
@login_required(login_url='login')
def medical_history(request, nationality_id):
	main_menu = 'patinets'
	sub_menu = 'all_patients'

	civil_status = Civil_Status.objects.get(nationality_id=nationality_id)
	selected_patient = Patient.objects.filter(civil_status=civil_status).first()
	medical_examinations = Medical_Examination.objects.filter(patient=selected_patient).order_by('-date')
	medical_examinations_filter = MedicalExaminationFilter(request.GET, queryset=medical_examinations)
	medical_examinations = medical_examinations_filter.qs.order_by('-date')
	recent_health_state = Basic_Health_State.objects.filter(patient=selected_patient).order_by('-date').first()


	context = {'title':'Medical History', 'main_menu':main_menu, 
			   'sub_menu':sub_menu, 'selected_patient':selected_patient,
			   'medical_examinations':medical_examinations, 
			   'medical_examinations_filter':medical_examinations_filter,
			   'recent_health_state':recent_health_state}
	
	return render(request, 'ministry/medical_history/medical_history.html', context)
#-----------------------------------------------------
#=====================================================
#=====================================================
#=====================================================



#=====================================================
#==================== Hospital =======================
#=====================================================
#------------------- Hospitals -----------------------
@login_required(login_url='login')
def hospitals(request):
	main_menu = 'hospitals'
	sub_menu = 'all_hospitals'

	all_hospitals = Hospital.objects.all()
	all_hospitals = set(all_hospitals)

	context = {'title':'Hospitals', 'all_hospitals':all_hospitals, 
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'ministry/hospitals/hospitals.html', context)
#-----------------------------------------------------


#-------------------- Add Hospital -------------------------
@login_required(login_url='login')
def add_hospital(request):
	main_menu = 'hospitals'
	sub_menu = 'add_hospital'
	# groups = Group.objects.order_by('name').all()
	if request.method == 'POST':
		if request.user.check_password(request.POST["admin_password"]):
			form = HospitalForm(request.POST)
			if form.is_valid():
				form.save()
				return redirect('hospitals')
		else:
			return redirect('add_hospital')
	else:
		form = HospitalForm()

	context = {'title':'New Hospital', 'form':form,
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'ministry/hospitals/add_hospital.html', context)
#-----------------------------------------------------

#------------------- Update Hospital -------------------
@login_required(login_url='login')
def hospital_update(request, hospital_id):
	main_menu = 'hospitals'
	sub_menu = 'all_hospitals'
	
	selected_hospital = Hospital.objects.get(hospital_id=hospital_id)
	formset = HospitalForm(instance=selected_hospital)
	if request.method == 'POST':
		if request.user.check_password(request.POST["admin_password"]):
			name = request.POST['name']
			email = request.POST['email']
			logo = request.FILES['logo']
			
			selected_hospital = Hospital(name=name, hospital_id=selected_hospital.hospital_id, 
										logo=logo, email=email)
			if selected_hospital:
				selected_hospital.save()
				return redirect('hospitals')
		else:
			return redirect('hospital_update', selected_hospital.hospital_id)

	context = {'title': selected_hospital.name, 'sub_menu':sub_menu,
				'formset':formset, 'main_menu':main_menu,
				'selected_hospital':selected_hospital}

	return render(request, 'ministry/hospitals/hospital_update.html', context)
#-----------------------------------------------------


#----------------- Deactive Hospital -----------------
@login_required(login_url='login')
def hospital_deactive(request, hospital_id):
	main_menu = 'hospitals'
	sub_menu = 'all_hospitals'

	selected_hospital = Hospital.objects.get(hospital_id=hospital_id)
	
	if request.method == 'POST':
		if request.user.check_password(request.POST["admin_password"]):
			selected_hospital.active = False
			selected_hospital.save()
			return redirect('hospitals')
		else:
			return redirect('hospital_deactive', hospital_id)

	context = {'title':'Deactive Hospital', 'item':selected_hospital,
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'ministry/hospitals/hospital_deactive.html', context)
#-----------------------------------------------------


#----------------- Active Hospital -----------------
@login_required(login_url='login')
def hospital_active(request, hospital_id):
	main_menu = 'hospitals'
	sub_menu = 'all_hospitals'

	selected_hospital = Hospital.objects.get(hospital_id=hospital_id)
	
	if request.method == 'POST':
		if request.user.check_password(request.POST["admin_password"]):
			selected_hospital.active = True
			selected_hospital.save()
			return redirect('hospitals')
		else:
			return redirect('hospital_active', hospital_id)

	context = {'title':'Active Hospital', 'item':selected_hospital,
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'ministry/hospitals/hospital_active.html', context)
#-----------------------------------------------------



#=====================================================
#==================== patient ========================
#=====================================================
#------------------- patients ------------------------
@login_required(login_url='login')
def patients(request):
	main_menu = 'patients'
	sub_menu = 'all_patients'

	all_patients = Patient.objects.all()
	all_patients = set(all_patients)

	context = {'title':'Patients', 'all_patients':all_patients, 
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'ministry/patients/patients.html', context)
#-----------------------------------------------------

#----------------- Delete patient -----------------
@login_required(login_url='login')
def patient_delete(request, patient_id):
	main_menu = 'patients'
	sub_menu = 'all_patients'

	selected_civil_status = Civil_Status.objects.get(nationality_id=patient_id)
	selected_patient = Patient.objects.get(civil_status=selected_civil_status)
	
	if request.method == 'POST':
		if request.user.check_password(request.POST["admin_password"]):
			selected_patient.delete()
			return redirect('patients')
		else:
			return redirect('patient_delete', patient_id)

	context = {'title':'Delete Patient', 'item':selected_patient,
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'ministry/patients/patient_delete.html', context)
#-----------------------------------------------------


#-------------- Nationality ID Check -----------------
@login_required(login_url='login')
def check_nationality_id(request):
	main_menu = 'patients'
	sub_menu = 'add_patient'
	# groups = Group.objects.order_by('name').all()
	if request.method == 'POST':
		civil_status = Civil_Status.objects.filter(nationality_id=request.POST["nationality_id"]).first()
		if (civil_status is not None):
			if not(Patient.objects.filter(civil_status=civil_status)):
				return redirect('add_patient', civil_status.nationality_id)

	context = {'title':'Check Nationality ID',
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'ministry/patients/check_nationality_id.html', context)
#-----------------------------------------------------


#-------------------- Add patient -------------------------
@login_required(login_url='login')
def add_patient(request, nationality_id):
	main_menu = 'patients'
	sub_menu = 'add_patient'
	# groups = Group.objects.order_by('name').all()
	formset = CivilStatusForm(instance=Civil_Status.objects.get(nationality_id=nationality_id))
	if request.method == 'POST':
		civil_status = Civil_Status.objects.get(nationality_id=nationality_id)
		if (civil_status is not None):
			if not(Patient.objects.filter(civil_status=civil_status)):
				if request.user.check_password(request.POST["admin_password"]):
					added_patient = Patient(email=request.POST["email"], phone=request.POST["phone"])
					if added_patient:
						added_patient.civil_status = civil_status
						added_patient.save()
						return redirect('patients')
				else:
					return redirect('add_patient', nationality_id)
	else:
		form = PatientForm()

	context = {'title':'New Patient', 'form':form, 'formset':formset,
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'ministry/patients/add_patient.html', context)
#-----------------------------------------------------


#------------------- Update patient -------------------
@login_required(login_url='login')
def patient_update(request, nationality_id):
	main_menu = 'patients'
	sub_menu = 'all_patients'
	
	civil_status = Civil_Status.objects.get(nationality_id=nationality_id)
	selected_patient = Patient.objects.get(civil_status=civil_status)
	formset = PatientForm(instance=selected_patient)
	if request.method == 'POST':
		if request.user.check_password(request.POST["admin_password"]):
			phone = request.POST['phone']
			email = request.POST['email']
			
			selected_patient.email = email
			selected_patient.phone = phone
			if selected_patient:
				selected_patient.save()
				return redirect('patients')
		else:
			return redirect('patient_update', selected_patient.patient_id)

	context = {'title': selected_patient.civil_status.full_name, 'sub_menu':sub_menu,
				'formset':formset, 'main_menu':main_menu,
				'selected_patient':selected_patient, 'civil_status':civil_status}

	return render(request, 'ministry/patients/patient_update.html', context)
#-----------------------------------------------------



#=====================================================
#===================== Charts ========================
#=====================================================
#----------------- Patients Chart --------------------
@login_required(login_url='login')
def patients_chart(request):
	data = []

	for d in (datetime.date.today() - datetime.timedelta(days=x) for x in reversed(range(0,30))):
		patients_count = Patient.objects.filter(date=d.strftime("%Y-%m-%d")).all().count()
		if patients_count:
			data.append({'{}'.format(d.strftime("%b, %d")): patients_count})
		else:
			data.append({'{}'.format(d.strftime("%b, %d")): 0})
	
	return JsonResponse(data, safe=False)
#-----------------------------------------------------


#----------- Medical Examinations Chart --------------
@login_required(login_url='login')
def medical_examinations_chart(request):
	data = []

	for d in (datetime.date.today() - datetime.timedelta(days=x) for x in reversed(range(0,30))):
		medical_examinations_count = Medical_Examination.objects.filter(date=d.strftime("%Y-%m-%d")).all().count()
		if medical_examinations_count:
			data.append({'{}'.format(d.strftime("%b, %d")): medical_examinations_count})
		else:
			data.append({'{}'.format(d.strftime("%b, %d")): 0})
	
	return JsonResponse(data, safe=False)
#-----------------------------------------------------



#=====================================================
#============== Basic Health State ===================
#=====================================================

#--------------- Add Health State --------------------
@login_required(login_url='login')
def update_health_state(request, nationality_id):
	main_menu = 'patients'
	sub_menu = 'all_patients'

	civil_status = Civil_Status.objects.get(nationality_id=nationality_id)
	selected_patient = Patient.objects.get(civil_status=civil_status)

	if request.method == 'POST':
		heart_rate = request.POST['heart_rate']
		oxygen_saturation = request.POST['oxygen_saturation']
		body_temperature = request.POST['body_temperature']
		glucose_level = request.POST['glucose_level']
		health_state = Basic_Health_State(patient=selected_patient, heart_rate=heart_rate,
										  oxygen_saturation=oxygen_saturation, body_temperature=body_temperature,
										  glucose_level=glucose_level)
		if health_state:
			health_state.save()
			return redirect('medical_history', nationality_id)
	else:
		health_state = Basic_Health_State.objects.filter(patient=selected_patient).order_by('-date').first()
		form = BasicHealthStateForm(instance=health_state)

	context = {'title':'Update Basic Health State', 'form':form,
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'ministry/medical_history/basic_health_state.html', context)
#-----------------------------------------------------


#=====================================================
#=================== Prescription ====================
#=====================================================

#----------------- Add Prescription ------------------
@login_required(login_url='login')
def add_prescription(request, nationality_id):
	main_menu = 'patients'
	sub_menu = 'all_patients'

	civil_status = Civil_Status.objects.get(nationality_id=nationality_id)
	selected_patient = Patient.objects.get(civil_status=civil_status)

	if request.method == 'POST':
		start_date = request.POST['start_date']
		end_date = request.POST['end_date']
		type = request.POST['type']
		name = request.POST['name']
		note = request.POST['note']
		prescription = Prescription(patient=selected_patient, start_date=start_date,
									end_date=end_date, type=type,
									name=name, note=note)
		if prescription:
			prescription.save()
			return redirect('medical_history', nationality_id)
	else:
		form = PrescriptionForm()

	context = {'title':'Add Prescription', 'form':form,
			   'main_menu':main_menu, 'sub_menu':sub_menu}

	return render(request, 'ministry/medical_history/add_prescription.html', context)
#-----------------------------------------------------