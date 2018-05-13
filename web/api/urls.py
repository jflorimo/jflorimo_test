from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import devices, home, users, user_devices, upload, records, record_data, download

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
    url(r'^record/?$', records.RecordList.as_view()),
    url(r'^record/(?P<pk>[0-9]+)$', records.RecordDetail.as_view()),
    # RECORD DATA
    url(r'^record/data/?$', record_data.RecordDataList.as_view()),
    url(r'^record/data/(?P<pk>[0-9]+)$', record_data.RecordDataDetail.as_view()),
    url(r'^record/data/record_id/(?P<pk>[0-9]+)$', record_data.RecordFileRecordData.as_view()),
    # UPLOAD
    url(r'^upload/?$', upload.Upload.as_view()),
    url(r'^download/?$', download.Download.as_view()),
    # AUTH
    # url(r'^auth/', include('rest_framework.urls')),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^auth/registration/', include('rest_auth.registration.urls')),
    # MEDIA
    url(r'^$', home.Home.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)