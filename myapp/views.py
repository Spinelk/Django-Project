from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return render(request, 'myapp/index.html')

def about(request):
    return render(request, 'myapp/about.html')