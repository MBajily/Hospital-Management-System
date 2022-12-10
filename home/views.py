import os
import secrets
from django.shortcuts import render, redirect
from api.models import *
from ministry.forms import *
import datetime
from django.contrib.auth import get_user_model

# from .forms import *
# from .filters import *


from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib import messages

# Import pafination
from django.core.paginator import Paginator


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RegisterForm()

    context = {'title':'Sign up','form':form}

    return render(request, "home/registration.html", context)


# ------------------- Home Page -----------------------
def error_404(request, exception):
    user_logged_in = request.user

    context = {"title": "Page not found", "user_logged_in": user_logged_in}

    return render(request, "home/page-not-found.html", context)


# -----------------------------------------------------

# @login_required(login_url='login')
def login_redirect_page(request):
    user = request.user
    if user.role == 'PATIENT':
        return redirect("patient_history")

    elif user.role == 'HOSPITAL':
        return redirect("register")

    elif user.role == 'ADMIN':
        return redirect('dashboard')


# =====================================================
# =================== Home Page =======================
# =====================================================
# ------------------- Home Page -----------------------
def home(request):
    home_menu = "home"
    user_logged_in = request.user

    # patient_count = Patient.patient.all().count()
    # hospital_count = Hospital.hospital.all().count()

    # all_hospitals = HospitalProfile.objects.all()

    context = {
        "title": "Home Page",
        "user_logged_in": user_logged_in,
        # "patient_count": patient_count,
        # "all_hospitals": all_hospitals,
        "home_menu": home_menu,
        # "hospital_count": hospital_count,
    }

    return render(request, "home/home.html", context)


# -----------------------------------------------------
# =====================================================
# =====================================================
# =====================================================


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data["email"]
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "registration/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        "domain": "127.0.0.1:8000",
                        "site_name": "Website",
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "token": default_token_generator.make_token(user),
                        "protocol": "http",
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(
                            subject,
                            email,
                            "admin@example.com",
                            [user.email],
                            fail_silently=False,
                        )
                    except BadHeaderError:

                        return HttpResponse("Invalid header found.")

                    messages.success(
                        request,
                        "A message with reset password instructions has been sent to your inbox.",
                    )
                    return redirect("password_reset_done")
    password_reset_form = PasswordResetForm()
    return render(
        request=request,
        template_name="registration/password_reset.html",
        context={"password_reset_form": password_reset_form},
    )