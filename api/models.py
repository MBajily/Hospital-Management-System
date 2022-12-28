from django.db import models
import datetime
from Seha.settings import MEDIA_ROOT, MEDIA_URL
from django import forms
from django.contrib.auth.models import User, Group, Permission, AbstractUser, BaseUserManager
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone
import random
import secrets
import uuid

#===============================================================
#=====================  Civil Status  ==========================
#===============================================================
class Civil_Status(models.Model):
	Genders = (
		('Male', 'Male - ذكر'),
		('Female', 'Female - أنثى')
	)
	Nationality = (
		('Sudanese', 'Sudanese - سوداني'),
		('Non-sudanese', 'Non-sudanese - غير سوداني')
	)
	nationality_id = models.CharField(primary_key=True, max_length=20, unique=True)
	full_name = models.CharField(max_length=200, null=True)
	birth = models.DateField()
	gender = models.CharField(max_length=200, null=True, choices=Genders)

	@property
	def age(self):
		if self.birth is None:
			self.birth = datetime.datetime.now().date()
		return int((datetime.datetime.now().date() - self.birth).days / 365.25)
	def __str__(self):
		return self.full_name


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        HOSPITAL = "HOSPITAL", "Hospital"
        PATIENT = "PATIENT", "Patient"

    base_role = Role.PATIENT

    username = None 
    last_login = None 
    first_name = None 
    last_name = None 
    is_staff = None 
    is_superuser = None 
    groups_id = None 
    user_permissions_id = None 
    email = models.EmailField(unique=True)
    is_deleted = models.BooleanField(null=False, default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # civil_status = models.ForeignKey(Civil_Status, null=True, on_delete=models.SET_NULL)
    role = models.CharField(max_length=50, choices=Role.choices)
    # groups = models.ForeignKey(Group, null=True, related_name='user_group', on_delete=models.SET_NULL)
    # user_permissions = models.ForeignKey(Permission, null=True, related_name='user_permissions', on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)



# ===============================================================
# ========================  Patients  ===========================
# ===============================================================
class PatientManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.PATIENT)


class Patient(User):
    # id = models.AutoField(primary_key=True)
    # civil_status = models.ForeignKey(Civil_Status, null=True, on_delete=models.SET_NULL)
    # phone = models.CharField(max_length=20)
    # email = models.EmailField(max_length=200, null=True)
    # date = models.DateField(auto_now_add=True, blank=True)
    # password = models.CharField(max_length=30, default=uuid.uuid4)

    base_role = User.Role.PATIENT

    patient = PatientManager()

    class Meta:
        proxy = True

    # def __str__(self):
    #   return self.civil_status.nationality_id

@receiver(post_save, sender=Patient)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == 'PATIENT':
        PatientProfile.objects.create(user=instance)
        Basic_Health_State.objects.create(patient=instance)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == 'PATIENT':
        PatientProfile.objects.create(user=instance)
        Basic_Health_State.objects.create(patient=instance)

class PatientProfile(models.Model):
    user = models.ForeignKey(Patient, on_delete=models.CASCADE)
    civil_status = models.ForeignKey(Civil_Status, null=True, on_delete=models.SET_NULL)
    phone = models.CharField(max_length=20)
    date_joined = models.DateField(auto_now_add=True, blank=True)
    is_deleted = models.BooleanField(null=False, default=False)
    photo = models.ImageField(null=True, blank=True, default='avatar.jpg')




# ===============================================================
# ========================  Hospital  ===========================
# ===============================================================
class HospitalManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.HOSPITAL)


class Hospital(User):
    # hospital_id = models.IntegerField(primary_key=True, editable=False)
    # name = models.CharField(max_length=100)
    # email = models.EmailField(max_length=200, unique=True)
    # logo = models.ImageField(null=True, blank=True)
    # username = models.CharField(max_length=50, unique=True)
    # password = models.UUIDField(max_length=9, default=uuid.uuid4)
    # active = models.BooleanField(null=False, default=True)
    # date = models.DateField(auto_now_add=True, blank=True)

    base_role = User.Role.HOSPITAL

    hospital = HospitalManager()

    class Meta:
        proxy = True

    # def __str__(self):
    #     return self.name

@receiver(post_save, sender=Hospital)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == 'HOSPITAL':
        HospitalProfile.objects.create(user=instance)

class HospitalProfile(models.Model):
    hospital_id = models.IntegerField(primary_key=True, editable=False)
    user = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    logo = models.ImageField(null=True, blank=True)
    is_active = models.BooleanField(null=False, default=True)
    is_deleted = models.BooleanField(null=False, default=False)
    date_joined = models.DateField(auto_now_add=True, blank=True)


#===============================================================
#=====================  Kin of patient  ========================
#===============================================================
class Kin(models.Model):
	Relationships = (
		('Father', 'Father'),
		('Mother', 'Mother'),
		('Husband', 'Husband'),
		('Wife', 'Wife'),
		('Son', 'Son'),
		('Daughter', 'Dauther'),
		('Brother', 'Father'),
		('Sister', 'Sister'),
		('Uncle', 'Uncle'),
		('aunt', 'aunt'),
		('Grandfather', 'Grandfather'),
		('grandmother', 'grandmother'),
		('Step Father', 'Step Father'),
		('Step Mother', 'Step Mother'),
		)
	id = models.AutoField(primary_key=True)
	full_name = models.CharField(max_length=200)
	address = models.CharField(max_length=1000, null=True)
	phone = models.CharField(max_length=20)
	email = models.EmailField(max_length=200, unique=True, null=True)
	patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL, related_name='kin_patient')
	relationship = models.CharField(max_length=200, choices=Relationships)

	def __str__(self):
		return "{} for {}".format(self.full_name)



#===============================================================
#====================  Hospital's Stuff  =======================
#===============================================================
class Stuff(models.Model):
	id = models.IntegerField(primary_key=True, default=random.randint(10000000000,90000000000), editable=False)
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=200, unique=True)
	hospital = models.ForeignKey(Hospital, null=True, on_delete=models.SET_NULL, related_name='stuff_hospital')
	role = models.CharField(max_length=100, null=True)
	# username = models.CharField(max_length=50, unique=True)
	password = models.UUIDField(max_length=9, default=uuid.uuid4)
	

	def __str__(self):
		return self.name



#===============================================================
#=================  Medical Examinations  ======================
#===============================================================
class Medical_Examination(models.Model):

	Types = (
		("Biopsy","Biopsy"),
		("Colonoscopy","Colonoscopy"),
		("CT scan","CT scan"),
		("CT scans and radiation exposure in children and young people","CT scans and radiation exposure in children and young people"),
		("Electrocardiogram (ECG)","Electrocardiogram (ECG)"),
		("Electroencephalogram (EEG)","Electroencephalogram (EEG)"),
		("Gastroscopy","Gastroscopy"),
		("Eye tests","Eye tests"),
		("Hearing test","Hearing test"),
		("MRI scan","MRI scan"),
		("PET scan","PET scan"),
		("Ultrasound","Ultrasound"),
		("X-rays","X-rays"),
		)

	id = models.AutoField(primary_key=True)
	patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL, related_name='medical_examination_patient')
	type = models.CharField(max_length=200, choices=Types)
	report = models.CharField(max_length=1000, null=True, blank=True)
	date = models.DateField(auto_now_add=True, null=True)
	result = models.FileField()
	# stuff = models.ForeignKey(Stuff, null=True, on_delete=models.SET_NULL)
	# hospital = models.ForeignKey(Hospital, null=True, on_delete=models.SET_NULL, related_name='medical_examination_hospital')


	def __str__(self):
		return self.patient.civil_status.full_name


#===============================================================
#=================  Basic Health State  ======================
#===============================================================
class Basic_Health_State(models.Model):

	Types = (
		("Heart Rate","Heart Rate"),
		("Oxygen Saturation","Oxygen Saturation"),
		("Body Temperature","Body Temperature"),
		("Glucose Level","Glucose Level"),
		)

	id = models.AutoField(primary_key=True)
	patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL, related_name='basic_health_state_patient')
	heart_rate = models.IntegerField(null=False, default=0)
	oxygen_saturation = models.IntegerField(null=False, default=0)
	body_temperature = models.IntegerField(null=False, default=0)
	glucose_level = models.IntegerField(null=False, default=0)
	date = models.DateTimeField(auto_now_add=True)
	# stuff = models.ForeignKey(Stuff, null=True, on_delete=models.SET_NULL)
	# hospital = models.ForeignKey(Hospital, null=True, on_delete=models.SET_NULL, related_name='basic_health_state_hospital')


	def __str__(self):
		return self.patient.civil_status.full_name


#===============================================================
#=================  Basic Health State  ======================
#===============================================================
class Prescription(models.Model):

	Types = (
		("Heart Disease","Heart Disease"),
		("Skin Care","Skin Care"),
		("Diabetes Disease","Diabetes Disease"),
		)

	id = models.AutoField(primary_key=True)
	patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL, related_name='patient')
	name = models.TextField(null=False)
	type = models.CharField(max_length=200, choices=Types)
	start_date = models.DateField()
	end_date = models.DateField()
	date = models.DateTimeField(auto_now_add=True)
	note = models.CharField(max_length=1000, null=True, blank=True)
	# stuff = models.ForeignKey(Stuff, null=True, on_delete=models.SET_NULL)
	# hospital = models.ForeignKey(Hospital, null=True, on_delete=models.SET_NULL, related_name='prescription_hospital')

	@property
	def duration(self):
		if self.end_date is None:
			return None
		return int((self.end_date - self.start_date).days)

	def __str__(self):
		return self.patient.civil_status.full_name