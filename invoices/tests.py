import unittest
import mock

from rest_framework.authtoken.admin import User
from rest_framework.test import APIClient


def mock_create_invoice(self, data):
    data['id'] = 10
    return data, True


class InvoicesTestCase(unittest.TestCase):
    fixtures = ["invoices/fixtures/invoices.json"]

    def setUp(self):
        user = User(username='test', email='user@test.com', password='test@testUser')
        self.client = APIClient()
        self.client.force_authenticate(user=user)

    def test_get(self):
        response = self.client.get('/api/invoices/')
        self.assertEqual(response.status_code, 200)



    @mock.patch('invoices.repository.InvoiceRepository.create', mock_create_invoice)
    def test_create(self):
        good_data = {
            "reference_month": 6,
            "reference_year": 2021,
            "document": "text test eeee",
            "description": "teste222aaaaaa",
            "amount": "20.99",
            "is_active": True
        }

        response = self.client.post('/api/invoices/', data=good_data)
        self.assertEqual(response.status_code, 201)

        good_data = {
            "reference_month": 6,
            "reference_year": 2021,
            "document": "text test eeee",
            "description": "teste com valores maiores e sem coluna is_active",
            "amount": "89891212.99"
        }

        response = self.client.post('/api/invoices/', data=good_data)

        self.assertEqual(response.status_code, 201)
        self.assertTrue('is_active' in response.data)


    @mock.patch('invoices.repository.InvoiceRepository.create', mock_create_invoice)
    def test_create_invalid_data(self):
        bad_data_invalid_month = {
            "reference_month": 16,
            "reference_year": 2021,
            "document": "text test eeee",
            "description": "teste222aaaaaa",
            "amount": "20.99",
            "is_active": True
        }

        response = self.client.post('/api/invoices/', data=bad_data_invalid_month)
        self.assertEqual(response.status_code, 400)

        bad_data_invalid_year = {
            "reference_month": 6,
            "reference_year": 1,
            "document": "text test eeee",
            "description": "teste222aaaaaa",
            "amount": "20.99",
            "is_active": True
        }

        response = self.client.post('/api/invoices/', data=bad_data_invalid_year)
        self.assertEqual(response.status_code, 400)

        bad_data_invalid_description_len = {
            "reference_month": 6,
            "reference_year": 1,
            "document": "text test eeee",
            "description": "mORjtuZradlJ2PSoALOOctvFEKU6nUZRuY6urpxEjwKtf0RkQXz2ec8TRZ86N6PuERManxwuiplgb0rpZrSuD721ApcE0k5XicjTU7CUMmXvqV0vKxN36f4vnvmv0PtQN5v2xReB6yCczjb78PLHtvXrE0S9PV091k4NdnopgAD9KSdk2yXmfzUYe57g8FvhZwMTzjJ72h92ocuEbiTA873ksAa5mUUCyi1s7k5IoxIPxwhvMkTQZ1K4lN2i5MdGmpLaCEDPr0EfASkKvgaOuH5Ciaofm1sWTAvWu6fUyR4o",
            "amount": "20.99",
            "is_active": True
        }

        response = self.client.post('/api/invoices/', data=bad_data_invalid_description_len)
        self.assertEqual(response.status_code, 400)

        bad_data_invalid_document_len = {
            "reference_month": 6,
            "reference_year": 1,
            "document": "mORjtuZradlJ2PSoALOOctvFEKU6nUZRuY",
            "description": "aa",
            "amount": "20.99",
            "is_active": True
        }

        response = self.client.post('/api/invoices/', data=bad_data_invalid_document_len)
        self.assertEqual(response.status_code, 400)

        bad_data_invalid_amount_len = {
            "reference_month": 6,
            "reference_year": 1,
            "document": "mORjtuZradlJ2PSoALOOctvFEKU6nUZRuY",
            "description": "aa",
            "amount": "123456789123456789.99",
            "is_active": True
        }

        response = self.client.post('/api/invoices/', data=bad_data_invalid_amount_len)
        self.assertEqual(response.status_code, 400)

        bad_data_invalid_amount_decimal_len = {
            "reference_month": 6,
            "reference_year": 1,
            "document": "mORjtuZradlJ2PSoALOOctvFEKU6nUZRuY",
            "description": "aa",
            "amount": "99.9999",
            "is_active": True
        }

        response = self.client.post('/api/invoices/', data=bad_data_invalid_amount_decimal_len)
        self.assertEqual(response.status_code, 400)
