from rest_framework import serializers
from fileUpLoad.models import Media

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ['user', 'mudia', 'title', 'uploaded_at']