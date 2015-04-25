from django.conf.urls import patterns,include, url
from Home.views import *

urlpatterns = patterns('',

    # Main Page
    url(r'^$', main_page),

    # Auth urls for login/out, password change/reset
    url('^', include('django.contrib.auth.urls'))



)
