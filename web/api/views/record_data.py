from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status

from ..models import RecordData
from ..serializer import RecordDataSerializer


class RecordDataList(APIView):
    def get(self, request, format=None):
        record_data = RecordData.objects.all()
        serializer = RecordDataSerializer(record_data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RecordDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RecordDataDetail(APIView):
    """
    Retrieve, update or delete a record_data instance.
    """

    def get_object(self, pk):
        try:
            return RecordData.objects.get(pk=pk)
        except RecordData.DoesNotExist:
            raise Http404

    """
    GET RECORD_DATA BY RECORD_DATA ID 
    """
    def get(self, request, pk, format=None):
        data = self.get_object(pk)
        serializer = RecordDataSerializer(data)
        return Response(serializer.data)

    """
    UPDATE RECORD_DATA BY RECORD_DATA ID 
    """
    def put(self, request, pk, format=None):
        data = self.get_object(pk)
        serializer = RecordDataSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """
    DELETE RECORD_DATA BY RECORD_DATA ID 
    """
    def delete(self, request, pk, format=None):
        data = self.get_object(pk)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RecordFileRecordData(APIView):

    """
    GET RECORD DETAIL BY RECORD ID
    """
    def get(self, request, pk, format=None):
        data = RecordData.objects.filter(record=pk).all()
        serializer = RecordDataSerializer(data, many=True)
        return Response(serializer.data)