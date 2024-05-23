from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("createlisting/",views.createListing, name="createlisting"),
    path("login/", views.login_view, name="login"),
    path("displayvategory", views.displayCategory, name="displayvategory"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register")
]
