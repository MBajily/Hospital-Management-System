import os
import secrets
from django.shortcuts import render, redirect
from api.models import *
import datetime
from api.forms import *
from api.filters import *
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
#==================== Register =======================
#=====================================================
# @unauthenticated_user
def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			client = User.objects.get(username=request.POST["username"])
			group = Group.objects.get(name='Client')
			client.groups.add(group)
	else:
		form = RegisterForm()

	context = {'title':'ES | Sign Up','form':form}

	return render(request, 'EN/Clients/Registration/Register.html', context)
#=====================================================
#=====================================================
#=====================================================
