from django.shortcuts import render
from .models import ConsumerLForm, BusinessLForm
from .serializers import ConsumerLFormSerializer, BusinessLFormSerializer
from rest_framework import viewsets


# Create your views here.
class ConsumerView(viewsets.ModelViewSet):
    queryset = ConsumerLForm.objects.all()
    serializer_class = ConsumerLFormSerializer

class BusinessView(viewsets.ModelViewSet):
    queryset = BusinessLForm.objects.all()
    serializer_class = BusinessLFormSerializer
