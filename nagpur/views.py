from django.shortcuts import render

# Create your views here.

def orange(request):
    return render(request,'orange.html')

def forest(request):
    return render(request,'forest.html')

