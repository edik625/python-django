from django.urls import path
from .views import index ,start_app,dina,dina2,index1,show_items
urlpatterns = [
    path("",index),
    path("start/",start_app),
    path("dinamiuri/<int:id>",dina),
    path("dinamiuri1/<str:id>",dina2),
    path("list",index1),
    path("list/<int:id>",show_items),
]