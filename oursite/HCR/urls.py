from django.conf.urls import patterns, url

from HCR import views

urlpatterns = patterns('',
	
	url(r'^$', views.home, name='home'),
	url(r'^patients/profile/$', views.patient_profile, name='patient_profile'),
	url(r'^doctors/$', views.doctors, name='doctors'),
	url(r'^app/$', views.create_appointment, name='create_appointment'),
	url(r'^contacts/$', views.contacts, name='contacts'),
	url(r'^app/(?P<specialization_id>\d+)/$', views.create_appointment_specs, name='create_appointment_specs'),
	url(r'^app/(?P<specialization_id>\d+)/(?P<doctor_id>\d+)/$', views.create_appointment_dates, name='create_appointment_dates'),
	url(r'^app/(?P<specialization_id>\d+)/(?P<doctor_id>\d+)/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/$', views.create_appointment_to_submit, name='create_appointment_to_submit'),
	
)