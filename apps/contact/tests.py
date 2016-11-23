from __future__ import absolute_import

from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from .views import home_page
from .models import ExpansionUsers


# Create your tests here.


class ExpansionUsersTestCase(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        """Resolve home page"""
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        """Cheack home page title"""
        request = HttpRequest()
        response = home_page(request)
        self.assertIn(b'<title>Home page</title>', response.content)

    def setUp(self):
        ExpansionUsers.objects.create(
            username="test@test.ru",
            first_name="admin",
            last_name="admin",
            email="test@test.ru",
            biometric_number="None",
            skype="test",
            other="test")
        ExpansionUsers.objects.create(
            username="test2@test.ru",
            first_name="admin2",
            last_name="admin2",
            email="test2@test.ru",
            biometric_number="None",
            skype="test2",
            other="test2")

    def test_expansionusers_name(self):
        """ExpansionUsers that can get are correctly first name  last name"""
        user1 = ExpansionUsers.objects.get(username="test@test.ru")
        user2 = ExpansionUsers.objects.get(username="test2@test.ru")
        print user1.first_name, user1.last_name
        print user2.first_name, user2.last_name
