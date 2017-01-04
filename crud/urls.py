from django.conf.urls import include, url
from django.contrib import admin
import cf_app

urlpatterns = [
    url(r'^cf_app/', include('cf_app.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include(cf_app.urls)),
]
