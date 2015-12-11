from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index_name'),
    url(r'^about/$', views.about, name='about_name'),
)
