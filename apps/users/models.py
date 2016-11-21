# -*- coding: utf-8 -*-

#import python
import os

# django import
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ExpansionUsers(User):

    image            = models.ImageField(upload_to="users_image", verbose_name=u'Фото', blank=True)
    biometric_number = models.CharField(max_length=40, verbose_name=u'Биометрический код', blank=True )
    skype            = models.CharField(max_length=40, verbose_name=u'Skype', blank=True)
    icq              = models.CharField(max_length=40, verbose_name=u'jaber', blank=True)
    birthday         = models.DateField(verbose_name=u'Дата рожджения', blank=True, null=True)
    other            = models.TextField(verbose_name=u'Другие данные', blank=True)

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
