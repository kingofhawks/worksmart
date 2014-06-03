from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'worksmart.views.home', name='home'),
    url(r'^$', 'worksmart.bug.views', name='trend'),
)
