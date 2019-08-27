"""Final_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import (url,
                              include)

from . import views as Main_views

from . import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
                  url(r'^admin/', admin.site.urls),

                  url(r'^$', Main_views.index, name='home'),

                  url(r'^About/', include('About.urls')),

                  url(r'^blog/', include('Blog.urls')),

                  url(r'^service/', include('Service.urls')),

                  url(r'^Contact/', include('Contact.urls')),

                  # url(r'^login/', include('User.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
