from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from api import settings
from invoices.models import Invoice
from invoices.repository import InvoiceRepository
from invoices.serializers import InvoiceSerializer


class InvoicesView(APIView, LimitOffsetPagination):
    """
    Invoices API View
    """
    repository = InvoiceRepository()

    def get(self, request, format=None):

        items = Invoice.objects.all()

        results = self.paginate_queryset(items, request)
        serializer = InvoiceSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

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
                return Response(resp, status=status.HTTP_204_NO_CONTENT)
            return Response(str(resp), status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)
