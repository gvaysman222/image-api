import base64
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import ImageEntry
from .serializers import ImageEntrySerializer

class ImageEntryViewSet(viewsets.ModelViewSet):
    queryset = ImageEntry.objects.all().order_by('-created_at')
    serializer_class = ImageEntrySerializer

    def create(self, request, *args, **kwargs):
        img_data = request.data['image']       # "data:image/png;base64,AAA..."
        desc     = request.data['description']

        header, b64 = img_data.split(';base64,')
        mime_type   = header.split(':', 1)[1]  # "image/png"
        binary      = base64.b64decode(b64)

        entry = ImageEntry.objects.create(
            mime_type   = mime_type,
            image_data  = binary,
            description = desc
        )
        serializer = self.get_serializer(entry)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
