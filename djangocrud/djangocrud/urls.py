from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/',include('api.urls')),
    url(r'',include('api.urls')),
    url(r'^rest_framework',include('rest_framework.urls', namespace='rest_framework'))
]


