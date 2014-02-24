from django.conf.urls import patterns, url

from sections import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index')
)
