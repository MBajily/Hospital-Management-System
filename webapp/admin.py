from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Civil_Status)
admin.site.register(Patient)
admin.site.register(Kin)
admin.site.register(Hospital)
admin.site.register(Stuff)
admin.site.register(Medical_Examination)