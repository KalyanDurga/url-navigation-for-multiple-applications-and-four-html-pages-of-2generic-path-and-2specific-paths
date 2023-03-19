from django.shortcuts import render

# Create your views here.

def encapsulation(request):
    return render(request,'encapsulation.html')
def inheritance(request):
    return render(request,'inheritance.html')