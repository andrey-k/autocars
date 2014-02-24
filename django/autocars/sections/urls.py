from django.conf.urls import patterns, url

from autocars.sections import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index')
)
