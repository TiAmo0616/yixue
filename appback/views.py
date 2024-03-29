from django.shortcuts import render

# Create your views here.

def register(request):
    name = request.POST.get('username')
    passwd = request.POST.get('password')