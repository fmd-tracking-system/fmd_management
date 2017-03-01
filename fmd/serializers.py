from rest_framework import serializers
from .models import Farm, FmdData
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class FarmSerializer(serializers.ModelSerializer):

    class Meta:
        model = Farm
        fields = "__all__"


class FmdDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = FmdData
        fields = "__all__"
