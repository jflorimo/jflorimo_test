from django.conf.urls import url
from .views import devices, home

urlpatterns = [
    url(r'', home.main),
    url(r'^device/$', devices.device_list),
]