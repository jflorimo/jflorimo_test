from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import Device, UserDreem, Record
from ..serializer import DeviceSerializer, UserDreemSerializer, RecordSerializer

@api_view(['GET', 'POST'])
def device_list(request, format=None):
    """
    List all code snippets, or create a new device.
    """
    if request.method == 'GET':
        devices = Device.objects.all()
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def device_detail(request, pk, format=None):
    """
    Retrieve, update or delete a device.
    """
    try:
        device = Device.objects.get(pk=pk)
    except Device.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DeviceSerializer(device)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DeviceSerializer(device, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        device.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
