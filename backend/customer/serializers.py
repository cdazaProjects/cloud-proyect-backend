from rest_framework import serializers
from .models import Customer, Contest, Video

class CustomerSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Customer
        fields='__all__'

class ContestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contest
        fields='__all__'

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Video
        fields='__all__'
        