from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import Farm, FmdData
from .serializers import FarmSerializer, FmdDataSerializer, UserSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FarmViewSet(viewsets.ModelViewSet):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer


class FmdDataViewSet(viewsets.ModelViewSet):
    queryset = FmdData.objects.all()
    serializer_class = FmdDataSerializer
