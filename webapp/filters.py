import django_filters
from django_filters import DateFilter, CharFilter

from api.models import *

class MedicalExaminationFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name='date', lookup_expr='gte')
	end_date = DateFilter(field_name='date', lookup_expr='lte')
	# Email = CharFilter(field_name='email', lookup_expr='icontains')
	# Full_Name = CharFilter(field_name='full_name', lookup_expr='icontains')
	
	class Meta:
		model = Medical_Examination
		fields = '__all__'
		exclude = ['date', 'id', 'patient', 'result', 'note', 'file', 'stuff', 'hospital']
