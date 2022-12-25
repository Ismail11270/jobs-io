from django import views
from django.contrib import admin
from django.db import router
from django.urls import path, include
from user.api import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('groups', views.GroupViewSet)
router.register('users', views.UserViewSet)

urlpatterns = [
    path('/', include(router.urls))
]
