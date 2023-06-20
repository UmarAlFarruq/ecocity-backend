from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	surname = models.CharField(max_length=200)
	photo = models.ImageField(upload_to='users',null=True)
	phone_number = models.CharField(max_length=30,null=True)



	def __str__(self):

		return self.name+" "+self.surname


class Posts(models.Model):

	title = models.CharField(max_length=200)
	description = models.TextField()
	image = models.ImageField()
	dataCreated =models.DateTimeField(auto_now_add=True)
	dataUpdated =models.DateTimeField(auto_now=True)
	longitude = models.CharField(max_length=30)
	latitude = models.CharField(max_length=30)
	user = models.ForeignKey(User,on_delete=models.CASCADE)


	def __str__(self):

		return self.title








