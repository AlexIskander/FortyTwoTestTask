# -*- coding: utf-8 -*-

#import python
import os

# django import
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ExpansionUsers(User):
    #keyuser          = models.OneToOneField(User)
    image            = models.ImageField(upload_to="users_image", verbose_name=u'Фото', blank=True)
    biometric_number = models.CharField(max_length=40, verbose_name=u'Бтометрический код', blank=True )
    skype            = models.CharField(max_length=40, verbose_name=u'Skype', blank=True)
    icq              = models.CharField(max_length=40, verbose_name=u'Icq', blank=True)

    def save(self, *args, **kwargs):
        try:
            obj = ExpansionUsers.objects.get(id=self.id)
            if obj.image.name != self.image.name:
                obj.image.delete()
        except: pass
        super(ExpansionUsers, self).save(*args, **kwargs)


    def _images_delete(self, *args ):
    	for item in args:
    	    if os.path.exists(item):
                os.remove(item)

    def delete( self, using=None ):
        obj = ExpansionUsers.objects.get( id=self.id )
        if obj.image:
            self._images_delete( obj.image.path )
        super(ExpansionUsers, self ).delete()


    class Meta :
        verbose_name        = u'Пользователь'
        verbose_name_plural = u'Пользователи'
        ordering            = [ u'username' ]
