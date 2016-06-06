# -*- coding: utf-8 -*-

#import django
from __future__ import absolute_import
from django.test import TestCase

from .models import ExpansionUsers
# Create your tests here.


class AnimalTestCase(TestCase):
    def setUp(self):
        ExpansionUsers.objects.create(username="First", password="last_name")
        ExpansionUsers.objects.create(username="Second", password="last_name")

    def test_get_user(self):
        """ check and set users passwords"""
        first  = ExpansionUsers.objects.get(username="First")
        second = ExpansionUsers.objects.get(username="Second")
        first.check_password("last_name")
        second.check_password("last_name")
        first.set_password("123")
        second.set_password("123")



