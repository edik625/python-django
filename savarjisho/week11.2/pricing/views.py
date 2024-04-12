from django.shortcuts import render

# Create your views here.
def pricing_plane(request):
    data =[
        {"name": 'Basic', 'price': '$10/month'},
        {'name': 'Standart', 'price': '$20/month'},
        {'name': 'Premium', 'price': '$30/month'},
    ]
    return render(request, 'pricing/index.html', {'data': data})