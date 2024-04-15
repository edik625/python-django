from django.urls import path
from .views import index1, home_veb, about_veb, contact_veb

urlpatterns = [
    path('page/', index1, name='page'), 
    path('home/', home_veb, name='home'),
    path('about/', about_veb, name='about'),
    path('contact/', contact_veb, name='contact'),
]
