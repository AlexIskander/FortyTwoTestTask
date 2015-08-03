# -*- coding: utf-8 -*-

import os
from django.shortcuts import render_to_response

from users.models import My_users

def home( request ) :
    
    BASE_DIR  = os.path.dirname(os.path.dirname(__file__))
    list_user = My_users.objects.all() 
    return render_to_response( u'base.html', locals() )
