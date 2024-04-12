from django.urls import path
from .views import ip_tracker

urlpatterns = [
    path('', ip_tracker)
]


