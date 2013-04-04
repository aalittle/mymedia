from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from media import views

urlpatterns = patterns('',
    url(r'^media/$', views.MediumList.as_view()),
    url(r'^media/(?P<pk>[0-9]+)/$', views.MediumDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)