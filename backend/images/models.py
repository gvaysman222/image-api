from django.db import models

class ImageEntry(models.Model):
    mime_type    = models.CharField(max_length=50)         # e.g. "image/png"
    image_data   = models.BinaryField()                   # «сырые» байты
    description  = models.TextField()
    created_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'ImageEntry {self.id}'