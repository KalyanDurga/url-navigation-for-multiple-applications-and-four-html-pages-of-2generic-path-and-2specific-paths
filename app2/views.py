from django.shortcuts import render

# Create your views here.

def polymorphisum(request):
    return render(request,'polymorphisum.html')

def abstraction(request):
    return render(request,'abstraction.html')
