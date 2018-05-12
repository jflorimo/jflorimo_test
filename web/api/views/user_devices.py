from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status

from ..models import UserDevice
from ..serializer import UserDeviceSerializer


class UserDeviceList(APIView):
    def get(self, request, format=None):
        devices = UserDevice.objects.all()
        serializer = UserDeviceSerializer(devices, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserDeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDeviceDetail(APIView):
    """
    Retrieve, update or delete a user_device instance.
    """

    def get_object(self, pk):
        try:
            return UserDevice.objects.filter(owner=pk).first()
        except UserDevice.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        device = UserDevice.objects.filter(owner=pk).all()
        serializer = UserDeviceSerializer(device, many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        device = self.get_object(pk)
        serializer = UserDeviceSerializer(device, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        device = self.get_object(pk)
        device.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
