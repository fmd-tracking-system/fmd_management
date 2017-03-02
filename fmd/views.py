from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import Farm, FmdData
from .serializers import FarmSerializer, FmdDataSerializer, UserSerializer
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse


def index(request):
    return render(request, 'index.html')


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FarmViewSet(viewsets.ModelViewSet):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer


class FmdDataViewSet(viewsets.ModelViewSet):
    queryset = FmdData.objects.all()
    serializer_class = FmdDataSerializer


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = RegistrationForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            user = authenticate(username=user_form.cleaned_data['username'],
                                password=user_form.cleaned_data['password']
                                    )
            login(request, user)
            return HttpResponseRedirect("/index/")
    else:
        user_form = RegistrationForm()
    return render(request,
            'registration/register.html',
            {'user_form': user_form, 'registered': registered} )
