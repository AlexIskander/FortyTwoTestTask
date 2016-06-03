from __future__ import absolute_import
from django.contrib import admin

# Register your models here.

from .models import My_users


admin.site.register( My_users )
