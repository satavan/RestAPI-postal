"""postal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns,include, url
from django.contrib import admin
from indpostal.views import PosViewSet
from indpostal.views import PoseingViewset




urlpatterns =patterns('',
   url(r'^admin/', include(admin.site.urls)),
   #url(r'^import_db','indpostal.views.import_db',name='import'),
   url(r'^retrive/',PosViewSet.as_view(),name='retrive'),
   url(r'^display/(?P<x>.+)/$',PoseingViewset.as_view()),

)
