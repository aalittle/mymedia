from media.models import Medium
from media.serializers import MediaSerializer
from rest_framework import generics

class MediumList(generics.ListCreateAPIView):
    model = Medium
    serializer_class = MediaSerializer
    
class MediumDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Medium
    serializer_class = MediaSerializer


