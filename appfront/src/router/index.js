import Vue from 'vue'
import Vuex from 'vuex'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import mainpage from '@/components/mainpage'
import login from '@/components/login'
import register from '@/components/register'
import userInfo from '@/components/userInfo'
import myCourse from '@/components/myCourse'
import teacherPage from '@/components/teacherPage'
import studentPage from '@/components/studentPage'
import singleCourse from '@/components/singleCourse'
import setquestions from '@/components/setquestions'
import totalAnswer from '@/components/totalAnswer'
import courses from '@/components/courses'
import homework from '@/components/homework'
import studentCourse from '@/components/studentCourse'
import judgeWork from '@/components/judgeWork'
import myWork from '@/components/myWork'
import zhibodemo from '@/components/zhibodemo'
import teacherzhibo from '@/components/teacherzhibo'
import studentzhibo from '@/components/studentzhibo'
import dianbo from '@/components/dianbo'
import lessonInfo from '@/components/lessonInfo'
import problem from '@/components/problem'
import searchPage from '@/components/searchPage'

Vue.use(Router)
Vue.use(Vuex);
const state = {
  isLoggedIn: false,
  username:'',
  role:'',
}
const mutations= {
  login(state,user) {
    
    state.isLoggedIn = true;
    state.username = user.username
    state.role = user.role
    
  },
  logout(state) {
    state.isLoggedIn = false;
    
    state.username = '';
    state.role = ''
  }
}
var store = new Vuex.Store({
 
  state,
  mutations
})
 
export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/main',
      name: 'mainpage',
      component: mainpage
    },
    {
      path: '/login',
      name: 'login',
      component: login,
      props: true
    },
    {
      path: '/register',
      name: 'register',
      component: register
    },
    {
      path: '/userInfo',
      name: 'userInfo',
      component: userInfo,
      props: true
    },
    {
      path: '/myCourse',
      name: 'myCourse',
      component: myCourse,
      props: true
    },
    {
      path: '/teacherPage',
      name: 'teacherPage',
      component: teacherPage,
      props: true
    },
    {
      path: '/studentPage',
      name: 'studentPage',
      component: studentPage,
      props: true
    },
    {
      path: '/singleCourse',
      name: 'singleCourse',
      component: singleCourse,
      props: true
    },
    {
      path: '/setquestions',
      name: 'setquestions',
      component: setquestions,
      props: true
    },
    {
      path: '/totalAnswer',
      name: 'totalAnswer',
      component: totalAnswer,
      props: true
    },
    {
      path: '/courses',
      name: 'courses',
      component: courses,
      props: true
    },
    {
      path: '/studentCourse',
      name: 'studentCourse',
      component: studentCourse,
      props: true
    },
    {
      path: '/homework',
      name: 'homework',
      component: homework,
      props: true
    },
    {
      path: '/judgeWork',
      name: 'judgeWork',
      component: judgeWork,
      props: true
    },
    {
      path: '/myWork',
      name: 'myWork',
      component: myWork,
      props: true
    },
    {
      path: '/zhibodemo',
      name: 'zhibodemo',
      component: zhibodemo,
      props: true
    },
    {
      path: '/teacherzhibo',
      name: 'teacherzhibo',
      component: teacherzhibo,
      props: true
    },
    {
      path: '/studentzhibo',
      name: 'studentzhibo',
      component: studentzhibo,
      props: true
    },
    {
      path: '/dianbo',
      name: 'dianbo',
      component: dianbo,
      props: true
    },
    {
      path: '/lessonInfo',
      name: 'lessonInfo',
      component: lessonInfo,
      props: true
    },
    {
      path: '/problem',
      name: 'problem',
      component: problem,
      props: true
    },
    {
      path: '/searchPage',
      name: 'searchPage',
      component: searchPage,
      props: true
    },



  ]
})
