from django.conf import settings
from django.db import models


class Photo(models.Model):
    """
    Model for photos
    """

    name = models.CharField(max_length=100, verbose_name="Name")
    slug = models.SlugField(verbose_name="URL")
    image = models.ImageField(upload_to="images", verbose_name="Image")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, verbose_name="Category"
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Photo"
        verbose_name_plural = "Photos"


class Category(models.Model):
    """
    Categories for photos
    """

    name = models.CharField(max_length=100, verbose_name="Name")
    slug = models.SlugField(verbose_name="URL")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Category"
        verbose_name_plural = "Categories"
