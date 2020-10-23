from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class InvoicesView(APIView):
    """
    Invoices API View
    """

    def get(self, request):
        # retrieve items
        return Response([])

    def post(self, request, format=None):
        # create
        return Response(request.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk, format=None):
        # perform delete
        return Response(status=status.HTTP_204_NO_CONTENT)

