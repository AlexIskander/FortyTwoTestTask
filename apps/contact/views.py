from __future__ import absolute_import

from django.shortcuts import render


from .models import ExpansionUsers
# Create your views here.


def home_page(request, template="base.html", limit=1):

    users = ExpansionUsers.objects.all()[:limit]
    return render(request, template, {"users": users})
