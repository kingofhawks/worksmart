from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'worksmart.views.home', name='home'),
    url(r'^$', views.trend, name='trend'),
    url(r'^trend_data/$', views.trend_data, name='trend_data'),
    url(r'^percentage/$', views.percentage, name='percentage'),
    url(r'^percentage_data/$', views.percentage_data, name='percentage_data'),
)
