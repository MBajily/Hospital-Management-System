from django.urls import path
from . import views

urlpatterns =[

	path('hospitals/', views.hospitals, name='hospitals'),
	path('hospital/add/', views.add_hospital, name='add_hospital'),
	path('hospital/update/<int:hospital_id>/', views.hospital_update, name='hospital_update'),
	path('hospital/deactivate/<int:hospital_id>/', views.hospital_deactive, name='hospital_deactive'),
	path('hospital/activate/<int:hospital_id>/', views.hospital_active, name='hospital_active'),

]