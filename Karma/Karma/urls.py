from django.conf.urls import patterns, include, url
from django.contrib import admin
import Home.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Karma.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include(Home.urls)),
    url(r'^admin/', include(admin.site.urls)),

)
