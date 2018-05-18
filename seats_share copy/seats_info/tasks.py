from celery.task import task
from django.apps import apps

@task
def reset_seats_info():
	DefaultSeatInfo = apps.get_model('seats_info','DefaultSeatInfo')
	SeatInfo = apps.get_model('seats_info', 'SeatInfo')
	SeatInfo = DefaultSeatInfo
	SeatInfo.save()