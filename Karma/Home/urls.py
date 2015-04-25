from django.conf.urls import patterns,include, url
from Home.views import *

urlpatterns = patterns('',

    # Main Page
    url(r'^$', main_page),

)
