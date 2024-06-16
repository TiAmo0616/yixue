<template>
<div>
  <!-- 导航栏 -->
  <div>
    <Daohanglan :isLoggedIn="isLoggedIn" :user="username"></Daohanglan>
  </div>
  <!-- 图片滑动 -->
  <div>
      <el-carousel :interval="5000" indicator-position="outside">
        <el-carousel-item v-for="course in courses.slice(0,5)" :key="course.cid">
          <div>
            <div class="backgroundpic">
              <img :src="course.img" alt="" width="100%"/>              
            </div>
            
            <div class="box-font">             
              <h1>{{ course.cname }}</h1>
              <button @click="see(course.cid)">了解详情</button>
            </div>
            
          </div>
        </el-carousel-item>
      </el-carousel>
    </div>

  <!-- 显示课程 -->
  <div>
    <div class="headbox">
      <h1>课程精选</h1>
      <button @click="seeall">查看全部</button>
    </div>

    <div class="card">
      <el-row>
            <el-col :span="8" v-for="course in courses" :key="course.cid" >
              <el-card shadow="hover" >                
                <div @click="see(course.cid)">
                  <img :src="course.img" alt="" />
                  <h2>{{ course.cname }}</h2>
                  <h4>{{ course.teacher }}|{{ course.status }}</h4>
                </div>                
              </el-card>
            </el-col>
        </el-row>
    </div>
    
  </div>
    
  <!-- <div class="lastline">
    <p>Copyright © 2024 GoodGoodStudy. All rights reserved. </p>
  </div>  -->

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
    
    console.log(this.role)
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
   see(cid){
    this.$router.push({ name: 'myCourse' ,params:{'cid':cid}})
   },
   seeall(){
    this.$router.push({ name: 'courses'})
   },
 
  },
  // mounted () {
  //   // this.setSize();
  //   const that = this;
  //   window.addEventListener('resize', function() {
  //     that.screenWidth = $(window).width();
  //     that.setSize();
  //   }, false);
  // },
 
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.backgroundpic{
  width: 100%;
  height: inherit;
  min-height: 360px;
  min-width: 1000px;
  position: absolute;
}

.box-font {
  position: absolute;/*绝对布局*/
  z-index: 1;/*置于上层*/
  top: 0;
  left: 0;
  height:100%;
  width:50%;
  background-color: rgba(255, 255, 255, 0.5);
  display: flex;
}

.box-font h1{
  color: black;
  margin-left: 20%;
  margin-top: 50px;
}

.box-font button{  
  background-color: rgba(245, 154, 36, 0.8);
  border:1px solid black;
  color: black;
  height:50px;
  width:100px;
  
  font-size: 15px;
  position: absolute;
  bottom: 50px; /* 距离底部的距离，可以根据需要调整 */
  right: 100px;
}

.headbox{
  display: flex;
}

.headbox h1{
  color: black;
  margin-left: 30px;
  font-size:30px;
}

.headbox button{
  background-color: white;
  border:2px solid #F59A23;
  color: black;
  height:50px;
  width:100px;
  font-size: 15px;
  margin-left: 30px;
  margin-top: 20px;
  border-radius: 10px;
}

.card{
  margin:10px;
  height:400px;
  padding: 0;
}

.card img{
  display: block; /* 使图片以块级元素显示 */
  margin-left: auto;
  margin-right: auto;
  width:100%;
  height: 200px;
  object-fit: cover;
}

.card p{
  margin:5px;
}

.lastline p{
  position: relative;
  bottom: 0;
  font-size: 10px;  
}
</style>
