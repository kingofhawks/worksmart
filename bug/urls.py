from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'worksmart.views.home', name='home'),
    url(r'^$', views.trend, name='trend'),
    url(r'^trend_data/$', views.trend_data, name='trend_data'),
)
