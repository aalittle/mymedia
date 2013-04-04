from media.models import Medium
from django.contrib.auth.models import User
from media.serializers import MediaSerializer, UserSerializer
from rest_framework import generics, permissions


class UserList(generics.ListAPIView):
    model = User
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    model = User
    serializer_class = UserSerializer

class MediumList(generics.ListCreateAPIView):
    model = Medium
    serializer_class = MediaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def pre_save(self, obj):
        obj.owner = self.request.user
    
class MediumDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Medium
    serializer_class = MediaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def pre_save(self, obj):
        obj.owner = self.request.user


