from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status

from ..models import Record
from ..serializer import RecordSerializer


class RecordList(APIView):
    """
    List all devices, or create a new device.
    """
    def get(self, request, format=None):
        records = Record.objects.all()
        serializer = RecordSerializer(records, many=True)
        return Response(serializer.data)


class RecordDetail(APIView):
    """
    Retrieve, update or delete a device instance.
    """

    def get_object(self, pk):
        try:
            return Record.objects.get(pk=pk)
        except Record.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        record = self.get_object(pk)
        serializer = RecordSerializer(record)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        record = self.get_object(pk)
        serializer = RecordSerializer(record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        device = self.get_object(pk)
        device.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
