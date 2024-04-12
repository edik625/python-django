from django.shortcuts import render
import requests
# Create your views here.
def ip_tracker(request):
    if request.method == 'POST':
        ip = request.POST.get("ip", '')
        data = get_ip_info(ip) 
        return render(request, 'iptracker/result.html', {'data': data})
    return render(request,'iptracker/from.html')

def get_ip_info(ip_address):
    url= f'https://ipinfo.io/{ip_address}/json'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {'error': 'something was wrong'}
    