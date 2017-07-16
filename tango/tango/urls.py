"""
Definition of urls for tango.
"""

from django.conf.urls import include, url
from rango import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^rango/', include('rango.urls')),
    # url(r'^$', tango.views.home, name='home'),
    # url(r'^tango/', include('tango.tango.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
]
