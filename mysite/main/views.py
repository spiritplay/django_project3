from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def demo(request):
    return render(request, 'demo.html')

def archives(request):
    return render(request, 'archives.html')

def blog(request):
    return render(request, 'blog.html')

def single(request):
    return render(request, 'single.html')

def page(request):
    return render(request, 'page.html')
