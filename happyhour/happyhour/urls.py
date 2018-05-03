"""happyhour URL Configuration

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
from django.conf.urls import url
from django.urls import path, re_path, include

from django.views.generic.base import RedirectView
favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

import hh.views as hhv

urlpatterns = [
    path('favicon.ico', favicon_view),
    path('', hhv.index, name='index'),
    path('bars/', hhv.all_bars, name='all_bars'),
    path('about/', hhv.about, name='about'),
    #url(r'^$', hhv.index, name='index'),
    #url(r'bars/$', hhv.all_bars, name='all_bars'),
    #url(r'about/', hhv.about, name='about'),
    path('bars/<slug:slug>/', hhv.barView, name='bar'),
    path('admin/', admin.site.urls),
    path('accounts/profile/', hhv.userProfileView, name='userprofile'),
    path('accounts/', include('allauth.urls')),
    path('api/bars/', hhv.BarListCreate.as_view() ),
    path('api/happyhours/', hhv.HHListCreate.as_view() ),
    # Match api/map/-23.32145/23.12345/ Minus optional. Before dot 2-3 digits
    re_path(r'^api/map/bars/(?P<latN>-?\d{2,3}\.\d{5})/(?P<lngW>-?\d{2,3}\.\d{5})/(?P<latS>-?\d{2,3}\.\d{5})/(?P<lngE>-?\d{2,3}\.\d{5})/$', hhv.MapBarListCreate.as_view() ),
    path('map/', hhv.map, name='mapdemo'),
    path('dataviz', hhv.dataviz, name='dataviz'),
    #url(r'^accounts/profile/$', hhv.userProfileView, name='userprofile'),
    #url(r'^accounts/', include('allauth.urls')),
    #url(r'^api/bars', hhv.BarListCreate.as_view() ),
    #url(r'^map/', hhv.map, name="mapdemo"),
]
