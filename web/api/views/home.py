from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

# @renderer_classes((StaticHTMLRenderer,))
# def main(request):
#     data = '<html><body>JFLORIMO API TEST</body></html>'
#     return Response(data)

class Home(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home.html'

    def get(self, request):
        return Response()