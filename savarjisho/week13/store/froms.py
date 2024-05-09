from django import forms
from .models import Order, Product, ProductCategory


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'