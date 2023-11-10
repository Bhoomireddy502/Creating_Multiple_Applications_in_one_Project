from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sekhar(request):
    return render(request,'sekhar.html')
def sekhar1(request):
    return HttpResponse ('<h1><i>sekhar1 duplicate of sekhar</i></h1>')