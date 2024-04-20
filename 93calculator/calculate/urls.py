from django.urls import path
from .views import calculator, add_veb, subtract_veb, multiply_veb, divide_veb


urlpatterns = [
    path('',calculator, name='calculator' ),
    path('add/', add_veb, name='add'),
    path('subtract/', subtract_veb, name='subtract'),
    path('multiply/', multiply_veb, name='multiply'),
    path('divide/', divide_veb, name='divide'),
]
