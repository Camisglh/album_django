from django.conf import settings
from django.db import models


class Photo(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(verbose_name="URL")
    image = models.ImageField(upload_to="images", verbose_name="Изображение")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, verbose_name="Категория"
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Фотографию"
        verbose_name_plural = "Фотографии"


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(verbose_name="URL")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
