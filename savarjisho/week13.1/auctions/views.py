from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from .models import User,Listing,Category,Comment,Bid


def index(request):
    allitems = Listing.objects.filter(isactive = True)
    allcategory = Category.objects.all()
    return render(request, "auctions/index.html", {'activeitems': allitems, "category":allcategory})


def createListing(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        imageURL = request.POST["imageURL"]
        price = request.POST["price"]
        category = request.POST["category"]
        currentUser = request.user
        currentCategory = Category.objects.get(categoryName=category)
        bid = Bid(bid = float(price), user=currentUser)
        bid.save()
        newListing = Listing(
            title = title,
            description = description,
            imageurl = imageURL,
            price = bid,
            owner =currentUser,
            category = currentCategory,
            )
        newListing.save()
        return redirect("index")
    categoryData = Category.objects.all()
    return render(request,"auctions/created.html",{"categories":categoryData})


def displayCategory(request):
    if request.method == "POST":
        currentCategory = request.POST["category"]
        category = Category.objects.get(categoryName = currentCategory)
        filteredItems = Listing.objects.filter(isActive = True,category=category)
        allcategories = Category.objects.all()
        return render(request,"auctions/index.html", {'activeitems': filteredItems, "categories":allcategories})

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
