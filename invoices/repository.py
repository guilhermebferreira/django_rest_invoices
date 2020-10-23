from django.db import connection
from .models import Invoice

class InvoiceRepository():

    def create(self, reference_month, reference_year, document, description, amount, is_active=True):
        data = {
            "reference_month": reference_month,
            "reference_year": reference_year,
            "document": document,
            "description": description,
            "amount": amount,
            "is_active": is_active,
        }

        query = "INSERT INTO invoice " \
                "(reference_month, reference_year, document, description, amount, is_active) " \
                " VALUES  " \
                "(:reference_month, :reference_year, :document, :description, :amount, :is_active) ".format(**data)
        with connection.cursor() as cursor:
            cursor.execute(query)

    def update(self):
        pass

    def delete(self):
        pass

    def list(self):
        list = Invoice.objects.raw('SELECT * FROM invoice')

        return list