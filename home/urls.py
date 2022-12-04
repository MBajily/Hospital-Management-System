from django.urls import path
from . import views

urlpatterns = [
	path("", views.home, name="home"),
	path("home/", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/redirect/", views.login_redirect_page, name="login_redirect_page"),
    # path("patient/login/", views.patient_login, name="patient_login"),
    # path("hospital/login/", views.hospital_login, name="hospital_login"),
    # path("ministry/login/", views.ministry_login, name="ministry_login"),
]
