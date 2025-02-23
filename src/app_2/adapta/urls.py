"""
URL configuration for adapta project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from base.views import MessagesViewSet
from rest_framework import routers

from django.contrib.auth.models import User, Group

# ? User management in app_1
admin.site.unregister(User)
admin.site.unregister(Group)


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'api/messages', MessagesViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
]
