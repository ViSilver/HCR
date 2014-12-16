from HCR.models import *
from abc import ABCMeta, abstractmethod
from django.shortcuts import get_object_or_404


class BaseDAO(object):
	__metaclass__ = ABCMeta

	@abstractmethod
	def count(self):
		nrOfItems = len(self.__entityClass__.objects.all())
		return nrOfItems

	@abstractmethod
	def delete(self):
		if (isinstance(self.__localObject__, self.__entityClass__)):
			self.__localObject__.delete()
			print("deleting the __localObject__")
		return 

	# criteria of search is not clearly defined
	@abstractmethod
	def findAll(self):
		pass
		
	@abstractmethod
	def getAll(self):
		self.__localObject__ = self.__entityClass__.objects.all()
		return self.__localObject__

	@abstractmethod
	def getById(self, ID):
		self.__localObject__ = get_object_or_404(self.__entityClass__, pk=ID)
		return self.__localObject__

	@abstractmethod
	def save(self):
		if (isinstance(self.__localObject__, self.__entityClass__)):
			self.__localObject__.save()
		return 

class PatientDAO(BaseDAO):
	__entityClass__ = Patient
	__localObject__ = object()

	def getByAppointment(self, app):
		self.__localObject__ = self.__entityClass__.objects.filter(appointment = app)[0]
		return self.__localObject__

	def getByTreatment(self, treat):
		self.__localObject__ = self.__entityClass__.objects.filter(appointment__treatment = treat)[0]
		return self.__localObject__

	def create(self, name):
		self.__localObject__ = self.__entityClass__(name = name)
		return 

class DoctorDAO(BaseDAO):
	__entityClass__ = Doctor
	__localObject__ = object()

	def getByAppointment(self, app):
		self.__localObject__ = self.__entityClass__.objects.filter(appointment = app)[0]
		return self.__localObject__

	def getBySpecialization(self, spec):
		self.__localObject__ = self.__entityClass__.objects.filter(specialization = spec)
		return self.__localObject__

	def getByTreatment(self, treat):
		self.__localObject__ = self.__entityClass__.objects.filter(appointment__treatment = treat)[0]
		return self.__localObject__

	def create(self, name, spec):
		self.__localObject__ = self.__entityClass__(name = name, specialization = spec)
		return

class SpecializationDAO(BaseDAO):
	__entityClass__ = Specialization
	__localObject__ = object()

	def getByDoctor(self, doctor):
		self.__localObject__ = self.__entityClass__.objects.filter(doctor = doctor)[0]
		return self.__localObject__


class TreatmentDAO(BaseDAO):
	__entityClass__ = Treatment 
	__localObject__ = object()

	def getByPatient(self, patient):
		self.__localObject__ = self.__entityClass__.objects.filter(appointment__patient = patient)[0]
		return self.__localObject__

	def getByDoctor(self, doctor):
		self.__localObject__ = self.__entityClass__.objects.filter(appointment__doctor = doctor)[0]
		return self.__localObject__

	def create(self, date, desc):
		self.__localObject__ = self.__entityClass__(date = date, description = desc)
		return

class AppointmentDAO(BaseDAO):
	__entityClass__ = Appointment
	__localObject__ = object()

	def getByDate(self, date):
		listOfAppointments = self.__entityClass__.objects.filter(date = date)
		return listOfAppointments

	def getByPatient(self, patient):
		listOfAppointments = self.__entityClass__.objects.filter(patient = patient)
		return listOfAppointments

	def getByDoctor(self, doctor):
		listOfAppointments = self.__entityClass__.objects.filter(doctor = doctor)
		return listOfAppointments

	def getByTreatment(self, treat):
		self.__localObject__ = self.__entityClass__.objects.filter(treatment = treat)[0]
		return self.__localObject__

	def create(self, treat, patient, doctor, date, valid):
		self.__localObject__ = self.__entityClass__(treatment = treat, patient = patient, doctor = doctor, date = date, validatedByPatient = valid)
		return

	def getOccDaysByDoctorAndDate(self, doctor, date):
		apps = self.__entityClass__.objects.filter(doctor = doctor, date__gt= date)
		days = []

		for item in apps:
			days.append(item.date.day)

		return days


class ForumDAO(BaseDAO):
	__entityClass__ = Forum 
	__localObject__ = object()

	def create(self, topic, owner):
		self.__localObject__ = self.__entityClass__(topic = topic, owner = owner)
		return

	def getByOwner(self, owner):
		listOfForums = self.__entityClass__.objects.filter(owner = owner)
		return listOfForums

class PatientCommentDAO(BaseDAO):
	__entityClass__ = PatientComment
	__localObject__ = object()

	def getByPatient(self, patient):
		listOfComments = self.__entityClass__.objects.filter(owner = patient)
		return listOfComments

	def create(self, contents, date, owner):
		self.__localObject__ = self.__entityClass__(body = contents, date = date, owner = owner)
		return

class DoctorCommentDAO(BaseDAO):
	__entityClass__ = DoctorComment
	__localObject__ = object()

	def getByPatient(self, doctor):
		listOfComments = self.__entityClass__.objects.filter(owner = doctor)
		return listOfComments

	def create(self, contents, date, owner):
		self.__localObject__ = self.__entityClass__(body = contents, date = date, owner = owner)
		return




	

		
