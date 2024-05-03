from django.urls import path
from .views import index, event_info, add_event, delete_event, edit_event

urlpatterns =[
    path('', index, name='index'),
    path('info/<str:id>',event_info, name= 'event_info'),
    path('add_event',add_event,name='addevent'),
    path('delete/<int:title>',delete_event,name='delete'),
    path('edit/<str:title>',edit_event, name='edit')
]