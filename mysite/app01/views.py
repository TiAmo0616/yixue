import os
from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from app01.models import userInfo

from app01.models import Course
import uuid

from app01.models import Work

from app01.models import w_c

from app01.models import sc

from app01.models import w_s


def generate_course_code(index):
    course_code = str(uuid.uuid4().hex)[:index]  # 生成一个32位的UUID，并截取前8位作为课程码
    return course_code

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

#显示一个具体课程
def showCourse(request):
    cid = request.POST.get('cid')
    course = Course.objects.filter(cid=cid).first()
    temp = {}
    temp['cname'] = course.cname
    temp['img'] = "http://127.0.0.1:8000/static/" + course.img
    temp['stuNum'] = course.stuNum
    temp['xueshi'] = course.xueshi
    temp['status'] = course.status

    return JsonResponse({'status': 'success','course':temp})

#精选课程
def listCourses(request):
    res = []
    courses = Course.objects.all()
    for course in courses:
        if len(res)<8 and course.status=='进行中':
            temp = {}
            temp['cid'] = course.cid
            temp['cname']= course.cname
            temp['img'] =  "http://127.0.0.1:8000/static/"+course.img
            temp['teacher'] = course.teacher
            temp['status'] = course.status
            res.append(temp)
        if len(res)>=8:
            break
    return JsonResponse({'status':'success','courses':res})

#展示所有课程
def listCoursesAll(request):
    res = []
    courses = Course.objects.all()
    for course in courses:
        temp = {}
        temp['cid'] = course.cid
        temp['cname']= course.cname
        temp['img'] =  "http://127.0.0.1:8000/static/"+course.img
        temp['status'] = course.status
        res.append(temp)
    return JsonResponse({'status':'success','courses':res})

#创建课程
def createCourses(request):
    # current_date = datetime.now().date()
    course = Course()
    username = request.POST.get('username')
    cname = request.POST.get('cname')
    xueshi = request.POST.get('xueshi')
    teacher = request.POST.get('teacher')
    introduction = request.POST.get('introduction')
    # 图片对象
    file_obj = request.FILES.get('file')
    # 图片名字
    file_name = request.POST.get('fileName')
    save_path = 'app01/static/' + file_name
    image_url = "http://127.0.0.1:8000/static/" + file_name
    # 使用文件系统存储对象进行保存
    fs = FileSystemStorage()
    fs.save(save_path, file_obj)

    # course.createdate = current_date
    course.username = username
    course.cname = cname
    course.img = file_name
    course.cid = generate_course_code(8)
    course.xueshi = xueshi
    course.introduction = introduction
    course.teacher = teacher
    course.save()

    courses = Course.objects.filter(username=username)
    res = []
    for course in courses:
        temp = {}
        temp['cid'] = course.cid
        temp['cname'] = course.cname
        temp['img'] = "http://127.0.0.1:8000/static/" + course.img
        temp['stuNum'] = course.stuNum
        temp['xueshi'] = course.xueshi
        temp['status'] = course.status
        res.append(temp)
    return JsonResponse({'status': 'success', 'courses': res})

#教师端加载我的课堂
def teacherCourses(request):
    username = request.POST.get('username')
    courses = Course.objects.filter(username=username)
    res=[]
    for course in courses:
        temp = {}
        temp['cid'] = course.cid
        temp['cname'] = course.cname
        temp['img'] = "http://127.0.0.1:8000/static/"+ course.img
        temp['stuNum'] = course.stuNum
        temp['xueshi'] = course.xueshi
        temp['status'] = course.status
        res.append(temp)
    return JsonResponse({'status': 'success', 'courses': res})

# 结束课程
def closeCourse(request):
    cid = request.POST.get('cid')
    username = request.POST.get('username')
    course = Course.objects.filter(cid=cid).first()
    course.status = '已结束'
    cname = course.cname
    course.save()
    courses = Course.objects.filter(username=username)
    res = []
    for course in courses:
        temp = {}
        temp['cid'] = course.cid
        temp['cname'] = course.cname
        temp['img'] = "http://127.0.0.1:8000/static/" + course.img
        temp['stuNum'] = course.stuNum
        temp['xueshi'] = course.xueshi
        temp['status'] = course.status
        res.append(temp)
    return JsonResponse({'status': 'success', 'courses': res,'cname':cname})

def listing(request):
    username = request.POST.get('username')
    s = request.POST.get('s')
    courses = Course.objects.filter(username=username)
    res = []
    ing=[]
    finish=[]
    for course in courses:
        temp = {}
        temp['cid'] = course.cid
        temp['cname'] = course.cname
        temp['img'] = "http://127.0.0.1:8000/static/" + course.img
        temp['stuNum'] = course.stuNum
        temp['xueshi'] = course.xueshi
        temp['status'] = course.status
        if course.status == '进行中':
            ing.append(temp)
            res.append(temp)
        else:
            finish.append(temp)
            res.append(temp)
    if s=='进行中':
        return JsonResponse({'status': 'success', 'courses': ing})
    elif s == '已结束':
        return JsonResponse({'status': 'success', 'courses': finish})
    else:
        return JsonResponse({'status': 'success', 'courses': res})


def createWork(request):
    cid = request.POST.get('cid')
    wname = request.POST.get('wname')
    begin = request.POST.get('begin')
    end = request.POST.get('end')
    wid = generate_course_code(12)
    work = Work()
    work.wname = wname
    work.wid = wid
    work.begin = begin
    work.end = end
    work.save()

    conn = w_c()
    conn.cid = cid
    conn.wid = wid
    conn.save()

    #发布给学生
    students = sc.objects.filter(cid=cid)
    for student in students:
        name = student.stuName
        ws= w_s()
        ws.wid = wid
        ws.name = name
        ws.save()


    res = searchWork(cid)

    return JsonResponse({'status': 'success', 'works': res})


def searchWork(cid):
    works = w_c.objects.filter(cid=cid)
    res=[]
    for work in works:
        temp={}
        if work.cid == cid:
            wid = work.wid
            ws = Work.objects.filter(wid=wid).first()

            temp['wname'] = ws.wname
            temp['begin'] = ws.begin
            temp['end'] = ws.end
            res.append(temp)
    return res

def showWorks(request):
    cid = request.POST.get('cid')
    res = searchWork(cid)
    return JsonResponse({'status': 'success', 'works': res})