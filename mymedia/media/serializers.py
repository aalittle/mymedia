from rest_framework import serializers
from media.models import Medium

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medium
        fields = ('id', 'title', 'rating', 'is_complete', 'medium_type')