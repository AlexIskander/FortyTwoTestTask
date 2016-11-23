from __future__ import absolute_import

from django.contrib import admin

from .models import ExpansionUsers

# Register your models here.


class ExpansionUsersAdmin(admin.ModelAdmin):
    list_display = ["username", "last_name", "email"]
    fields = ["username", "first_name", "last_name", "email", "image",
              "biometric_number", "skype", "icq", "birthday", "other"]
admin.site.register(ExpansionUsers, ExpansionUsersAdmin)
