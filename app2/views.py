from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def bhoomi(request):
    return render(request,'bhoomi.html')

def bhoomi1(request):
    return HttpResponse ('<h1><i>bhoomi1 duplicate of sekhar</i></h1>')