from django.db import models
from datetime import datetime
# Create your models here.
class Admin(models.Model):
	admin_username=models.CharField(max_length=20)
	admin_password=models.CharField(max_length=100)
	email_id=models.EmailField(max_length=100)
	first_name=models.CharField(max_length=25)
	last_name=models.CharField(max_length=25)
	mobile_number=models.TextField(max_length=10)

	def __str__(self):
		return self.admin_username

class User(models.Model):
	username=models.CharField(max_length=20)
	password=models.CharField(max_length=100)
	email_id=models.EmailField(max_length=100)
	first_name=models.CharField(max_length=25)
	last_name=models.CharField(max_length=25)
	mobile_number=models.TextField(max_length=10)

	def __str__(self):
		return self.username

class User_data(models.Model):
	data=models.TextField(max_length=500)
	emotion=models.CharField(max_length=20)
	date=models.DateTimeField("date published",default=datetime.now)
	user=models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.emotion