from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from invoices.serializers import InvoiceSerializer
from invoices.repository import InvoiceRepository

class InvoicesView(APIView):
    """
    Invoices API View
    """
    repository = InvoiceRepository()

    def get(self, request):
        # retrieve items
        return Response([])

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
        return Response(status=status.HTTP_204_NO_CONTENT)

