from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Device, Record, UserDevice


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('id', 'name', 'created')

class UserDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDevice
        fields = ('owner', 'device', 'created', 'devices')

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ('name', 'status', 'device', 'owner','created')