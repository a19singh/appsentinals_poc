import logging
from django.shortcuts import render
from rest_framework import viewsets, status

from .models import PlatformUser
from .serializers import PlatformUserSerializer, PlatformUserListSerializer

class PlatformUserView(viewsets.ModelViewSet):
    """
    Model View to Create Platform User
    """
    queryset = PlatformUser.objects.all()
    serializer_class = PlatformUserSerializer 


class PlatformUserListView(viewsets.ModelViewSet):
    """
    Model View to Create Platform User
    """
    queryset = PlatformUser.objects.all()
    serializer_class = PlatformUserListSerializer 
