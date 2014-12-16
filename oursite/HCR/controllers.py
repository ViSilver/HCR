from django.shortcuts import get_object_or_404

from HCR.dao import *


class PatientController(object):
	__patientDAO__ = PatientDAO()
	__appointmentDAO__ = AppointmentDAO()
	__patient__ = object()

	# def create(self, name):
	# 	self.__patientDAO__.create(name)
	# 	return

	def createAppointment(self, doctor, date, patient):
		self.__appointmentDAO__.create(null, patient, doctor, date, False)
		return

class SpecializationController(object):
	__specializationDAO__ = SpecializationDAO()

	def getAll(self):
		return self.__specializationDAO__.getAll()

	def getById(self, ID):
		return self.__specializationDAO__.getById(ID)
	
class DoctorController(object):
	__doctorDAO__ = DoctorDAO()
	__specializationDAO__ = SpecializationDAO()

	def getAll(self):
		return self.__doctorDAO__.getAll()

	def getSpecialization(self, doctor):
		return self.__specializationDAO__.getByDoctor(doctor)

	def getById(self, doc_id):
		return self.__doctorDAO__.getById(doc_id)

	def getBySpecId(self, spec_id):
		return self.__doctorDAO__.getBySpecialization(SpecializationController().getById(spec_id)) 
		
class AppointmentController(object):
	__appointmentDAO__ = AppointmentDAO()

	def getOccDaysByDoctorAndDate(self, doctor, date):
		return self.__appointmentDAO__.getOccDaysByDoctorAndDate(doctor, date)


