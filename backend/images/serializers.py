import base64
from rest_framework import serializers
from .models import ImageEntry

class ImageEntrySerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = ImageEntry
        fields = ['id', 'image', 'description', 'created_at']

    def get_image(self, obj):
        b64 = base64.b64encode(obj.image_data).decode('ascii')
        return f"data:{obj.mime_type};base64,{b64}"
