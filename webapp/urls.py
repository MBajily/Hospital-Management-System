from django.urls import path
from . import views

urlpatterns =[
	path('dashboard/', views.dashboard, name='dashboard'),

	path('hospitals/', views.hospitals, name='hospitals'),
	path('hospitals/add/', views.add_hospital, name='add_hospital'),
	path('hospitals/update/<int:hospital_id>/', views.hospital_update, name='hospital_update'),
	path('hospitals/deactivate/<int:hospital_id>/', views.hospital_deactive, name='hospital_deactive'),
	path('hospitals/activate/<int:hospital_id>/', views.hospital_active, name='hospital_active'),

	path('patients/', views.patients, name='patients'),
	path('patients/<int:patient_id>/delete/', views.patient_delete, name='patient_delete'),
	path('patients/add/<int:nationality_id>/', views.add_patient, name='add_patient'),
	path('patients/add/check/', views.check_nationality_id, name='check_nationality_id'),
	path('patients/<int:nationality_id>/update/', views.patient_update, name='patient_update'),


	path('data/patients/json/', views.patients_chart, name='patients_chart'),
	path('data/medical_examinations/json/', views.medical_examinations_chart, name='medical_examinations_chart'),


]