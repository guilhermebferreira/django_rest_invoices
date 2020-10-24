from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from invoices.models import Invoice
from invoices.repository import InvoiceRepository
from invoices.serializers import InvoiceSerializer


class InvoicesView(APIView, LimitOffsetPagination):
    """
    Invoices API View
    """
    repository = InvoiceRepository()
    ordering_by = ['reference_month', 'reference_year', 'document']
    filter_by = [
        {'param': 'reference_month', 'operator': '='},
        {'param': 'reference_year', 'operator': '='},
        {'param': 'document', 'operator': 'like'},
    ]

    def get(self, request, format=None):
        try:
            order_by = self.get_order_by(request)
            filter_by = self.get_filter_by(request)

            query_select = 'SELECT * FROM invoices_invoice'
            query_order = ''
            query_where = ''
            if order_by:
                order_by = ', '.join(order_by)
                query_order = ' ORDER BY ' + order_by
            if filter_by:
                filter_by = ' AND '.join(filter_by)
                query_where = ' WHERE ' + filter_by

            query = query_select + query_where + query_order

            items = Invoice.objects.raw(query)

            results = self.paginate_queryset(items, request)

            serializer = InvoiceSerializer(results, many=True)
            return self.get_paginated_response(serializer.data)
        except Exception as ex:
            return Response(ex, status=status.HTTP_400_BAD_REQUEST)

    def get_order_by(self, request):
        order_by_params = self.request.query_params.get('order_by', '')
        order = []
        if order_by_params:
            for order_by in order_by_params.split(','):
                order_by = order_by.strip()
                is_reversed = order_by.startswith('-')
                order_attr = order_by.lstrip('-')

                if order_attr not in self.ordering_by:
                    raise ValidationError(
                        '{} - invalid param value (must be: {})'.format(order_attr, ', '.join(self.ordering_by)))

                order_sign = 'DESC' if is_reversed else 'ASC'
                order_statment = order_attr + ' ' + order_sign
                order.append(order_statment)
        return order

    def get_filter_by(self, request):

        where = []

        for param in self.filter_by:
            param_value = self.request.query_params.get(param.get('param'))

            if param_value:
                where.append("{} {} '{}'".format(param.get('param'), param.get('operator', '='), param_value))

        return where

    def post(self, request, format=None):
        serializer = InvoiceSerializer(data=request.data)

        if serializer.is_valid():
            resp, ok = self.repository.create(serializer.data)
            if ok:
                return Response(resp, status=status.HTTP_201_CREATED)

            return Response(str(resp), status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        # perform delete

        try:
            Invoice.objects.get(id=pk)
        except Invoice.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if pk:
            resp, ok = self.repository.deactivate(int(pk))
            if ok:
                return Response(resp, status=status.HTTP_200_OK)
            return Response(str(resp), status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)
