from django.urls import path

from . import views  # pylint: disable=relative-beyond-top-level

urlpatterns = [
    path("", views.index, name="index"),
]
