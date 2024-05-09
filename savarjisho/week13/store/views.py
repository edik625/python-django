from django.shortcuts import render, redirect
from .froms import ProductForm
from .models import Product
# Create your views here.
def product_list(request):
    product = Product.objects.all()
    return render(request, 'index.html',{'product':product})

def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form= ProductForm()
    return render(request, 'add_product.html', {'form':form})


def update_product_detail(request,id):
    product = Product.objects.get(pk=id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'add_product.html', {'form':form})