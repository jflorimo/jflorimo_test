from rest_framework.response import Response


from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status

from ..models import Device, Record
from ..serializer import DeviceSerializer, UserSerializer, RecordSerializer


class DeviceList(APIView):
    """
    List all devices, or create a new device.
    """
    def get(self, request, format=None):
        devices = Device.objects.all()
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeviceDetail(APIView):
    """
    Retrieve, update or delete a device instance.
    """

    def get_object(self, pk):
        try:
            return Device.objects.get(pk=pk)
        except Device.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        device = self.get_object(pk)
        serializer = DeviceSerializer(device)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        device = self.get_object(pk)
        serializer = DeviceSerializer(device, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        print(pk)
        device = self.get_object(pk)
        print(device.__str__())
        device.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
