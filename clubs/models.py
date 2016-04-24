#encoding: utf-8
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Club(models.Model):
	name = models.CharField(max_length=100, verbose_name=u'Nombre del club')
	logo = models.ImageField(upload_to='uploads/clubs/logos/', verbose_name=u'Logo')
	header_image = models.ImageField(upload_to='uploads/clubs/headers/', verbose_name=u'Imagen de perfil')
	header_description = models.CharField(max_length=100, verbose_name=u'Descripción de la imagen')
	president = models.ForeignKey(User, related_name='president', null=True, blank=True, verbose_name=u'Presidente')
	foundation = models.DateField(verbose_name=u'Fecha de fundación')
	is_active = models.BooleanField(default=True, verbose_name=u'Club activo')
	website = models.URLField(null=True, blank=True, verbose_name=u'Sitio web')
	fb_page = models.URLField(null=True, blank=True, verbose_name=u'Facebook')
	tw_page = models.URLField(null=True, blank=True, verbose_name=u'Twitter')
	yt_page = models.URLField(null=True, blank=True, verbose_name=u'Youtube')

	def __unicode__(self):
		return self.name