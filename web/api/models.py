from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Device(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)


class UserDreem(User):
    devices = models.ManyToManyField(Device)

class Record(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    userDreem = models.ForeignKey(UserDreem, on_delete=models.CASCADE)



