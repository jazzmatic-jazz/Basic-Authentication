from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class Employee(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [BasicAuthentication,]
    
    def get(self, request, format=None):
        content = {
            'user': str(request.user)
        }
        return Response(content)
        
    permission_classes = [IsAuthenticated,]