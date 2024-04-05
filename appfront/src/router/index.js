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
Vue.use(Router)
Vue.use(Vuex);
const state = {
  isLoggedIn: false,
  username:'',
  role:''
}
const mutations= {
  login(state,username,role) {
    state.isLoggedIn = true;
    state.username = username;
    state.role = role
  },
  logout(state,username,role) {
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
    }
  ]
})
