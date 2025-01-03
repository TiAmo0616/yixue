import io
import json
import os
from datetime import datetime, timedelta
import paramiko
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.shortcuts import render

from difflib import get_close_matches

# Create your views here.
from app01.models import userInfo

from app01.models import Course
import uuid

from app01.models import Work


from app01.models import sc

from app01.models import w_s

from app01.models import question

from app01.models import s_q

from app01.models import problem
from app01.models import records
from app01.models import learningMaterials
from app01.models import Answer
from app01.models import comment
from app01.models import CommentZan


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
    temp['u'] = course.username
    temp['zhibo'] = course.zhibo
    return JsonResponse({'status': 'success','course':temp})

#精选课程
def listCourses(request):
    res = []
    courses = Course.objects.all()
    for course in courses:
        if len(res)<9 and course.status=='进行中':
            temp = {}
            temp['cid'] = course.cid
            temp['cname']= course.cname
            temp['img'] =  "http://127.0.0.1:8000/static/"+course.img
            temp['teacher'] = course.teacher
            temp['status'] = course.status
            res.append(temp)
        if len(res)>=9:
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
    if file_name:
        save_path = 'app01/static/' + file_name
        image_url = "http://127.0.0.1:8000/static/" + file_name
        # 使用文件系统存储对象进行保存
        fs = FileSystemStorage()
        fs.save(save_path, file_obj)
        course.img = file_name

    # course.createdate = current_date
    if introduction:
        course.introduction = introduction
    if xueshi:
        course.xueshi = xueshi
    course.username = username
    course.cname = cname

    course.cid = generate_course_code(8)
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
    temp['teacher'] = course.teacher
    temp['introduction'] = course.introduction
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
    res.sort(key=lambda  x:x['begin'])
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
    cid = request.POST.get('cid')
    submitstudents = w_s.objects.filter(wid=wid)
    totalstudents =sc.objects.filter(cid=cid)
    alreadysubmit = len(submitstudents)
    noal = len(totalstudents)-alreadysubmit
    res=[]
    for ws in submitstudents:
        temp={}
        temp['username'] = ws.name
        temp['t'] = ws.t
        temp['status'] = ws.status
        res.append(temp)
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
    zhiboCourse=[]
    for i in courses:
        course = Course.objects.filter(cid=i.cid).first()
        temp = {}
        temp['cid'] = course.cid
        temp['cname'] = course.cname
        temp['img'] = "http://127.0.0.1:8000/static/"+ course.img
        temp['xueshi'] = course.xueshi
        temp['status'] = course.status
        if course.zhibo == '正在直播':
            zhiboCourse.append(course.cname)
            zhiboCourse.append(course.cid)
        res.append(temp)
    return JsonResponse({'status': 'success', 'courses': res,'zhibo':zhiboCourse})

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
        q = question.objects.filter(qid=qid).first()
        trueans = q.q_ans
        score = q.score
        if ans == 1:
            ans = 'A'
            if ans==trueans:
                qs.score=score
            else:
                qs.score='0'
        elif ans == 2:
            ans = 'B'
            if ans==trueans:
                qs.score=score
            else:
                qs.score='0'
        elif ans==3:
            ans = 'C'
            if ans==trueans:
                qs.score=score
            else:
                qs.score='0'
        elif ans == 4:
            ans = 'D'
            if ans==trueans:
                qs.score=score
            else:
                qs.score='0'
        elif ans == 5:
            ans='正确'
            if ans==trueans:
                qs.score=score
            else:
                qs.score='0'
        elif ans == 6:
            ans='错误'
            if ans==trueans:
                qs.score=score
            else:
                qs.score='0'
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


def studentWorks(request):
    username = request.POST.get('username')
    cid = request.POST.get('cid')
    status = request.POST.get('status')
    res = searchWork(cid,status)
    wss = w_s.objects.filter(name=username)
    wids=[]
    status={}
    for ws in wss:
        wids.append(ws.wid)
        status[ws.wid] = ws.status
    return JsonResponse({'status': 'success', 'works': res,'wids':wids,'statuses':status})

def seeStudentWork(request):
    wid = request.POST.get('wid')
    name = request.POST.get('name')
    ws = w_s.objects.filter(wid=wid,name=name).first()
    qss = question.objects.filter(wid=wid)
    res=[]
    answers={}
    scores={}
    judgements={}
    for qs in qss:
        temp={}
        qid = qs.qid
        temp['qid'] = qid
        temp['qname'] = qs.qname
        temp['info'] = qs.info
        temp['ans'] = qs.q_ans
        temp['kind'] = qs.kind
        temp['a'] = qs.a
        temp['b'] = qs.b
        temp['c'] = qs.c
        temp['d'] = qs.d
        temp['score'] = qs.score
        userans = s_q.objects.filter(qid=qid,name=name).first()
        ans = A21(userans.ans)
        temp['myans'] = ans

        answers[qid] = ans
        if ws.status == '已批改':
            scores[qid] = userans.score
            judgements[qid] = userans.judgement
        res.append(temp)
    res.sort(key=lambda x:x['qname'])
    return JsonResponse({'status': 'success', 'works': res,'answers':answers,'scores':scores,'judgements':judgements})

def A21(ans):
    if ans == 'A':
        ans=1
    elif ans == 'B':
        ans=2
    elif ans=='C':
        ans=3
    elif ans=='D':
        ans=4
    elif ans=='正确':
        ans=5
    elif ans=='错误':
        ans=6
    else:
        ans=ans
    return ans

def saveCheck(request):
    wid = request.POST.get('wid')
    name = request.POST.get('name')
    scoredata = request.POST.get('scores')
    scoredata = json.loads(scoredata)
    judgedata = request.POST.get('judges')
    judgedata = json.loads(judgedata)
    for qid in scoredata:
        qs = s_q.objects.filter(qid=qid,name=name).first()
        qs.score = scoredata[qid]
        if qid in judgedata:
            qs.judgement = judgedata[qid]
        qs.save()
    ws = w_s.objects.filter(wid=wid,name=name).first()
    ws.status = '已批改'
    ws.save()
    return JsonResponse({'status': 'success'})

def searchProblems(cid,status,username):

    problems = problem.objects.filter(cid=cid)
    res=[]
    mys = []
    jhs = []
    for p in problems:
        temp={}
        temp['pid'] = p.pid
        temp['askername'] = p.name
        temp['t'] = p.t
        temp['status'] = p.status
        temp['ans'] = p.ans
        temp['pinfo'] = p.info
        temp['jh'] = p.jh
        res.append(temp)
        if p.name == username:
            mys.append(temp)
        if p.jh == '1':
            jhs.append(temp)

    if status == 'my':
        return  mys
    elif status == 'jh':
        return jhs
    res.sort(key=lambda  x:x['t'])
    return res

def showProblems(request):
    username = request.POST.get('username')
    cid = request.POST.get('cid')
    status = request.POST.get('status')
    problems = searchProblems(cid,status,username)
    return JsonResponse({'status': 'success', 'problems':problems})

def saveProblems(request):
    username = request.POST.get('username')
    cid = request.POST.get('cid')
    info = request.POST.get('info')
    pid = generate_course_code(12)
    t = datetime.now().strftime("%Y-%m-%d %H:%M")
    p = problem()
    p.pid = pid
    p.info = info
    p.cid = cid
    p.name = username
    p.t = t
    p.save()
    problems = searchProblems(cid, 'all', username)
    return JsonResponse({'status': 'success', 'problems': problems})

def beginClass(request):
    cid = request.POST.get('cid')
    course = Course.objects.filter(cid=cid).first()
    course.zhibo = '正在直播'
    course.save()
    return JsonResponse({'status': 'success'})

def endClass(request):
    cid = request.POST.get('cid')
    course = Course.objects.filter(cid=cid).first()
    course.zhibo = '暂无直播'
    course.save()
    return JsonResponse({'status': 'success'})


def showzhiboInfo(request):

    name = request.POST.get('username')
    user = userInfo.objects.filter(name=name).first()
    myName = request.POST.get('myName')
    me = userInfo.objects.filter(name=myName).first()
    return JsonResponse({'status': 'success','img':"http://127.0.0.1:8000/static/"+user.img,'myImage':"http://127.0.0.1:8000/static/"+me.img})

def updateRecords(request):
    cid = request.POST.get('cid')
    rootPath = request.POST.get('rootPath')
    paths = json.loads(request.POST.get('paths'))
    period = request.POST.get('period')
    paths.sort()
    print(rootPath)
    print(paths)
    record = records()
    record.cid = cid
    record.period = period
    record.path = rootPath+paths[-1]
    record.rname = period+":"+paths[-1]
    record.save()
    return JsonResponse({'status': 'success'})

def getRecordsList(request):#[{'period':2024-05-20','records':[{},{}]},{}]
    cid = request.POST.get('cid')
    rs = records.objects.filter(cid=cid)
    # res0=[]
    # for record in rs:
    #     period = record.period
    #     path = record.path
    #     res0.append({'period':period,'rname':record.rname,'path':path})
    res=[]
    flag = True
    for record in rs:
        period = record.period
        flag = True
        for i in res:
            if i['period'] == period:
                flag = False
                i['records'].append({'period':period,'rname':record.rname,'path':record.path})
        if flag:
            res.append({'period':period,'records':[{'period':period,'rname':record.rname,'path':record.path}]})


    print(res)
    return JsonResponse({'status': 'success','res':res})

def reName(request):
    cid = request.POST.get('cid')
    newrname = request.POST.get('newrname')
    rname = request.POST.get('rname')
    rec = records.objects.filter(cid=cid,rname=rname).first()
    rec.rname = newrname
    rec.save()
    return JsonResponse({'status': 'success'})

def deletelubo(request):
    cid = request.POST.get('cid')
    rname = request.POST.get('rname')
    rec = records.objects.filter(cid=cid, rname=rname).first()
    rec.delete()
    return JsonResponse({'status': 'success'})


def uploadVideo(request):
    video_file = request.FILES['video']
    file_contents = video_file.read()  # 读取文件内容
    file_name = video_file.name  # 获取文件原始名称
    transport = paramiko.Transport(("192.168.44.129", 22))
    transport.connect(username="xu", password="11280616")
    sftp = paramiko.SFTPClient.from_transport(transport)

    try:
        sftp.putfo(io.BytesIO(file_contents), "/home/xu/demo1/ZLMediaKit/release/linux/Debug/www/lubo/"+file_name)
        return JsonResponse({'status': 'success','rname':file_name,'path':"/home/xu/demo1/ZLMediaKit/release/linux/Debug/www/lubo/"+file_name})
    except Exception as e:
        return JsonResponse({'status': 'fail'})
    finally:
        sftp.close()
        transport.close()


def appendLM(request):
    cid = request.POST.get('cid')
    did  = request.POST.get('id')
    label = request.POST.get('label')
    parentdid = request.POST.get('pdid')
    path = request.POST.get('path')
    lm = learningMaterials()
    lm.cid = cid
    lm.did = did
    lm.label = label
    lm.parentdid = parentdid
    lm.path = path
    lm.save()
    return JsonResponse({'status': 'success'})

def deleteLM(request):
    cid = request.POST.get('cid')
    did = request.POST.get('id')
    lm = learningMaterials.objects.filter(cid=cid,did=did).first()
    lm.delete()
    operateLM(cid)
    return JsonResponse({'status': 'success'})

def searchLM(request):
    cid = request.POST.get('cid')
    lmTree = learningMaterials.objects.filter(cid=cid)
    res0=[]
    for lm in lmTree:
        temp={}
        temp['did'] = lm.did
        temp['label'] = lm.label
        temp['children'] = []
        temp['path'] = lm.path
        temp['pdid'] = lm.parentdid
        res0.append(temp)
    res0.sort(key=lambda x:int(x['did']))
    res1=[{'did':'0','label':'学习资源','children':[],'path':''}]
    for i in res0:
        pdid = i['pdid']
        for j in res1:
            if j['did'] == pdid:
                j['children'].append(i)
                res1.append(i)

    res1.reverse()
    for i in range(len(res1)):
        for j in range(i+1,len(res1)):
            if res1[i]['pdid'] == res1[j]['did']:
                for k in range(len(res1[j]['children'])):
                    if res1[j]['children'][k]['did'] == res1[i]['did']:
                        res1[j]['children'][k] = res1[i]


        # if i not in res:
        #     lm = learningMaterials.objects.filter(cid=cid,did=i['id']).first()
        #     lm.delete()
    if len(res0)>0:
        maxId = res0[-1]['did']
    else:
        maxId = 0

    return JsonResponse({'status': 'success','res':[res1[-1]],'maxId':int(maxId)+1})

def operateLM(cid):
    lmTree = learningMaterials.objects.filter(cid=cid)
    res0 = []
    for lm in lmTree:
        temp = {}
        temp['id'] = lm.did
        temp['label'] = lm.label
        temp['children'] = []
        temp['path'] = lm.path
        pdid = lm.parentdid
        temp['pdid'] = pdid
        res0.append(temp)
    res0.sort(key=lambda x: x['id'])
    res = [{'id': '0', 'label': '学习资源', 'children': [], 'path': ''}]
    for i in res0:
        pdid = i['pdid']
        for j in res:
            if j['id'] == pdid:
                j['children'].append(i)
                res.append(i)
        if i not in res:
            lm = learningMaterials.objects.filter(cid=cid, did=i['id']).first()
            lm.delete()

def editDirectory(request):
    cid = request.POST.get('cid')
    did = request.POST.get('id')
    label = request.POST.get('label')
    lm = learningMaterials.objects.filter(cid=cid, did=did).first()
    lm.label = label
    lm.save()
    return JsonResponse({'status': 'success'})

def editCourse(request):
    cid = request.POST.get('cid')
    cname = request.POST.get('cname')
    xueshi = request.POST.get('xueshi')
    info = request.POST.get('intro')
    teacher = request.POST.get('teacher')
    c = Course.objects.filter(cid=cid).first()
    c.cname = cname
    c.xueshi = xueshi
    c.introduction = info
    c.teacher = teacher
    c.save()
    return JsonResponse({'status': 'success'})


def changeImage(request):
    # 图片对象
    file_obj = request.FILES.get('file')
    # 图片名字
    file_name = request.POST.get('fileName')
    cid = request.POST.get('cid')  # 账号名

    save_path = 'app01/static/' + file_name
    image_url = "http://127.0.0.1:8000/static/" + file_name
    # 使用文件系统存储对象进行保存
    fs = FileSystemStorage()
    fs.save(save_path, file_obj)

    c = Course.objects.filter(cid=cid).first()
    c.img = file_name
    c.save()
    # 返回图片保存路径给前端

    return JsonResponse({
        "file_name": file_name,
        'url': image_url})


def deleteCourse(request):
    cid = request.POST.get('cid')
    c = Course.objects.filter(cid=cid).first()
    c.delete()
    scs = sc.objects.filter(cid=cid)
    for i in scs:
        i.delete()
    return JsonResponse({'status': 'success'})

def searchProblem(request):
    cid = request.POST.get('cid')
    pid = request.POST.get('pid')
    p = problem.objects.filter(pid=pid).first()
    answers = Answer.objects.filter(pid=pid)
    res=[]
    for answer in answers:
        temp = {}
        temp['info'] = answer.ans
        temp['answerer'] = answer.name
        temp['answerTime'] = answer.t
        temp['aid'] = answer.aid
        res.append(temp)


    return JsonResponse({'status': 'success','info':p.info,'asker':p.name,'t':p.t,'resolved':p.status,'jh':p.jh,'res':res})

def createAnswer(request):
    pid = request.POST.get('pid')
    aid = generate_course_code(12)
    t = datetime.now().strftime("%Y-%m-%d %H:%M")
    ans = request.POST.get('ans')
    answerer = request.POST.get('answerer')
    a = Answer()
    a.ans = ans
    a.aid = aid
    a.pid = pid
    a.t = t
    a.name = answerer
    a.save()
    return JsonResponse({'status': 'success'})

def showAns(request):
    pid = request.POST.get('pid')
    answers = Answer.objects.filter(pid=pid)
    res = []
    for answer in answers:
        temp = {}
        temp['info'] = answer.ans
        temp['answerer'] = answer.name
        temp['answerTime'] = answer.t
        temp['aid'] = answer.aid
        res.append(temp)
    return JsonResponse({'status': 'success','res':res})

def deleteAnswer(request):
    aid = request.POST.get('aid')
    a = Answer.objects.filter(aid=aid).first()
    a.delete()
    return JsonResponse({'status': 'success'})

def deleteProblem(request):
    pid = request.POST.get('pid')
    p = problem.objects.filter(pid=pid).first()
    p.delete()
    return JsonResponse({'status': 'success'})

def setjh(request):
    pid = request.POST.get('pid')
    p = problem.objects.filter(pid=pid).first()
    p.jh = 1
    p.save()
    return JsonResponse({'status': 'success'})


def fuzzy_search(word_list, word_to_search):
    matches = get_close_matches(word_to_search, word_list, n=5)
    return matches
def sousuo(request):
    info = request.POST.get('info')
    courses = Course.objects.filter()
    word_list = []
    for i in courses:
        if i.cname not in word_list:
            word_list.append(i.cname)
    matches = fuzzy_search(word_list, info)
    res=[]
    for i in matches:
        c = Course.objects.filter(cname=i)
        for j in c:
            temp={}
            temp['cid'] = j.cid
            temp['cname'] = j.cname
            temp['teacher'] = j.teacher
            temp['xueshi'] = j.xueshi
            temp['img'] = "http://127.0.0.1:8000/static/" +j.img
            temp['status'] = j.status
            res.append(temp)
    return JsonResponse({'status': 'success','matches':res})

def createComment(request):
    cid = request.POST.get('cid')
    info = request.POST.get('info')
    username = request.POST.get('username')
    t = datetime.now().strftime("%Y-%m-%d %H:%M")
    commid = generate_course_code(8)
    comm = comment()
    comm.cid = cid
    comm.info = info
    comm.username = username
    comm.t = t
    comm.comid = commid
    comm.save()
    return JsonResponse({'status': 'success'})

def showComments(request):
    cid = request.POST.get('cid')
    username = request.POST.get('username')
    comments = comment.objects.filter(cid = cid)
    res=[]
    for i in comments:
        temp = {}
        jilu = CommentZan.objects.filter(comid=i.comid, username=username).first()
        if jilu:
            temp['showZan'] = 'on'
        else:
            temp['showZan'] = 'off'


        temp['info'] = i.info
        temp['username'] = i.username
        temp['t'] = i.t
        temp['zan'] = i.zan
        temp['comid'] = i.comid
        res.append(temp)
    res.sort(key=lambda x:x['t'])
    return JsonResponse({'status': 'success', 'res': res})

def deleteComment(request):
    cid = request.POST.get('cid')
    comid = request.POST.get('comid')
    c = comment.objects.filter(cid=cid,comid=comid).first()
    c.delete()
    return JsonResponse({'status': 'success'})

def dianzan(request):
    comid = request.POST.get('comid')
    username = request.POST.get('username')
    jilu = CommentZan.objects.filter(comid=comid,username=username).first()
    c = comment.objects.filter(comid=comid).first()
    if jilu:
        jilu.delete()
        c.zan-=1
        c.save()
        return JsonResponse({'status': 'success'})#已经给这条评论点过赞了，取消点赞
    else:

        c.zan+=1
        c.save()
        c2u = CommentZan()
        c2u.comid = comid
        c2u.username = username
        c2u.save()
        return JsonResponse({'status': 'success'})

