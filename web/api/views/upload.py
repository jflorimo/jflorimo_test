import h5py
from h5py import Dataset

from django.http import HttpResponseRedirect
from django import forms
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from django.http import Http404
from background_task import background

from ..models import Device, Record
from django.contrib.auth.models import User


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=200)
    user_id = forms.IntegerField()
    device_id = forms.IntegerField()
    file = forms.FileField()

class Upload(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        return Response(template_name='upload.html')

    @csrf_exempt
    def post(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            device_id = request.POST['device_id']
            user_id = request.POST['user_id']
            title = request.POST['title']

            try:
                device = Device.objects.get(pk=device_id)
                user = User.objects.get(pk=user_id)
            except Device.DoesNotExist:
                raise Http404
            except User.DoesNotExist:
                raise Http404

            self.handle_uploaded_file(title, request.FILES['file'], user, device)
            return HttpResponseRedirect('/record/')
        return Response({'file': 'uploaded'}, template_name='upload.html')

    @staticmethod
    def handle_uploaded_file(title, file, user, device):
        path = '/data/web/storage/'+title
        record = Record.objects.create(name=title, path=path, device=device, owner=user, status=Record.STATUS.UPLOADING)
        with open(path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        print('starting parsing')
        Upload.parse_file(record.id)


    @staticmethod
    @background(queue='parsing_queue')
    def parse_file(record_id):
        record = Record.objects.get(pk=record_id)
        record.status = Record.STATUS.PARSING
        record.save()



        filename = record.path
        f = h5py.File(filename, 'r')

        print("==============\n")

        def find_keys(value):
            finded_keys = {}

            for key in list(value.keys()):
                if isinstance(value[key], Dataset):
                    finded_keys[key] = None
                    # For Values in a list:
                    # finded_keys[key] = list(value[key].value)
                else:
                    finded_keys[key] = find_keys(value[key])

            return finded_keys

        print(find_keys(f))


