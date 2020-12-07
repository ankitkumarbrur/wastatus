"""wastatus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from pages.views import home_view
from pages.views import qr_view
from pages.views import current_view
from pages.views import background_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('qr/', qr_view, name='qr'),
    path('screen/',current_view, name='screen'),
    path('tracking/',current_view, name='tracking'),
    path('back/',background_view, name='back')
]+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
