from django.urls import path

from .views import InvoicesView

app_name = "articles"

urlpatterns = [
    path('invoices/', InvoicesView.as_view()),
]
