"""hack-server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from webreceiver.views import submit, index, submit2, load

urlpatterns = [
    path('admin/', admin.site.urls),
    path('submit', submit, name='reversefingerprint'),
    path('submit2', submit2, name='submit2print'),
    path('load', load, name='load2print'),
    path('', index, name='index'),
]
