from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
from django.conf import settings


urlpatterns = [
    path('admin', admin.site.urls),
    path('', include('hundred.urls')),
]
