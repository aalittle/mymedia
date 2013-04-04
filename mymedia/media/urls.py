from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from media import views
from django.conf.urls import include

urlpatterns = format_suffix_patterns(patterns('media.views',
    url(r'^$', 'api_root'),
    url(r'^media/$',
        views.MediumList.as_view(),
        name='medium-list'),
    url(r'^media/(?P<pk>[0-9]+)/$',
        views.MediumDetail.as_view(),
        name='medium-detail'),
    url(r'^users/$',
        views.UserList.as_view(),
        name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name='user-detail')
))


urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
)
