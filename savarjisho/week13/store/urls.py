from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import product_list, product_create, update_product_detail
urlpatterns = [
    path('', product_list, name='product_list'),
    path('add_product/', product_create, name='product_create'),
    path('edit_product/<int:id>', update_product_detail, name="edit_product")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)