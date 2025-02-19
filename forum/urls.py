from django.urls import path
from forum import views


urlpatterns = [
    path("", views.topic_list, name="topics"),
]
