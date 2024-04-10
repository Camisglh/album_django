from io import BytesIO

from django.core.files.base import ContentFile
from PIL import Image

from celery import shared_task

from .models import Photo


@shared_task
def process_photo(photo_id):
    photo = Photo.objects.get(id=photo_id)
    img = Image.open(photo.image)
    img.thumbnail((800, 800))
    img = img.convert("RGB")
    thumb = BytesIO()
    img.save(thumb, "JPEG")
    thumb.seek(0)
    photo.image.save(
        f"{photo.image.name}_thumbnail.jpg", ContentFile(thumb.read()), save=False
    )
    photo.save()
