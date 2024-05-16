from django.urls import path
from .views import user_login, user_registration, user_logout 
urlpatterns = [
    path("", user_login, name="login"),
    path("register/", user_registration, name="registration"),
    path('logout/', user_logout, name='logout'),
]
