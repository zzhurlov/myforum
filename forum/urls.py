from django.urls import path
from forum import views


urlpatterns = [
    path("forum/", views.topic_list, name="forum"),
]
