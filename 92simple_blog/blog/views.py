from django.shortcuts import render

# Create your views here.
def index1(request):
    blog = [
        {'satauri': 'blog1', 'text': 'imyofebi pirvel blogze', 'avtori': 'nika davitadze'},
        {'satauri': 'blog2', 'text': 'imyofebi meore blogze', 'avtori': 'giorgi beridze'},
        {'satauri': 'blog3', 'text': 'imyofebi mesame blogze', 'avtori': 'davit yifiani'},
        {'satauri': 'blog4', 'text': 'imyofebi meotxe blogze', 'avtori': 'jaba maxaradze'}
        ]
    return render(request, 'blog/blog.html', {'blog': blog})