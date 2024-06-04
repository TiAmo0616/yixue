<template>
  <div>
      <!-- 说明：通过isLoggedIn区分已登录导航栏和未登录导航栏的差别，对应不同的内容，以下是示例 -->
      <!-- 已登录 -->
      <div  v-if="isLoggedIn">
        <el-row :gutter="20">
          <el-col :span="4">
            <div class="grid-content bg-purple">
              <img src="../assets/image/logo2.0-removebg-preview.png" alt="logo" height="60px" @click="backToMain"/>
            </div>
          </el-col>
        
          <el-col :span="14">
            <div class="grid-content bg-purple">
              <el-input placeholder="请输入内容" v-model="input3" class="input-with-select">
                  <el-button slot="append" icon="el-icon-search" @click="sousuo"></el-button>
                </el-input>
            </div>
          </el-col>

          <el-col :span="6">
            <div class="grid-content bg-purple">
              <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal">
                <el-menu-item index="3" @click="backToMain">首页</el-menu-item>
                <el-menu-item index="1" @click="enterClass">我的课堂</el-menu-item>
                <el-submenu index="2">
                      <template slot="title">{{ username }}|{{ currentrole }}</template>
                      <el-menu-item index="2-1" @click="editProfile">账号管理</el-menu-item>
                      <el-menu-item index="2-2" @click="logout">退出登录</el-menu-item>
                      <el-menu-item v-if="this.role == '老师'" index="2-3" @click="changeRole">切换身份</el-menu-item>
                  </el-submenu>
              </el-menu>
              </div>
          </el-col>
        </el-row>
      </div>

      <!-- 未登录 -->
      <div v-else class="customer">
        <el-row :gutter="20">
          <el-col :span="4">
            <div class="grid-content bg-purple">
              <img src="../assets/image/logo2.0-removebg-preview.png" alt="logo" height="60px" @click="backToMain"/>
            </div>
          </el-col>

          <el-col :span="14">
            <div class="grid-content bg-purple">
              <el-input placeholder="请输入内容" v-model="input3" class="input-with-select">
                  <el-button slot="append" icon="el-icon-search" @click="sousuo"></el-button>
                </el-input>
            </div>
          </el-col>
          <el-col :span="6">
            <div class="grid-content bg-purple">
              <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" :ellipsis="false" active-text-color="#eeae4b">             
                <el-menu-item index="3"  @click="backToMain">首页</el-menu-item>
                <el-menu-item index="1" @click="login">我的课堂</el-menu-item>
                <el-menu-item index="2" @click="login">登录|注册</el-menu-item>
              </el-menu>  
            </div>
          </el-col>
        </el-row>

                 
      </div>       
  </div>
  
</template>

<script>
import logo from "../assets/logo.png"
import axios from 'axios'
export default {
name: 'daohanglan',

data () {
  return {
    logo,
    activeIndex: '',
    opr:'',
    input3:'',
    matches:[],
  }
},
computed: {
  
  isLoggedIn() {
    return this.$store.state.isLoggedIn;
  },
  username() {
    return this.$store.state.username.username;
  },
  role() {
    return this.$store.state.username.role;
  },
  currentrole(){
      return this.$store.state.username.currentrole;
  }
},
methods:{
  sousuo(){
    this.$router.push({ name: 'searchPage' ,params:{'info':this.input3}});
  },
  changeRole(){
    if(this.currentrole == '学生'){
    this.opr = '老师'
  }
  else{
    this.opr='学生'
  }
    this.$store.commit('login',{username:this.username,role:this.role,currentrole:this.opr});
    localStorage.setItem('userInfo', {username:this.username,role:this.role,currentrole:this.opr});
    this.$router.push({ name: 'mainpage' ,params:{"username":this.username,'role':this.opr}});
  },
  logout(){
      this.$store.commit("logout")
      this.$router.push({ name: 'mainpage'});
  },
  editProfile(){
      this.$router.push({ name: 'userInfo' })
  },
  login(){
      this.$router.push({ name: 'login' })
  },
  enterClass(){
    console.log(this.role)
    if(this.currentrole == '学生'){this.$router.push({ name: 'studentPage' })}
    else{this.$router.push({ name: 'teacherPage' })}
  },
  backToMain(){
    this.$router.push({ name: 'mainpage'});
  }
}
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>


#customer{
display: flex;
justify-content:space-between;
}

.el-input{
width:70%;
margin-top: 10px;
justify-content:left;
}

.el-menu{
padding: 0;
}
</style>
