from django.contrib import admin
from .models import ConsumerLForm, BusinessLForm

# Register your models here.
# This enables you to see form from the admin dashbord
admin.site.register(ConsumerLForm)
admin.site.register(BusinessLForm)