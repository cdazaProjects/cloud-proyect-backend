from rest_framework import serializers
from video_encoding.models import Format

from .models import Contest, Video

class ContestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contest
        fields='__all__'


class FormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Format
        fields='__all__'


class VideoSerializer(serializers.ModelSerializer):
    contest = ContestSerializer()
    format_set = FormatSerializer(many=True)
    class Meta:
        model=Video
        fields='__all__'
        