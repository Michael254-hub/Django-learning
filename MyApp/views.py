from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'index.html')
def services(request):
    return render(request,'services.html')
def about(request):
    return render(request,'about.html')
def blog(request):
    return render(request,'blog.html')
def contacts (request):
    return render(request,'contacts.html')