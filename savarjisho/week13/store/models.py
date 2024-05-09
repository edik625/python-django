from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)


    class Meta:
        verbose_name_plural = "Category"    
    
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/')

    class Meta:
        verbose_name_plural = "Product"   

    def __str__(self):
        return self.name
    
class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    datee_order = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Order"   

    def __str__(self):
        return f"Order for {self.product.name}"
