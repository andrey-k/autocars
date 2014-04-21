from django.conf.urls import patterns, url

from sections import views

urlpatterns = patterns(
    '',
    url(r'^contact/', views.contact, name='contact_url'),
    url(r'^$', views.index, name='index'),
)
