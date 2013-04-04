from rest_framework import serializers
from media.models import Medium
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    media = serializers.HyperlinkedRelatedField(many=True, view_name='medium-detail')

    class Meta:
        model = User
        fields = ('url', 'username', 'media')

class MediaSerializer(serializers.ModelSerializer):
    owner = serializers.Field(source='owner.username')
    
    class Meta:
        model = Medium
        fields = ('id', 'title', 'rating', 'is_complete', 'medium_type', 'owner')
        