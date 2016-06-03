# -*- coding: utf-8 -*-

#import django
from __future__ import absolute_import
from django.contrib import admin

from .models import ExpansionUsers

# Register your models here.

class ExpansionUsersAdmin(admin.ModelAdmin) :
    list_display = ["first_name", "last_name", "email"]
    fields       = ["username", "password", "first_name", "last_name", "email", "image", "biometric_number", "skype", "icq"]



admin.site.register( ExpansionUsers, ExpansionUsersAdmin )