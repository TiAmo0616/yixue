<template>
<div>
     <!-- 导航栏 -->
    <div>
        <Daohanglan :isLoggedIn="isLoggedIn" :username="username"></Daohanglan>
    </div>
    <!-- 加个搜索框 -->
    <div>

    </div>
    <!-- 显示所有课程 -->
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

</template>

<script>
import axios from 'axios'
import Daohanglan from './daohanglan.vue';
export default {
  name: 'courses',
  components:{
    Daohanglan,
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
  data () {
    return {
      courses:[]
    }
  },
  created(){
    axios.post("http://127.0.0.1:8000/listCoursesAll/",{
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
    see(cid){
    this.$router.push({ name: 'myCourse' ,params:{'cid':cid}})
   },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
