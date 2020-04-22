from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
import datetime
from timein.choices import *

class Student(models.Model):
	admin = models.ForeignKey(User, on_delete=models.CASCADE)
	ID_number = models.CharField(max_length=15)
	last_name = models.CharField(max_length=50)
	first_name = models.CharField(max_length=50)
	course = models.CharField(max_length=20)
	purpose = models.CharField(choices=purposes, blank=False, max_length=20, default='general')
	pc = models.IntegerField()
	date = models.DateTimeField(default=timezone.now)
	timeout = models.TimeField(default=timezone.now, blank=True, null=True)
       
	def __str__(self):
		return self.last_name + ', ' + self.first_name 
	def Students(self):
		return self.last_name + ', ' + self.first_name 
	def Date(self):
	    return self.date.strftime("%B %d,%Y")
	def dtin(self):
	    return self.date.strftime("%d %B %Y %I:%M%p")
	def out(self):
	    return self.timeout.strftime("%I:%M%p")
	    