import os

from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from app01.models import userInfo


def register(request):
    name = request.POST.get('username')
    passwd = request.POST.get('password')
    role = request.POST.get('role')
    users = userInfo.objects.filter(name=name)
    flag = False
    expect_name = ''
    for user in users:
        expect_name = user.name
    if expect_name:
        return JsonResponse({'status': 'exist'})
    else:
        userInfo.objects.create(name=name,password=passwd,role=role)
        return JsonResponse({'status': 'success'})

def login(request):
    name = request.POST.get('username')
    passwd = request.POST.get('password')
    users = userInfo.objects.filter(name=name)
    flag = False
    expect_name = ''
    for user in users:
        expect_name = user.name
        expect_passwd = user.password
        role = user.role
        if expect_passwd == passwd:
            flag=True
    if flag:
        return JsonResponse({'status': 'success','role':role})
    else:
        if expect_name:
            return JsonResponse({'status': 'unmatch'})
        else:
            return JsonResponse({'status': 'unregister'})

def editInfo(request):
    name = request.POST.get('username')
    username = request.POST.get('name')
    sex = request.POST.get('sex')
    info = request.POST.get('info')

    user = userInfo.objects.filter(name=name).first()
    user.username = username
    user.sex = sex
    user.info = info
    user.save()
    return JsonResponse({'status': 'success'})

def upload_image(request):
    # 图片对象
    file_obj = request.FILES.get('file')
    # 图片名字
    file_name = request.POST.get('fileName')
    username = request.POST.get('username')#账号名

    save_path = 'app01/static/' + file_name
    image_url = "http://127.0.0.1:8000/static/"+file_name
    # 使用文件系统存储对象进行保存
    fs = FileSystemStorage()
    fs.save(save_path, file_obj)

    user = userInfo.objects.filter(name=username).first()
    user.img = file_name
    user.save()
    # 返回图片保存路径给前端

    return JsonResponse({
        "file_name": file_name,
        'url': image_url})

def showInfo(request):
    name = request.POST.get('username')
    user = userInfo.objects.filter(name=name).first()

    return JsonResponse({'status': 'success','name':user.username,'sex':user.sex,'info':user.info,'img':"http://127.0.0.1:8000/static/"+user.img})


def changePasswwd(request):
    name = request.POST.get('username')
    passwd = request.POST.get('passwd')
    user = userInfo.objects.filter(name=name).first()
    user.password = passwd
    user.save()
    return JsonResponse({'status': 'success'})

def deleteUser(request):
    name = request.POST.get('username')
    user = userInfo.objects.filter(name=name).first()
    user.delete()
    return JsonResponse({'status': 'success'})