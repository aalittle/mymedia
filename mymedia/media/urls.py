from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from media import views
from django.conf.urls import include

urlpatterns = patterns('',
    url(r'^media/$', views.MediumList.as_view()),
    url(r'^media/(?P<pk>[0-9]+)/$', views.MediumDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
)
