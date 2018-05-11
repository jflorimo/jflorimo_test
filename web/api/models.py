from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Device(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    users = models.ManyToManyField(User, null=True)

    class Meta:
        ordering = ('created',)


class Record(models.Model):

    name = models.CharField(max_length=100, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, blank=False, default='UNKNOWN')
    device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ('created',)



