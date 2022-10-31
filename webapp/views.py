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
#===================== Hospital =========================
#=====================================================
#-------------------- Hospitals -------------------------
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

	context = {'title':'New Admin', 'form':form,
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