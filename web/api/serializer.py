from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Device, Record, UserDevice, RecordData


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class UserDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDevice
        fields = '__all__'

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'

class RecordDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecordData
        fields = ('id', 'record', 'chanel')