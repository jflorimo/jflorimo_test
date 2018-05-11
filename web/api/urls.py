from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import devices, home

urlpatterns = [
    url(r'^device/?$', devices.DeviceList.as_view()),
    url(r'^device/(?P<pk>[0-9]+)$', devices.DeviceDetail.as_view()),
    # url(r'^auth/', include('rest_framework.urls')),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^auth/registration/', include('rest_auth.registration.urls')),
    url(r'^$', home.Home.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)