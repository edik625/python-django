from django.contrib import admin
from .models import Order,Product,ProductCategory
from django.utils.safestring import mark_safe
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','category', 'image_prevew')
    list_filter = ('category',)
    search_fields = ('name','category__name')

    def image_prevew(self,obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-widht:100px; max-height:100px;" />')
        else:
            return 'no image'
    image_prevew.short_description = 'Images'
admin.site.register(Product,ProductAdmin)
admin.site.register([Order,ProductCategory])
