from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()




class Upload(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        return Response(template_name='upload.html')

    @csrf_exempt
    def post(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            self.handle_uploaded_file(request.POST['title'], request.FILES['file'])
            return HttpResponseRedirect('/record/')
        return Response(template_name='upload.html')

    @staticmethod
    def handle_uploaded_file(title, file):
        print(title)
        print(file)
        with open('/data/web/storage/'+title, 'wb+') as destination:
            # print(str(len(file.chunks())))
            for chunk in file.chunks():
                destination.write(chunk)
