from django.conf.urls import url, include
from django.contrib import admin

from creds import urls as cred_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(cred_urls)),
    url(r'^rest-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
