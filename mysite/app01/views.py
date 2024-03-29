from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from app01.models import userInfo


def register(request):
    name = request.POST.get('username')
    passwd = request.POST.get('password')
    print(name)
    userInfo.objects.create(name=name,password=passwd,role=1)
    return JsonResponse({'status': 'success', 'exist': "yes"})
