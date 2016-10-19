from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v0/', include('apps.api_v0.urls')),
    url(r'^', include('apps.base.urls')),
]
