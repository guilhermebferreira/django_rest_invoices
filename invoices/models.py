from django.db import models
from django.utils import timezone


class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    reference_month = models.IntegerField(null=False)
    reference_year = models.IntegerField(null=False)
    document = models.CharField(max_length=14, null=False, blank=False)
    description = models.CharField(max_length=256, null=True, blank=True)
    amount = models.DecimalField(
        max_digits=16, decimal_places=2, null=False)
    is_active = models.BooleanField(default=True, null=False)
    created_at = models.DateTimeField(editable=False)
    deactive_at = models.DateTimeField(null=True)
