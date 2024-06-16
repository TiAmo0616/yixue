<template>
<div>
  <!-- 导航栏 -->
  <div>
      <Daohanglan :isLoggedIn="isLoggedIn" :username="username"></Daohanglan>
  </div>
  <!-- 我的课堂 -->
  <div class='pagebody'>
    <div class="steambox" v-show="steamvisible">
      <h4>{{zhibocourse}}正在直播!</h4>
      <button @click="enter()">进入直播间</button>
    </div>
    <div class='box'>
        <div class='headinfo'>
          <h1>我的课堂</h1>
        </div>

       <div class="tab-pane">
          <el-tabs v-model="activeName" @tab-click="handleClick">
            <el-tab-pane label="全部课程" name="all"></el-tab-pane>
            <el-tab-pane label="进行中" name="ing"></el-tab-pane>
            <el-tab-pane label="已结束" name="done"></el-tab-pane>
          </el-tabs>
        </div>

        <div>
            <el-row>
            <el-col :span="8" v-for="course in courses" :key="course.cid" :offset="index > 0 ? 2 : 0">
              <el-card shadow="hover" class="card ">
                
                <div @click="enterCourse(course.cid)">
                  <img :src="course.img" alt="" />
                  <h2>{{ course.cname }}</h2>
                </div>
                <p>学时:{{ course.xueshi }}</p>
                <p>{{ course.status }}</p>
                <button @click="exitCourse(course.cid)" v-if="course.status == '进行中'">退选课程</button>
                
              </el-card>
            </el-col>
          </el-row>
        </div>
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
      courses:[],
      zhibocourse:'',
      zhibocid:'',
      steamvisible:false,
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
          console.log(response.data.zhibo.length)
          if(response.data.zhibo.length>0){
            this.zhibocourse = response.data.zhibo[0]
            this.zhibocid = response.data.zhibo[1]
            this.steamvisible=true;
            
          }
        }
         
      })
      .catch(error => {
        
        console.error('Error:', error);
      });
  },
  methods:{
    
    handleClick(tab, event) {
        console.log(tab, event);
        if (tab.name === 'all') {
        // 调用listing函数，并传递'显示全部'
          this.listing('显示全部');
        }
        else if(tab.name === 'ing'){
          this.listing('进行中');
        }
        else{
          this.listing('已结束');
        }
      },
    listing(s){
      axios.post("http://127.0.0.1:8000/listMyCourses/",{'username':this.username,'s':s},{
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
    },
    enter(){

      this.$router.push({ name: 'studentCourse' ,params:{"cid":this.zhibocid}})
    },
    enterCourse(cid){

      this.$router.push({ name: 'studentCourse' ,params:{"cid":cid}})
      },
    
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.pagebody{
  width: 100%;
  background-color: #f5f5f5;
  /* position: fixed; */
  overflow-y: scroll;
  max-width: 100vw;
  margin: 0 auto;
  overflow:hidden;
  height: calc(100%);
}

.box{
  background-color: white;
  border: 1px solid #797979;
  margin:50px;
  margin-top: 30px;
}

.headinfo{
  display: flex;
  margin-left: 30px;
  justify-content: space-between; /* 两端对齐 */
  align-items: center;
}

.headinfo h1{
  font-size: 30px;
}

.tab-pane{
  margin-left: 20px;
}
h2{
  font-size: 20px;
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

button{
  background-color: white;
  border:2px solid #F59A23;
  color: black;
  font-size: 15px;
  border-radius: 10px; 
  height: 45px;
  width: 100px;
  margin-top: 10px;
}

.steambox{
  background-color: white;
  border: 1px solid #797979;
  width:250px;
  margin:0 auto;
  margin-top: 10px;
}

.steambox button{
  margin-bottom: 10px;
}

.steambox h4{
  margin-bottom: 0;
}
</style>
