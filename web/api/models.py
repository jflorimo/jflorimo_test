from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

class UserDevice(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, null=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

class Record(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    path = models.CharField(max_length=300, blank=False, null=False, default='')
    status = models.CharField(max_length=100, blank=False, default='UNKNOWN')
    device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ('created',)
