from django.conf.urls.defaults import *

urlpatterns = patterns('jadb.accounts.views',
	(r'login$', 'login'),
)