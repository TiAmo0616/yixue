<template>
    <!-- 具体课程显示页面 -->
<div>
    <!-- 导航栏 -->
    <div>
        <Daohanglan :isLoggedIn="isLoggedIn" :username="username"></Daohanglan>
    </div>
    <!-- 课程名称 -->
    <div>
        {{ course.cname }}
    </div>
    <!-- 图片 -->
    <div>
      <img :src="course.img" alt="" width="200"/>
    </div>
    <!-- 课程介绍 -->
    <div>
      课程介绍
      {{ course.introduction }}
      学时{{ course.xueshi }}
      累计选课{{ course.stuNum }}人
      {{ course.status }}
    </div>
    <!-- 选课 -->
    <div>
      <div v-if="this.currentrole == '学生'">
        <div v-if="already==0">
          <button @click="pick">选课</button>
        </div>
        <div v-else>
          已选课
        </div>
      </div>
      
      
    </div>
    <!-- 教师 -->
    <div>
      授课教师
      {{ course.teacher }}
    </div>
    
</div>

</template>

<script>
import Daohanglan from './daohanglan.vue';
import axios from 'axios'
export default {
  name: 'myCourse',
  props: ['cid'],
  components:{
    Daohanglan,
  },
  data () {
    return {
      course:'',
      already:0,

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
  created(){
    axios.post("http://127.0.0.1:8000/showCourse/",{'cid':this.cid,'username':this.username},{
      headers: {
        'Content-Type': 'multipart/form-data'
      }
  })
      .then(response =>{
        console.log(response.data)
        if(response.data.status == 'success'){
          this.course = response.data.course
          this.already = this.course.already
        }
         
      })
      .catch(error => {
        
        console.error('Error:', error);
      });
  },
  methods:{
    pick(){
      if(this.isLoggedIn){
        axios.post("http://127.0.0.1:8000/pickCourse/",{'cid':this.cid,'username':this.username},{
      headers: {
        'Content-Type': 'multipart/form-data'
      }
  })
      .then(response =>{
        console.log(response.data)
        if(response.data.status == 'success'){
          this.course = response.data.course
          this.already = 1
        }
         
      })
      .catch(error => {
        
        console.error('Error:', error);
      });
      }
      else{
        this.$router.push({ name: 'login' })
      }
     
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
