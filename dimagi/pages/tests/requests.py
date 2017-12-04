from __future__ import absolute_import
from django.test import TestCase, RequestFactory

from dimagi.pages.views import home


class SimpleTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_details(self):
        # Create an instance of a GET request.
        request = self.factory.get('/')

        # Test my_view() as if it were deployed at /customer/details
        response = home(request)
        self.assertEqual(response.status_code, 200)
