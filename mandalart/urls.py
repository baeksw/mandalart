
from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.urls import path
from django.urls.conf import include
from django.views.generic.base import RedirectView, TemplateView
from rest_framework import routers
from rest_framework.authtoken.models import Token
from rest_framework.documentation import include_docs_urls

from rest_framework.permissions import AllowAny

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include(('app.urls', 'app'), namespace='app')),
] 