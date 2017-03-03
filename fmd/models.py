from django.db import models
from django.contrib.auth.models import User


class Farm(models.Model):
    farm_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=300)
    address = models.TextField(blank=True, null=True)


class FmdData(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=300)
    fmd = models.ForeignKey(Farm)
    farm_condition = models.TextField()
    bgp_requirements = models.TextField()
    corrective_action = models.TextField()

    observed = models.DateTimeField(auto_now_add=True)

    hand_delivered = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    corrected = models.DateTimeField(auto_now_add=True, blank=True, null=True)


class FmdDataImage(models.Model):
    FmdData = models.ForeignKey(FmdData, related_name='images')
    image = models.ImageField()
