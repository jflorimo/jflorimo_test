from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import devices, home

urlpatterns = [
    url(r'', home.main),
    url(r'^device/$', devices.device_list),
    url(r'^device/(?P<pk>[0-9]+)$', devices.device_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)