import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (AbstractBaseUser)
from HCR.managers import *

# Create your models here.

class Patient(AbstractBaseUser):
	name = models.CharField(max_length=100)
	#date_of_birth = models.DateField()
	objects = PatientManager()

	USERNAME_FIELD = 'name'
	#REQUIRED_FIELDS = ['date_of_birth']

	# implicit manager methods
	def get_name(self):
		return self.name

	def get_short_name(self):
		# The user is identified by their email address
		return self.name

	def __str__(self):
		return self.name

class Specialization(models.Model):	
	title = models.CharField(max_length = 30)

	#def __init__(self):
	def __str__(self):
		return self.title

class Doctor(AbstractBaseUser):
	name = models.CharField(max_length=100)
	specialization = models.ForeignKey(Specialization, default = 1)
	objects = DoctorManager()

	USERNAME_FIELD = 'name'
	#REQUIRED_FIELDS = ['date_of_birth']

	# implicit manager methods
	def get_name(self):
		return self.name

	def get_short_name(self):
		# The user is identified by their email address
		return self.name

	def __str__(self):
		return self.name

class Treatment(models.Model):
	date = models.DateTimeField('treatment creation date') # change date to date
	description = models.CharField(max_length=256)

	def __str__(self):              # __unicode__ on Python 2
		return self.description

class Appointment(models.Model):
	treatment = models.OneToOneField(Treatment, null=True)
	patient = models.ForeignKey(Patient, default = 1)
	doctor = models.ForeignKey(Doctor, default = 1)
	date = models.DateTimeField('appointment creation date', default = timezone.now())
	validatedByPatient = models.BooleanField(default=False)
	
	def __str__(self):              # __unicode__ on Python 2
		buffer = "date: " + str(self.date)
		if(self.treatment):
			buffer += " treatment: " + str(self.treatment)
		return str(buffer)

	def getValidation(self):
		return self.validatedByPatient

	def getDate(self):
		return self.date

	def wasCreatedRecently(self):
		return self.date >= timezone.now() - datetime.timedelta(days=1)

	#entries = models.Manager()

class  Forum(models.Model):
	topic = models.CharField(max_length = 256)
	owner = models.ForeignKey(Patient, default = 1)

	def __str__(self):
		return self.topic

class PatientComment(models.Model):
	body = models.CharField(max_length = 2048)
	date = models.DateTimeField('patient comment creation', default = timezone.now())
	owner = models.ForeignKey(Patient, default = 1)
		
	def __str__(self):
		return str(self.date) + str(self.owner)

class DoctorComment(models.Model):
	body = models.CharField(max_length = 2048)
	date = models.DateTimeField('doctor comment creation', default = timezone.now())
	owner = models.ForeignKey(Doctor, default = 1)
		
	def __str__(self):
		return str(self.date) + str(self.owner)


class DoctorCommentDAOX(object):
	__entityClass__ = DoctorComment
	__localObject__ = object()

	def getByPatient(self, doctor):
		listOfComments = self.__entityClass__.objects.filter(owner = doctor)
		return listOfComments

	def create(self, contents, date, owner):
		self.__localObject__ = self.__entityClass__(body = contents, date = date, owner = owner)
		return

   