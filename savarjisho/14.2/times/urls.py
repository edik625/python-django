from .views import TimesView
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'times', TimesView)


urlpatterns = [
    path('', include(router.urls)),
]