from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('media.views',
    url(r'^media/$', 'medium_list'),
    url(r'^media/(?P<pk>[0-9]+)$', 'medium_detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns)