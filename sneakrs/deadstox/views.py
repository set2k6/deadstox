
from .models import *
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
# from django.shortcuts import HttpResponse
from deadstox.serializers import ClosetsSerializer, SneakersSerializer
import datetime

class ClosetsViewSet(viewsets.ModelViewSet):
    queryset = Closets.objects.all()
    serializer_class = ClosetsSerializer
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly,)


class SneakersViewSet(viewsets.ModelViewSet):
    queryset = Sneakers.objects.all()
    serializer_class = SneakersSerializer
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly,)


