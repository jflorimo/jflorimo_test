from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import StaticHTMLRenderer
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@api_view(['GET'])
@renderer_classes((StaticHTMLRenderer,))
def main(request):
    data = '<html><body>JFLORIMO API TEST</body></html>'
    return Response(data)