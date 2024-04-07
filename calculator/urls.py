from django.urls import path
from .views import calculate_from,calculate_result,multiply,login_form,login


urlpatterns = [
    
    path("",login_form),
    path("login/",login),
    path("calculate_form/",calculate_from),
    path("calculate_form/result/",calculate_result),
    
    # path("result/", calculate_result ),
    # path("<int:num1>/<int:num2>",multiply),
] 
 