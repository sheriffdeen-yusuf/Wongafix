from rest_framework import serializers
from .models import ConsumerLForm, BusinessLForm

class ConsumerLFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsumerLForm
        fields = ['name', 'email', 'hom_addr', 'bvn', 'loan_figure', 'id_upload']


class BusinessLFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessLForm
        fields = ['name', 'email', 'busiz_name', 'busiz_regno', 'bvn', 'loan_amount', 'gur_id_1']