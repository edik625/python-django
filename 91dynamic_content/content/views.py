from django.shortcuts import render

# Create your views here.
def index1(request):
    if request.method == 'POST':
        name = request.POST.get('text5', '')
        noun = request.POST.get('text1', '')
        verb = request.POST.get('text2', '')
        adjective = request.POST.get('text3', '')
        adverb = request.POST.get('text4', '')
        return render(request, 'content/index2.html', {'name': name, 'noun':noun, 'verb': verb, 'adverb': adverb, 'adjective': adjective})
    return render(request, 'content/index.html')