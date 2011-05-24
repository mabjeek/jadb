from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib.auth import views as auth_views

admin.autodiscover()

urlpatterns = patterns('',
    (r'^accounts/login', auth_views.login),
    (r'^accounts/logout', auth_views.logout),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)
