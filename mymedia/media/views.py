from media.models import Medium
from django.contrib.auth.models import User
from media.serializers import MediaSerializer, UserSerializer
from rest_framework import generics, permissions
from media.permissions import IsOwner
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

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
    
class MediumDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Medium
    serializer_class = MediaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwner,)
    
    def pre_save(self, obj):
        obj.owner = self.request.user


