from rest_framework import serializers
from media.models import Medium
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    media = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'media')

class MediaSerializer(serializers.ModelSerializer):
    owner = serializers.Field(source='owner.username')
    
    class Meta:
        model = Medium
        fields = ('id', 'title', 'rating', 'is_complete', 'medium_type', 'owner')
        