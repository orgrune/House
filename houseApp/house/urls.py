from django.conf.urls import url
from django.urls import include, path

urlpatterns = [
    url(r'^api/', include('fileUpload.urls')),
]
