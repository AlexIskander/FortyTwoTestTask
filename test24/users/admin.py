from django.contrib import admin

# Register your models here.

from users.models import My_users


admin.site.register( My_users )
