# -*- coding: utf-8 -*-

#import django
from __future__ import absolute_import
from django.forms import ModelForm

from .models import ExpansionUsers


class ExpansionUsersForm(ModelForm):
    class Meta:
        model = ExpansionUsers
        widgets = {
            'other': Textarea(attrs={'cols': 80, 'rows': 20}),
        }