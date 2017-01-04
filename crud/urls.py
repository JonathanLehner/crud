from django.conf.urls import include, url
from django.contrib import admin
import crud_app

urlpatterns = [
    url(r'^crud_app/', include('crud_app.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include(crud_app.urls)),
]
