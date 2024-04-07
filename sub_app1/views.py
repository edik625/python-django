from django.http import HttpResponse

def index(request):
    return HttpResponse("sub aplications 1")

def start_app(request):
    init_string= ""
    # name = input("gamarjoba ")
    for i in range(10):
        for j in range(10):
            string = f"<li>{i} * {j} = {i*j}</li>"
            init_string += string
    return HttpResponse(f"<ul> {init_string}</ul>")
def dina(request,id):
    return HttpResponse(f"hellow {id+21}")

def dina2(request,id):
    return HttpResponse(f'gamarjoba {id})')

items =["Apple","Banana","Fruits","Orange"]
def index1(request):
    new_items = "<br>".join(items)
    return HttpResponse(f"Items: <br>{new_items}")


def show_items(request,id):
    try:
        return HttpResponse(f"selected {items[id-1]}")
    except:
        return HttpResponse("wrong id")