from django.db import models
from account.models import User

class UserProfile(models.Model):
	GENDER_CHOICES = (
		(u'M', u'Male'),
		(u'F', u'Female'),
		)
	user = models.OneToOneField(User,unique=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=100,blank=True)
	age = models.CharField(max_length=3,blank=True)
	gender = models.CharField(max_length=10,blank=True,choices=GENDER_CHOICES)  #Users are allowed to choose their gender through a drop_down box
	major = models.CharField(max_length=100,blank=True)
	hometown = models.CharField(max_length=100,blank=True)
	phoneNum = models.CharField(max_length=20,blank=True)
