from django.urls import path
from .views import camera_feed

urlpatterns = [
    # The root path of this app will point to the camera feed
    path('', camera_feed, name='camera_feed'),
]