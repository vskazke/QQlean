from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def indexlandingpage(request):
    return render(request, 'index-landingpage.html')

