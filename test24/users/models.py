# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class My_users(models.Model) :
    name           = models.CharField( max_length = 150, verbose_name = "Имя" )
    last_name      = models.CharField( max_length = 150, verbose_name = "Фамилия" )
    date_birth     = models.DateField( verbose_name = "Дата рожения" )
    bio            = models.CharField( max_length = 150, verbose_name = "BIO" )
    email          = models.EmailField( verbose_name = "Email", blank=True, null=True)
    jaber          = models.CharField( max_length = 150, verbose_name = "jaber", blank=True, null=True)
    skype          = models.CharField( max_length = 150, verbose_name = "skype", blank=True, null=True)
    other_contacts = models.CharField( max_length = 150, verbose_name = "Другие контакты", blank=True, null=True)
    
    def __unicode__ ( self ) :
        return self.name

    class Meta :
        verbose_name        = u'Пользователь'
        verbose_name_plural = u'Пользователи'
        ordering            = [ u'name' ]
