<template>
<div>
  <!-- 导航栏 -->
  <div>
      <Daohanglan :isLoggedIn="isLoggedIn" :username="username"></Daohanglan>
  </div>
  <!-- 我的课堂 -->
  <div>
        我的课堂
        <button @click="listing('显示全部')">显示全部</button>
        <button @click="listing('进行中')">进行中</button>
        <button @click="listing('已结束')">已结束</button>
        <div>
            <el-row v-for="course in courses" :key="course.cid">
                
                <img :src="course.img" alt="" width="200"/>
               <div @click="enter(course.cid)">
                {{ course.cname }}
               </div> 
               学时:{{ course.xueshi }}
               {{ course.status }}
                <button @click="exitCourse(course.cid)" v-if="course.status == '进行中'">退选课程</button>
            </el-row>
        </div>
    </div>

</div>

</template>

<script>
import axios from 'axios'
import Daohanglan from './daohanglan.vue';
export default {
  name: 'studentPage',
  components:{
    Daohanglan,
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
    }
  },
  data () {
    return {
      courses:[]
    }
  },
  created(){
    axios.post("http://127.0.0.1:8000/studentCourse/",{'username':this.username},{
      headers: {
        'Content-Type': 'multipart/form-data'
      }
  })
      .then(response =>{
        console.log(response.data)
        if(response.data.status == 'success'){
          this.courses = response.data.courses
        }
         
      })
      .catch(error => {
        
        console.error('Error:', error);
      });
  },
  methods:{
    exitCourse(cid){
      axios.post("http://127.0.0.1:8000/exitCourse/",{'username':this.username,'cid':cid},{
      headers: {
        'Content-Type': 'multipart/form-data'
      }
  })
      .then(response =>{
        console.log(response.data)
        if(response.data.status == 'success'){
          alert("退选成功！")
          this.courses = response.data.courses
        }
         
      })
      .catch(error => {
        
        console.error('Error:', error);
      });
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
