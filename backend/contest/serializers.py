from rest_framework import serializers
from .models import Contest, Video

class ContestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contest
        fields='__all__'

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Video
        fields='__all__'
        