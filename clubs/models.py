from django.db import models

# Create your models here.

class Club(models.Model):
	name = models.CharField(max_length=100)
	logo = models.ImageField(upload_to='uploads/clubs/logos/')