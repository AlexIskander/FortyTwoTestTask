from __future__ import absolute_import

from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import ExpansionUsers
# Create your views here.


def home_page(request, template="base.html", output_number_page=10):

    list_user = ExpansionUsers.objects.all()
    # Show  users per page
    paginator = Paginator(list_user, output_number_page)

    page = request.GET.get('page')
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, template, {"users": users})
