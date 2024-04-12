# yixue

## 说明
dnaghanglan.vue导航栏组件√

mainPage.vue首页√

login.vue登录界面√

register.vue 注册界面√

userInfo.vue账号管理界面√

myCourse.vue课程具体页面√

teacherPage.vue教师端的我的课堂

studentPage.vue学生端的我的课堂

courses.vue显示所有课程（无原型图）

singleCourse.vue教师端我的课堂中点击一门课程显示的具体课程页面

homework.vue学生作答页面，页面只显示一题，点击下一题之后跳转（无原型图）

setQuestions.vue老师设置题目界面（无原型图）

totalAnswer.vue一门作业对应的学生作答情况（无原型图）

singleAnswer.vue某个学生一门作业的作答情况（无原型图）

studentCourse.vue学生端我的课堂中点击一门课程显示的具体课程页面


## 前端想法

2024.4.5

关于teacherPage.vue：

有三个按钮显示全部、进行中和已结束，
我想要导航栏的那种效果，
就是比如点击进行中，
那进行中的样式就和其他两个不一样，
让用户知道现在显示的是进行中

2024.4.7

关于el-row的样式，基本上都是矩形框，每个矩形框里面是一个作业的信息或者学生提交信息等等。
可以加个那种 已提交 水印，绿色的那种

因为没有原型图，所以我没有考虑界面设计，只实现交互

比如说mainpage需要点击课程的名字然后跳转到页面，鼠标光标移动到文字上的时候文字要变色

关于myCourse.vue：原本的课程内容部分删掉，可以把简介调整到这部分，页面重新设计一下

其实有一些模块是差不多的，比如说studentPage和teacherPage，只是有很小的区别，可以考虑把相同的部分抽出来单独作为一个组件，这样写起来会方便清晰一点，但是我暂时没有这样做，考虑到交互问题，设计页面的时候可以考虑一下

2024.4.11

关于导航栏的问题：你点中比如说我的课堂的时候，应该有个下划线，就是显示指出我当前是在这个菜单，

2023.4.12

可能因为是本地的原因，点浏览器自带的返回上一页的按钮，网页之间传递的参数会丢失，我就加了一个页头，点击它回到上一页，


## 每日进度（碎碎念？）

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

2024.4.6

原型图还是要画的尽量详细一点，不然在开发的时候还要考虑界面设计，越写越觉得我们画的原型图好粗糙，很多地方都没有考虑

发布作业的交互基本完成，但是时间不是北京时间，需要调整

2024.4.7

时间问题已经解决，用timedelta手动修改的

教师端设置作业题目已经完成，只能删除和增加，因为修改很麻烦...

每日一吐槽 原型图实在是太粗糙了

~~totalAnswer还没写完，因为学生选课的交互还没搞，先去搞myCourse.vue~~

myCourse.vue 和 courses.vue基本完成

看后端代码，发现冗余代码很多，导致整体很杂乱，work之后的函数在写的时候规避了冗余，之前关于course的代码很冗余，有空再来优美一下代码吧

导航栏写错了，牵一发而动全身......虽然搞好了，但我并不能理解，明明按教程写的但是username和role就是传不进去，最后居然是用username.username和username.role来获取全局的username和role，好离谱.....

正在写studentPage，加载课程和退课完成了

2024.4.12

homework.vue 和studentCourse.vue，学生可以写作业，提交之后显示已完成

作业模块应该好了，学生可以完成作业，老师可以批改，老师和学生都可以查看批改好的作业.


