from django.urls import path
from . import views

urlpatterns =[
	path('dashboard/', views.dashboard, name='dashboard'),


	path('hospitals/', views.hospitals, name='hospitals'),
	path('hospitals/new/', views.add_hospital, name='add_hospital'),
	path('hospitals/<int:hospital_id>/update/', views.hospital_update, name='hospital_update'),
	path('hospitals/<int:hospital_id>/deactivate/', views.hospital_deactive, name='hospital_deactive'),
	path('hospitals/<int:hospital_id>/activate/', views.hospital_active, name='hospital_active'),


	path('patients/', views.patients, name='patients'),
	path('patients/<int:patient_id>/delete/', views.patient_delete, name='patient_delete'),
	path('patients/new/<int:nationality_id>/', views.add_patient, name='add_patient'),
	path('patients/new/check/', views.check_nationality_id, name='check_nationality_id'),
	path('patients/<int:nationality_id>/update/', views.patient_update, name='patient_update'),
	path('patients/<int:nationality_id>/medical_history/', views.medical_history, name='medical_history'),
	path('patients/<int:nationality_id>/health_state/update/', views.update_health_state, name='update_health_state'),
	path('patients/<int:nationality_id>/prescriptions/new/', views.add_prescription, name='add_prescription'),


	path('data/patients/json/', views.patients_chart, name='patients_chart'),
	path('data/medical_examinations/json/', views.medical_examinations_chart, name='medical_examinations_chart'),


]