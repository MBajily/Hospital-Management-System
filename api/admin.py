from django.contrib import admin

# Register your models here.

from .models import *


class CivilStatusAdmin(admin.ModelAdmin):
	list_display = ['nationality_id', 'full_name', 'birth', 'gender']
	search_fields = ['nationality_id']


admin.site.register(Civil_Status, CivilStatusAdmin)
admin.site.register(Patient)
admin.site.register(Kin)
admin.site.register(Hospital)
admin.site.register(Stuff)
admin.site.register(Medical_Examination)