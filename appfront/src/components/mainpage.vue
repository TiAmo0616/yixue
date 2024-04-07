<template>
<div>
  <!-- 导航栏 -->
  <div>
    <Daohanglan :isLoggedIn="isLoggedIn" :username="username"></Daohanglan>
  </div>
  <!-- 图片滑动 -->
  <div>

  </div>
  <!-- 显示课程 -->
  <div>
    <div>
      课程精选
      <button @click="seeall">查看全部</button>
    </div>
    <div>
      <el-row :gutter="20">
        <el-col v-for="course in courses" :key="course.cid" :span="6">
          <div class="course-card">
            <img :src="course.img" alt="" width="200" height="150"/>
            <div class="course-info">
              <h3 @click="see(course.cid)">{{ course.cname }}</h3>
              <h4>{{ course.teacher }}|{{ course.status }}</h4>
            </div>
          </div>
        </el-col>
      </el-row>
    </div>
  </div>
    
    
</div>

</template>

<script>
import axios from 'axios'
import Daohanglan from './daohanglan.vue';
export default {
  name: 'mainpage',
  props:{
    
    },
  components:{
    Daohanglan,
  },
  data () {
    return {
      islogged:false,
      courses: [] 
    }
  },
  created(){
    axios.post("http://127.0.0.1:8000/listCourses/",{
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
   see(cid){
    this.$router.push({ name: 'myCourse' ,params:{'cid':cid}})
   },
   seeall(){
    this.$router.push({ name: 'courses'})
   }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
