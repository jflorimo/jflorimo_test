import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer


class Download(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):

        path = '/data/web/storage/'
        files = [path+f.title() for f in os.listdir(path)]
        return  Response(template_name='download.html', data={
            'user': request.user,
            'file_dict': files,
        })