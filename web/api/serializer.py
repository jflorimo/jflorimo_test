from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Device, UserDreem, Record


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('id', 'name', 'created')

class UserDreemSerializer(serializers.HyperlinkedModelSerializer):
    devices = serializers.PrimaryKeyRelatedField(many=True, queryset=Device.objects.all())
    class Meta:
        model = UserDreem
        fields = ('username', 'email')

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ('name', 'device', 'userDreem','created')