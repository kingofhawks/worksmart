from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'worksmart.views.home', name='home'),
    url(r'^bug/', include('bug.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
