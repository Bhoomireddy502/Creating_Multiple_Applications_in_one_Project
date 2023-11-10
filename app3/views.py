from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def reddy(request):
    return render(request,'reddy.html')
def reddy1(request):
    return HttpResponse ('<h1><i>reddy1 duplicate of sekhar</i></h1>')