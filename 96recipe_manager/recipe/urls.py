from django.urls import path
from .views import index, add_recipe, info, delete, edit

urlpatterns = [
    path('',index, name='index'),
    path('add/',add_recipe, name='add_recipe'),
    path('info/<str:name>', info, name='info_recipe'),
    path('delete/<str:name>', delete, name='delete'),
    path('edit/<str:name>', edit, name='edit')
]
