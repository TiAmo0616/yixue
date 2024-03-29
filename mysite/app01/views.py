from django.shortcuts import render

# Create your views here.

from models import userInfo

def register(request):
    name = request.POST.get('username')
    passwd = request.POST.get('password')
