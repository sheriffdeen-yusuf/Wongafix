"""wongafixServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

#https://www.django-rest-framework.org/
#read on router for more explanations

from api.views import  ConsumerView, BusinessView
from rest_framework import routers

route = routers.DefaultRouter()
route.register("", ConsumerView, basename="consumerView")

route2 = routers.DefaultRouter()
route2.register("", BusinessView, basename="BusinessView")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('consumerApi/', include(route.urls)),
    path('businessApi/', include(route2.urls)),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#the above setting wasnt added by default. it was used to configure the media to urls
#check documentation of static files from the offical doc