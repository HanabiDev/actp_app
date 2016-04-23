#encoding: utf-8
from django.contrib.auth.models import User

from django.db import models

# Create your models here.
from clubs.models import Club

def get_path(instance,file):
	return 'uploads/partners/'+str(instance.user.id)+'/'+file


class Partner(User):
	GENDERS = (
		("M", "Masculino"),
		("F", "Femenino")
	)
	# Affiliation Info
	models.ForeignKey(Club, related_name='partner_club').contribute_to_class(User, 'club')
	models.BooleanField(default=False).contribute_to_class(User, 'is_approved')

	# Personal info
	models.CharField(max_length=30).contribute_to_class(User, 'doc_id')
	models.DateField(max_length=10).contribute_to_class(User, 'birth_date')
	models.CharField(max_length=30, choices=GENDERS).contribute_to_class(User, 'gender')
	models.CharField(max_length=10).contribute_to_class(User, 'phone')
	models.CharField(max_length=50).contribute_to_class(User, 'address')
	models.ImageField(upload_to=get_path).contribute_to_class(User, 'photo')

	# Support files
	models.FileField(upload_to=get_path).contribute_to_class(User, 'dni_support')
	models.FileField(upload_to=get_path).contribute_to_class(User, 'reference_letter')
	models.FileField(upload_to=get_path).contribute_to_class(User, 'request_letter')
	models.FileField(upload_to=get_path).contribute_to_class(User, 'release_letter')
	models.FileField(upload_to=get_path).contribute_to_class(User, 'eps_affiliation')
	models.FileField(upload_to=get_path).contribute_to_class(User, 'legal_records')
	models.FileField(upload_to=get_path).contribute_to_class(User, 'bank_deposit')

	def save(self, *args, **kwargs):
		super(Partner, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.first_name + ' '+ self.last_name