from media.models import Medium
from django.contrib.auth.models import User
from media.serializers import MediaSerializer, UserSerializer
from rest_framework import generics, permissions
from media.permissions import IsOwner
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
import logging
from rest_framework.authentication import OAuth2Authentication


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'media': reverse('medium-list', request=request, format=format)
    })

class UserList(generics.ListAPIView):
    model = User
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    model = User
    serializer_class = UserSerializer

class MediumList(generics.ListCreateAPIView):
    model = Medium
    serializer_class = MediaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwner,)
    
    def pre_save(self, obj):
        obj.owner = self.request.user
    
    def get_queryset(self):
        """
        Should return all the mediums owned by the requesting, authenticated user.
        """
        user = self.request.user
        return Medium.objects.filter(owner=user)
    
    
class MediumDetail(generics.RetrieveUpdateDestroyAPIView):

    # Unable to get OAuth2 working using the following two lines.
    #authentication_classes = (OAuth2Authentication,)
    #permission_classes = (permissions.TokenHasReadWriteScope,)

    model = Medium
    serializer_class = MediaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwner,)
    
    
    def pre_save(self, obj):
        obj.owner = self.request.user


