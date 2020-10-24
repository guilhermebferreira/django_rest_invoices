from django.db import connection, transaction

from .models import Invoice


class InvoiceRepository:

    def create(self, data: dict):
        # data = {
        #     "reference_month": reference_month,
        #     "reference_year": reference_year,
        #     "document": document,
        #     "description": description,
        #     "amount": amount,
        #     "is_active": is_active,
        # }

        try:
            query = "INSERT INTO invoices_invoice  " \
                    "(reference_month, reference_year, document, description, amount, is_active) " \
                    "VALUES  " \
                    "({}, {}, '{}', '{}', {}, {})".format(data['reference_month'], data['reference_year'],
                                                      data['document'], data['description'], data['amount'],
                                                      data['is_active'])
            with connection.cursor() as cursor:
                cursor.execute(query)
                data['id'] = cursor.lastrowid
                return data, True
        except Exception as ex:
            print(str(ex))
            return ex, False

    def update(self):
        pass

    def delete(self):
        pass

    def list(self):
        list = Invoice.objects.raw('SELECT * FROM invoice')

        return list
