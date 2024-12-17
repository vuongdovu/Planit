from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_user, name="get_user"),
    path("create_user", views.create_user, name="create_user"),
]
