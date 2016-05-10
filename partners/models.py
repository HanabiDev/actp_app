#encoding: utf-8
from django.contrib.auth.models import User

from django.db import models

# Create your models here.
from clubs.models import Club

def get_path(instance,file):
	return 'uploads/partners/'+str(instance.doc_id)+'/'+file


class Partner(User):
	GENDERS = (
		("M", "Masculino"),
		("F", "Femenino")
	)

	RH = (
		("AP","A+"),
		("AM","A-"),
		("ABP","AB+"),
		("ABM","AB-"),
		("BP","B+"),
		("BM","B-"),
		("OP","O+"),
		("OM","O-"),
	)
	# Affiliation Info

	models.ForeignKey(Club, related_name='partner_club', null=True, blank=True).contribute_to_class(User, 'club')
	models.BooleanField(default=False, verbose_name=u'Aceptado en la asociación').contribute_to_class(User, 'is_approved')
	models.DateField(max_length=30, null=True, verbose_name=u'Miembro desde').contribute_to_class(User, 'member_since')
	# Personal info
	models.CharField(max_length=30, verbose_name=u'Número de documento').contribute_to_class(User, 'doc_id')
	models.DateField(max_length=10, verbose_name=u'Fecha de nacimiento').contribute_to_class(User, 'birth_date')
	models.CharField(max_length=1, choices=GENDERS, verbose_name=u'Género').contribute_to_class(User, 'gender')
	models.CharField(max_length=3, choices=RH, verbose_name=u'RH').contribute_to_class(User, 'rh')
	models.CharField(max_length=10, verbose_name=u'Teléfono').contribute_to_class(User, 'phone')
	models.CharField(max_length=50, verbose_name=u'Dirección').contribute_to_class(User, 'address')
	models.ImageField(upload_to=get_path, verbose_name=u'Foto').contribute_to_class(User, 'photo')

	#work info
	models.CharField(max_length=80, verbose_name=u'Ocupación').contribute_to_class(User, 'occupation')
	models.CharField(max_length=10, verbose_name=u'Teléfono empresa').contribute_to_class(User, 'work_phone')
	models.CharField(max_length=50, verbose_name=u'Dirección empresa').contribute_to_class(User, 'work_address')

	#emergency info
	models.CharField(max_length=60, verbose_name=u'Contacto de emergencia').contribute_to_class(User, 'emergency_contact')
	models.CharField(max_length=10, verbose_name=u'Teléfono del contacto').contribute_to_class(User, 'emergency_phone')

	#health condition
	models.BooleanField(default=False, verbose_name=u'Padece una enfermedad física o mental').contribute_to_class(User, 'have_disease')
	models.CharField(max_length=50, verbose_name=u'¿Cúal?', null=True, blank=True).contribute_to_class(User, 'disease_name')

	#observations
	models.TextField(null=True, blank=True, verbose_name='Observaciones').contribute_to_class(User, 'observations')

	# Support files
	models.FileField(upload_to=get_path, verbose_name=u'Documento de identificación').contribute_to_class(User, 'dni_support')
	models.FileField(upload_to=get_path, verbose_name=u'Carta de recomendación').contribute_to_class(User, 'reference_letter')
	models.FileField(upload_to=get_path, verbose_name=u'Carta de petición').contribute_to_class(User, 'request_letter')
	models.FileField(upload_to=get_path, verbose_name=u'Carta de descargos').contribute_to_class(User, 'release_letter')
	models.FileField(upload_to=get_path, verbose_name=u'Afiliación EPS').contribute_to_class(User, 'eps_affiliation')
	models.FileField(upload_to=get_path, verbose_name=u'Pasado judicial').contribute_to_class(User, 'legal_records')
	models.FileField(upload_to=get_path, verbose_name=u'Consignación').contribute_to_class(User, 'bank_deposit')


	def __unicode__(self):
		return self.first_name + ' '+ self.last_name
