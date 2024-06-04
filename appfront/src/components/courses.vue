<template>
<div>
     <!-- 导航栏 -->
    <div>
        <Daohanglan :isLoggedIn="isLoggedIn" :username="username"></Daohanglan>
    </div>

    <!-- 显示所有课程 -->
    <div class="pagebody">
      <div>
        <el-row>
            <el-col :span="6" v-for="course in courses" :key="course.cid" :offset="index > 0 ? 2 : 0">
              <el-card shadow="hover" class="card ">
                <div class="course-card" @click="see(course.cid)">
                  <img :src="course.img" alt="" width="200" height="150"/>
                  <div class="course-info">
                    <h3>{{ course.cname }}</h3>
                    <h4>{{ course.teacher }}|{{ course.status }}</h4>
                  </div>
                </div>              
              </el-card>
            </el-col>
          </el-row>

          
      </div>

      <div class="lastline">
        <p>Copyright © 2024 GoodGoodStudy. All rights reserved. </p>
      </div>
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
.pagebody{
  background-color: #f5f5f5;
  /* position: fixed; */
  overflow-y: scroll;
  max-width: 100vw;
  margin: 0 auto;
  overflow:hidden;
 
}

.lastline p{
  position: relative;
  bottom: 0;
  font-size: 10px;  
}
</style>
