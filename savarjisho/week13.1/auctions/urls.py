from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("createlisting/",views.createListing, name="createlisting"),
    path("login/", views.login_view, name="login"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("listing/<int:id>",views.listing, name="listing"),
    path("removewatchlist/<int:id>", views.removewatchlist, name="removewatchlist"),
    path("addwatchlist/<int:id>", views.addwatchlist, name="addwatchlist"),
    path("displayvategory", views.displayCategory, name="displaycategory"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register")
]
