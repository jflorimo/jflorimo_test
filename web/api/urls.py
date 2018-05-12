from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import devices, home, users, user_devices

urlpatterns = [
    # USER
    url(r'^user/$', users.UserList.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/$', users.UserDetail.as_view()),
    # USER_DEVICE
    url(r'^user/device/?$', user_devices.UserDeviceList.as_view()),
    url(r'^user/device/(?P<pk>[0-9]+)$', user_devices.UserDeviceDetail.as_view()),
    # DEVICE
    url(r'^device/?$', devices.DeviceList.as_view()),
    url(r'^device/(?P<pk>[0-9]+)$', devices.DeviceDetail.as_view()),
    # RECORD

    # AUTH
    # url(r'^auth/', include('rest_framework.urls')),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^auth/registration/', include('rest_auth.registration.urls')),
    url(r'^$', home.Home.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)