<template>
    <div>
        <!-- 说明：通过isLoggedIn区分已登录导航栏和未登录导航栏的差别，对应不同的内容，以下是示例 -->
        <div  v-if="isLoggedIn">
            <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal">
              <el-menu-item index="1" @click="enterClass">我的课堂</el-menu-item>
              <el-submenu index="2">
                    <template slot="title">{{ username }}</template>
                    <el-menu-item index="2-1" @click="editProfile">账号管理</el-menu-item>
                    <el-menu-item index="2-2" @click="logout">退出登录</el-menu-item>
                </el-submenu>
            </el-menu>
        </div>
        <div v-else>
          <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal">
              <el-menu-item index="1" @click="login">我的课堂</el-menu-item>
              <el-menu-item index="1" @click="login">登录|注册</el-menu-item>
            </el-menu>
        </div>
        
    </div>
    
</template>

<script>
import logo from "../assets/logo.png"

export default {
  name: 'daohanglan',

  data () {
    return {
      logo,
      isloged:false
    }
  },
  computed: {
    isLoggedIn() {
      return this.$store.state.isLoggedIn;
    },
    username() {
      return this.$store.state.username;
    },
    role() {
      return this.$store.state.role;
    }
  },
  methods:{
    logout(){
        this.$store.commit("logout")
    },
    editProfile(){
        this.$router.push({ name: 'userInfo' })
    },
    login(){
        this.$router.push({ name: 'login' })
    },
    enterClass(){
      this.$router.push({ name: 'myCourse' })
    },

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
