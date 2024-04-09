from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = "card"
urlpatterns = [
    path("", views.home, name="home"),
    path("<slug:category_slug>/", views.home, name="home_category"),
    path("add-photo/", views.add_photo, name="add-photo"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
