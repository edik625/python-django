from django.urls import path
from .views import index,  myclass, myclass2, test_redirect
urlpatterns = [
    path('' , index) ,
    path('test/' , test_redirect, name='reddir') ,
    path('class1/' , myclass) ,
    path('class/<int:id>' , myclass2) ,
]
