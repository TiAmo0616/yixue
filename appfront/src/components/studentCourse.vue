<template>
<!-- 学生端在我的课堂点击已选课程后进入的具体的课程页面 -->
<div>
      <!-- 导航栏 -->
  <div>
      <Daohanglan :isLoggedIn="isLoggedIn" :username="username"></Daohanglan>
  </div>
   <!-- 课程介绍 -->
   <div>
        <img :src="course.img" alt="" width="200"/>
              
        {{ course.cname }}
        课程码{{ this.cid }}     
                
        学时:{{ course.xueshi }}
        {{ course.status }}
    </div>
    <!-- 服务 -->
    <div>
        <el-tabs v-model="activeName" @tab-click="handleClick">
            <el-tab-pane label="学习资源" name="first">学习资源</el-tab-pane>
            <el-tab-pane label="作业" name="second">作业</el-tab-pane>
            <el-tab-pane label="问答" name="third">问答</el-tab-pane>
            <el-tab-pane label="学生管理" name="fourth">学生管理</el-tab-pane>
        </el-tabs>
    </div>
    <!-- 学习资源（录播课程） -->
    <div v-show="firstshow">
        
    </div>
     <!-- 作业 -->
     <div v-show="sencondshow">
        <div>
            <button @click="showWork('ing')">未截止</button>
            <button @click="showWork('ed')">已截止</button>
            <button @click="showWork('all')">全部</button>
        </div>

        <div>
            <el-row v-for="work in works" :key="work.wid">  
                {{ work.wname }}    
               开始时间{{ work.begin }}
               截止时间{{ work.end }}
               <button @click="write(work.wid)">去完成</button>
            </el-row>
        </div>
     </div>

</div>
</template>

<script>
import axios from 'axios'
import Daohanglan from './daohanglan.vue';
export default {
  name: 'studentCourse',
  props: ['cid'],
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
      course:'',
      works:[],
    }
  },
  created(){
    
    axios.post("http://127.0.0.1:8000/showCourse/",{'cid':this.cid},{
      headers: {
        'Content-Type': 'multipart/form-data'
      }
  })
      .then(response =>{
        console.log(response.data)
        if(response.data.status == 'success'){
          this.course = response.data.course
        }
         
      })
      .catch(error => {
        console.error('Error:', error);
      });
      
  },
  methods:{
    write(wid){
        this.$router.push({ name: 'homework' ,params:{"wid":wid,'cid':this.cid}})
    },
    handleClick(tab) {
        if(tab.name == 'first'){
            this.firstshow = true
            this.sencondshow = false
            this.thirdshow = false
            this.fourthshow = false
        }
        else if(tab.name == 'second'){
            axios.post("http://127.0.0.1:8000/showWorks/",{'cid':this.cid,'status':'all'},{
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        })
            .then(response =>{
                console.log(response.data)
                if(response.data.status == 'success'){
                this.works = response.data.works
                }
                
            })
            .catch(error => {
                console.error('Error:', error);
            });
            this.firstshow = false
            this.sencondshow = true
            this.thirdshow = false
            this.fourthshow = false
        }else if(tab.name == 'third'){
            this.firstshow = false
            this.sencondshow = false
            this.thirdshow = true
            this.fourthshow = false
        }
        else{
            this.firstshow = false
            this.sencondshow = false
            this.thirdshow = false
            this.fourthshow = true
        }
      },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
