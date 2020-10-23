from http import HTTPStatus
# from django.test import TestCase
import mock
from invoices.models import Invoice
import unittest

from rest_framework.test import APIClient

def mock_test(*args, **kwargs):
    return 200

class InvoicesTestCase(unittest.TestCase):

    def setUp(self):
        self.client = APIClient()

    # @mock.patch('invoices.models.Invoice.get_test', mock_test)
    def test_get(self):
        # self.client = APIClient()
        response = self.client.post('/api/invoices/')
        self.assertEqual(response.status_code, 201)
        print(response)

        # mock test
        # i = Invoice()
        # self.assertEqual(i.get_test(), 200)

