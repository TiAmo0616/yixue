# yixue

##说明

mainPage.vue首页

login.vue登录界面

register.vue 注册界面

userInfo.vue账号管理界面

myCourse.vue课程具体页面

teacherPage.vue教师端的我的课堂

studentPage.vue学生端的我的课堂

courses.vue显示所有课程

singleCourse.vue教师端我的课堂中点击一门课程显示的具体课程页面

##前端想法

2023.4.5

关于teacherPage.vue：

有三个按钮显示全部、进行中和已结束，
我想要导航栏的那种效果，
就是比如点击进行中，
那进行中的样式就和其他两个不一样，
让用户知道现在显示的是进行中


##每日进度

2024.3.30

已登录和未登录首页都是mainpage，区别在于导航栏图标，登录之后我会传递参数username和role过来，可以用v-if进行判别显示

登录界面login

注册界面register

登录成功后不论是老师还是学生都跳转到mainpage

注册成功跳转到登录界面

2024.3.31

mainpage/login/register的交互基本完成，只需设计界面

2024.4.1

完成账号管理的更换图像（搞了好久好久....）

2024.4.2

账号管理的页面交互基本完成

2024.4.5

教师端我的课堂界面交互基本完成，包括创建课程，显示课程，显示进行中，显示已结束，结束课程

注意，无论当前显示的是全部、进行中还是已结束，创建课程后都会显示全部课程

