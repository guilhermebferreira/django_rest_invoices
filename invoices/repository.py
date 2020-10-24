from django.db import connection

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

    def deactivate(self, pk):
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE invoices_invoice SET is_active = FALSE, deactive_at=NOW() WHERE id={}".format(pk))
                # row = Invoice.objects.raw("SELECT * FROM invoices_invoice WHERE id={}".format(pk))

                cursor.execute("SELECT * FROM invoices_invoice WHERE id={}".format(pk))
                row = self.__dictfetchone(cursor)

            return row, True

        except Exception as ex:
            print(str(ex))
            return ex, False

    def delete(self):
        pass

    def list(self):
        list = Invoice.objects.raw('SELECT * FROM invoice')

        return list

    def __dictfetchall(self, cursor):
        "Returns all rows from a cursor as a dict"
        desc = cursor.description
        return [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
        ]

    def __dictfetchone(self, cursor):
        "Returns all rows from a cursor as a dict"
        desc = cursor.description
        row = cursor.fetchone()
        return  dict(zip([col[0] for col in desc], row))