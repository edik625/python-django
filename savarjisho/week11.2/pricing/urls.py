from django.urls import path
from .views import pricing_plane

urlpatterns = [
    path('', pricing_plane)
]
