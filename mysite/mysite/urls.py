"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app01 import views

urlpatterns = [
    path('register/',views.register),
    path('login/',views.login),
    path('edit/', views.editInfo),
    path('handleImage/',views.upload_image),
    path('showInfo/',views.showInfo),
    path('changePasswd/',views.changePasswwd),
    path('deleteUser/',views.deleteUser),
    path('showCourse/',views.showCourse),
    path('listCourses/',views.listCourses),
    path('listCoursesAll/',views.listCoursesAll),
    path('createCourse/',views.createCourses),
    path('teacherCourse/',views.teacherCourses),
    path('closeCourse/',views.closeCourse),
    path('listing/',views.listing),
    path('createWork/',views.createWork),
    path('showWorks/',views.showWorks),
    path('deleteWork/',views.deleteWork),
    path('saveq/',views.saveq),
    path('showQuestions/',views.showQuestions),
    path('deleteq/',views.deleteq),
    path('showtotalans/',views.showtotalans),
    path('pickCourse/',views.pickCourse),
    path('studentCourse/',views.studentCourses),
    path('exitCourse/',views.exitCourse)



]
