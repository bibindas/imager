from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class imager(models.Model):
	user= models.ForeignKey(User,on_delete= models.CASCADE)
	image=models.ImageField(blank=True,null=True,upload_to="images/")
	description=models.CharField(max_length=50,null=True,blank=True)
	like=models.CharField(max_length=50,blank=True,null=True)
