from django.contrib.auth.models import (BaseUserManager)
from django.db import models 

class PatientManager(BaseUserManager):
	def create_patient(self, name, password=None):
		"""
		Creates and saves a User with the given email, date of
		birth and password.
		"""
		user = self.model(
			name=name,
		)

		user.set_password(password)
		user.save(using=self._db)

		return user




class DoctorManager(BaseUserManager):
	def create_doctor(self, name, password=None):
		"""
		Creates and saves a Doctor with the given name, and password.
		"""
		user = self.model(
			name=name,
		)

		user.set_password(password)
		user.save(using=self._db)

		return user
