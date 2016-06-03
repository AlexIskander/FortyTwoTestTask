from __future__ import absolute_import
from django.shortcuts import render


# Create your views here.
from .models import My_users

def home( request, template=u'base.html' ) :
    list_user = My_users.objects.all()
    return render(request,  template, {"list_user": list_user } )