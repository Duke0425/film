from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse('OK')

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
