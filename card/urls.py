from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = "card"
urlpatterns = [
    path("", views.home, name="home"),
    path("add-photo/", views.add_photo, name="add-photo"),
    path("<slug:category_slug>/", views.home, name="home_category"),
    path("edit/<slug:photo_id>/", views.edit_photo, name="edit_photo"),
    path("delete/<slug:photo_id>/", views.delete_photo, name="delete_photo"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
