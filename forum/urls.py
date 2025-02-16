from django.urls import path
from forum import views


urlpatterns = [
    path("main/", views.fff, name="main"),
]
