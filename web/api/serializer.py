from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Device, Record


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('id', 'name', 'created')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    devices = serializers.PrimaryKeyRelatedField(many=True, queryset=Device.objects.all())
    class Meta:
        model = User
        fields = ('username', 'email', 'devices')

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ('name', 'device', 'userDreem','created')