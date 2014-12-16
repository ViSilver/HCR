from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect

from HCR.controllers import *

specControl = SpecializationController()
docControl = DoctorController()
appControl = AppointmentController()

def home(request):
	"""
	Renders the home page of the application.

	**Parameters:**

	*request* - HttpRequest object 

	**Return value:**	

	*HttpResponse object* with an empty dictionary.
	"""
	
	return render(request, 'HCR/home.html', {})

def patient_profile(request):
	"""
	Renders the profile page of the patient.

	**Parameters:**

	*request* - HttpRequest object 

	**Return value:**	

	*HttpResponse object* with an empty pdictionary.
	"""

	return render(request, 'HCR/profile.html', {})

def doctors(request):
	"""
	Renders the page with all doctors and their specialization which are stored in the database.

	**Parameters:**

	*request* - HttpRequest object 

	**Return value:**	

	*HttpResponse object* with a dictionary which contains:
		* a list of the doctors with 'doctors' key.
	"""

	doctors = docControl.getAll()
	context = {'doctors' : doctors}

	return render(request, 'HCR/doctors.html', context)

def create_appointment(request):
	"""
	Renders the first stage of the **creating appointment** process.

	**Parameters:**

	*request* - HttpRequest object 

	**Return value:**	

	*HttpResponse object* with a dictionary which contains:
		* a list of the specialization with 'specialization_list' key.
	"""

	specialization_list = specControl.getAll()
	context = {'specialization_list': specialization_list}
	return render(request, 'HCR/new_appointment.html', context)

def create_appointment_specs(request, specialization_id):
	"""
	Renders the second stage of the **creating appointment** process.

	**Parameters:**

	*request* - HttpRequest object 

	*specialization_id* - integer object. The id of the selected in the first stage specialization.

	**Return value:**	

	*HttpResponse object* with a dictionary which contains:
		* a specialization object with 'specialization' key,
		* a list of doctors, which have the given specialization, with 'doctors' key.
	"""

	specialization = specControl.getById(specialization_id) 
	doctors = docControl.getBySpecId(specialization_id)
	return render(request, 'HCR/new_appointment_specs.html', {'specialization': specialization, 'doctors': doctors})

def create_appointment_dates(request, specialization_id, doctor_id):
	"""
	Renders the third stage of the **creating appointment** process.

	**Parameters:**

	*request* - HttpRequest object 

	*specialization_id* - integer object. The id of the selected in the first stage specialization.

	*doctor_id* - integer object. The id of the selected in the second stage doctor.

	**Return value:**	

	*HttpResponse object* with a dictionary which contains:
	 	* a specialization object with 'specialization' key, 
	 	* a doctor object with 'doctor' key, 
		* an integer object which holds the current year with 'year' key, 
		* an integer object which holds the current month with 'month' key,
		* a list of free days of the selected in the second stage doctor which has the 'doc_free_days' key. 
	"""

	specialization = specControl.getById(specialization_id)
	doctor = docControl.getById(doctor_id)
	current_year = timezone.now().year
	current_month = timezone.now().month
	current_day = timezone.now().day
	doc_free_days = []
	doc_occ_days = appControl.getOccDaysByDoctorAndDate(doctor, timezone.now())

	for day in range(current_day, current_day + 5):
		if (day not in doc_occ_days):
			doc_free_days.append(day)

	context = {'specialization': specialization, 'doctor': doctor, 'doc_free_days': doc_free_days, 'year': current_year, 'month': current_month}
	return render(request, 'HCR/new_appointment_dates.html', context)

def create_appointment_to_submit(request, specialization_id, doctor_id, year, month, day):
	"""
	Renders the fourth stage of the **creating appointment** process.

	**Parameters:**

	*request* - HttpRequest object 

	*specialization_id* - integer object. The id of the selected in the first stage specialization.

	*doctor_id* - integer object. The id of the selected in the second stage doctor.

	*year* - integer object. The selected year of the appointment.

	*month* - integer object. The selected month of the appointment.

	*day* - integer object. The selected day of the appointment.

	**Return value:**	

	*HttpResponse object* with a dictionary which contains:
	 	* a specialization object with 'specialization' key, 
	 	* a doctor object with 'doctor' key, 
		* an integer object which holds the current year with 'year' key, 
		* an integer object which holds the current month with 'month' key,
		* an integer object which holds the selected day with 'day' key. 
	"""

	specialization = specControl.getById(specialization_id)
	doctor = docControl.getById(doctor_id)
	# Create and save the appointment here !!!!!!!
	context = {'specialization': specialization, 'doctor': doctor, 'year': year, 'month': month, 'day':day}

	return render(request, 'HCR/new_appointment_to_submit.html', context)

def contacts(request):
	"""
	Renders the contact page of the Health Care Clinic.

	**Parameters:**

	*request* - HttpRequest object 

	**Return value:**	

	*HttpResponse object* with an empty dictionary.
	"""

	return render(request, 'HCR/contacts.html', {})
