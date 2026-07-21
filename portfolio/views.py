from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'portfolio/index.html')

def projects(request):
    return render(request, 'portfolio/projects.html')

def about(request):
    return render(request, 'portfolio/about.html')

def resume(request):
    return render(request, 'portfolio/resume.html')

def contact(request):
    return render(request, 'portfolio/contact.html')