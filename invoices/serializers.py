from rest_framework import serializers

from .models import Invoice


class InvoiceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    reference_month = serializers.IntegerField(min_value=1, max_value=12, required=True)
    reference_year = serializers.IntegerField(min_value=1900, max_value=2999, required=True)
    document = serializers.CharField(max_length=14, required=True)
    description = serializers.CharField(max_length=256, required=True)
    amount = serializers.DecimalField(
        max_digits=16, decimal_places=2, required=True)
    is_active = serializers.BooleanField(default=True)
    created_at = serializers.DateTimeField(read_only=True)
    deactive_at = serializers.DateTimeField(required=False)

    class Meta:
        model = Invoice
        fields = '__all__'
