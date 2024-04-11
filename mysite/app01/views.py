import json
import os
from datetime import datetime, timedelta

from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from app01.models import userInfo

from app01.models import Course
import uuid

from app01.models import Work


from app01.models import sc

from app01.models import w_s

from app01.models import question

from app01.models import s_q


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
    username = request.POST.get('username')
    course = Course.objects.filter(cid=cid).first()
    students = sc.objects.filter(cid=cid)
    temp = {}
    temp['already'] = 0
    for student in students:
        if student.stuName == username:
            temp['already'] = 1
            break

    temp['cname'] = course.cname
    temp['img'] = "http://127.0.0.1:8000/static/" + course.img
    temp['stuNum'] = len(students)
    temp['xueshi'] = course.xueshi
    temp['status'] = course.status
    temp['teacher'] = course.teacher
    temp['introduction'] = course.introduction

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
        temp['teacher'] = course.teacher
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
        students = sc.objects.filter(cid=course.cid)
        temp['cid'] = course.cid
        temp['cname'] = course.cname
        temp['img'] = "http://127.0.0.1:8000/static/" + course.img
        temp['stuNum'] = len(students)
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
        students = sc.objects.filter(cid=course.cid)
        temp['cid'] = course.cid
        temp['cname'] = course.cname
        temp['img'] = "http://127.0.0.1:8000/static/"+ course.img
        temp['stuNum'] = len(students)
        temp['xueshi'] = course.xueshi
        temp['status'] = course.status
        res.append(temp)
    return JsonResponse({'status': 'success', 'courses': res})

def searchCourse(cid):
    course = Course.objects.filter(cid=cid).first()
    temp = {}
    students = sc.objects.filter(cid=cid)
    temp['cid'] = course.cid
    temp['cname'] = course.cname
    temp['img'] = "http://127.0.0.1:8000/static/" + course.img
    temp['stuNum'] = len(students)
    temp['xueshi'] = course.xueshi
    temp['status'] = course.status
    return temp


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
        students = sc.objects.filter(cid=course.cid)
        temp['cid'] = course.cid
        temp['cname'] = course.cname
        temp['img'] = "http://127.0.0.1:8000/static/" + course.img
        temp['stuNum'] = len(students)
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
        students = sc.objects.filter(cid=course.cid)
        temp['stuNum'] = len(students)
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
    work.cid = cid
    work.save()

    #
    #
    # #发布给学生
    # students = sc.objects.filter(cid=cid)
    # for student in students:
    #     name = student.stuName
    #     ws= w_s()
    #     ws.wid = wid
    #     ws.name = name
    #     ws.save()


    res = searchWork(cid,'all')

    return JsonResponse({'status': 'success', 'works': res})

def checking(begin,end):
    now = datetime.now()
    begin = datetime.strptime(begin,"%Y-%m-%d %H:%M:%S")
    end = datetime.strptime(end,"%Y-%m-%d %H:%M:%S")

    if now>end:
        return False
    else:
        return True

def searchWork(cid,status):

    works = Work.objects.filter(cid=cid)
    res=[]
    ings = []
    eds = []
    for work in works:
        temp={}
        temp['wid'] = work.wid
        temp['wname'] = work.wname
        temp['begin'] = work.begin
        temp['end'] = work.end
        res.append(temp)
        if checking(work.begin,work.end):
            ings.append(temp)
        else:
            eds.append(temp)
    if status == 'ing':
        return  ings
    elif status == 'ed':
        return eds
    return res

def showWorks(request):
    cid = request.POST.get('cid')
    status = request.POST.get('status')
    res = searchWork(cid,status)
    return JsonResponse({'status': 'success', 'works': res})

def deleteWork(request):
    wid = request.POST.get('wid')
    work = Work.objects.filter(wid = wid).first()
    cid = work.cid
    work.delete()

    students = w_s.objects.filter(wid = wid)
    for student in students:
        student.delete()

    res = searchWork(cid,'all')
    return JsonResponse({'status': 'success', 'works': res})


def saveq(request):
    q = question()
    qid = generate_course_code(20)
    wid = request.POST.get('wid')
    info = request.POST.get('info')
    qname = request.POST.get('qname')
    q_ans = request.POST.get('ans')
    kind = request.POST.get('kind')
    score = request.POST.get('score')
    if kind == '1':
        kind = '单选题'
        if q_ans == '1':
            q_ans = 'A'
        elif q_ans == '2':
            q_ans = 'B'
        elif q_ans == '3':
            q_ans = 'C'
        else:
            q_ans = 'D'
    elif kind == '2':
        kind = '判断题'
        if q_ans == '1':
            q_ans = '正确'
        else:
            q_ans = '错误'
    elif kind == '3':
        kind = '填空题'
    else:
        kind = '简答题'
    a = request.POST.get('a')
    b = request.POST.get('b')
    c = request.POST.get('c')
    d = request.POST.get('d')
    q.qid = qid
    q.wid = wid
    q.info = info
    q.qname = qname
    q.q_ans = q_ans
    q.kind = kind
    q.a = a
    q.b = b
    q.c = c
    q.d = d
    q.score = score
    q.save()

    return JsonResponse({'status': 'success'})

def showQuestions(request):
    wid = request.POST.get('wid')
    res = searchq(wid)
    return JsonResponse({'status': 'success', 'qs': res})

def searchq(wid):
    questions = question.objects.filter(wid=wid)
    res = []
    for q in questions:
        temp = {}
        temp['qid'] = q.qid
        temp['qname'] = q.qname
        temp['info'] = q.info
        temp['ans'] = q.q_ans
        temp['kind'] = q.kind
        temp['a'] = q.a
        temp['b'] = q.b
        temp['c'] = q.c
        temp['d'] = q.d
        temp['score'] = q.score
        res.append(temp)
    res.sort(key=lambda x: x['qname'])
    return res

def deleteq(request):
    qid = request.POST.get('qid')
    wid = request.POST.get('wid')
    print(qid)
    q = question.objects.filter(qid=qid).first()
    q.delete()

    res = searchq(wid)

    return JsonResponse({'status': 'success', 'qs': res})


def showtotalans(request):
    wid = request.POST.get('wid')
    students = w_s.objects.filter(wid=wid)
    alreadysubmit = 0
    res=[]
    for student in students:
        temp={}
        if student.status == '已提交':
            alreadysubmit+=1
            temp['name'] = student.name
            temp['t'] = student.t
            res.append(temp)
    noal = len(students) - alreadysubmit
    return JsonResponse({'status': 'success', 'res': res,'al':alreadysubmit,'noal':noal})

def pickCourse(request):
    cid = request.POST.get('cid')
    username = request.POST.get('username')

    conn = sc()
    conn.cid = cid
    conn.stuName = username
    conn.save()

    course = searchCourse(cid)
    return JsonResponse({'status': 'success','course':course})


def studentCourses(request):
    username = request.POST.get('username')
    courses = sc.objects.filter(stuName=username)
    res=[]
    for i in courses:
        course = Course.objects.filter(cid = i.cid).first()
        temp = {}
        temp['cid'] = course.cid
        temp['cname'] = course.cname
        temp['img'] = "http://127.0.0.1:8000/static/"+ course.img
        temp['xueshi'] = course.xueshi
        temp['status'] = course.status
        res.append(temp)
    return JsonResponse({'status': 'success', 'courses': res})

def exitCourse(request):
    username = request.POST.get('username')
    cid = request.POST.get('cid')
    conn = sc.objects.filter(stuName = username)
    for con in conn:
        if con.cid == cid:
            con.delete()
            break
    courses = sc.objects.filter(stuName=username)
    res = []
    for i in courses:
        course = Course.objects.filter(cid=i.cid).first()
        temp = {}
        temp['cid'] = course.cid
        temp['cname'] = course.cname
        temp['img'] = "http://127.0.0.1:8000/static/" + course.img
        temp['xueshi'] = course.xueshi
        temp['status'] = course.status
        res.append(temp)
    return JsonResponse({'status': 'success', 'courses': res})

def listMyCourses(request):
    username = request.POST.get('username')
    s = request.POST.get('s')
    cids = sc.objects.filter(stuName=username)
    res = []
    ing = []
    finish = []
    for cid in cids:
        course = Course.objects.filter(cid = cid.cid).first()
        temp = {}
        temp['cid'] = course.cid
        temp['cname'] = course.cname
        temp['img'] = "http://127.0.0.1:8000/static/" + course.img
        temp['xueshi'] = course.xueshi
        temp['status'] = course.status
        if course.status == '进行中':
            ing.append(temp)
            res.append(temp)
        else:
            finish.append(temp)
            res.append(temp)
    if s == '进行中':
        return JsonResponse({'status': 'success', 'courses': ing})
    elif s == '已结束':
        return JsonResponse({'status': 'success', 'courses': finish})
    else:
        return JsonResponse({'status': 'success', 'courses': res})

def saveWork(request):
    wid = request.POST.get('wid')
    answers = request.POST.get('answers')
    name = request.POST.get('name')
    answers = json.loads(answers)
    for qid in answers:

        qs = s_q()
        qs.qid = qid
        ans = answers[qid]
        if ans == '1':
            ans = 'A'
        elif ans == '2':
            ans = 'B'
        elif ans=='3':
            ans = 'C'
        elif ans == '4':
            ans = 'D'
        elif ans == 5:
            ans='正确'
        elif ans == 6:
            ans='错误'
        else:
            ans = ans
        qs.ans = ans
        qs.name = name
        qs.save()
    ws = w_s()
    ws.wid = wid
    ws.name = name
    ws.t = datetime.now().strftime("%Y-%m-%d %H:%M")
    ws.save()
    return JsonResponse({'status': 'success'})