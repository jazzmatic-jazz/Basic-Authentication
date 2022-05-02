from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('employee',Employee)

urlpatterns = [
    path('', include(router.urls)),
]

