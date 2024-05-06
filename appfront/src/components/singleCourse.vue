<template>
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
                
        学生人数：{{ course.stuNum }}
        学时:{{ course.xueshi }}
        {{ course.status }}
    </div>
    <!-- 服务 -->
    <div>
        <el-tabs v-model="activeName" @tab-click="handleClick">
            <el-tab-pane label="学习资源" name="first">学习资源</el-tab-pane>
            <el-tab-pane label="作业" name="second">作业</el-tab-pane>
            <el-tab-pane label="问答" name="third">答疑</el-tab-pane>
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
            <button @click="gotofabu">发布</button>
            
        </div>

        <div>
            <el-row v-for="work in works" :key="work.wid">
               
                {{ work.wname }}
                
               开始时间{{ work.begin }}
               截止时间{{ work.end }}
               <button @click="deleteWork(work.wid)">删除</button>
               <button @click="setquestions(work.wid)">设置题目</button>
               <button @click="see(work.wid)">查看</button>
            </el-row>
        </div>
        <!-- 发布作业 -->
        <div v-show="fabushow" class="modal">
            <div class="modal-content">
            <form @submit.prevent="submitfabu">  
                <div class="form-group">  
                <label for="new_wname">作业标题：</label>  
                <input type="text" id="new_wname" v-model="new_wname" required>  
                </div>  
                
                <div class="form-group">  
                    <label for="info">开始时间</label>  
                    <el-date-picker
                        v-model="newbegin"
                        type="datetime"
                        placeholder="选择日期时间">
                    </el-date-picker>
                </div>  

                <div class="form-group">  
                    <label for="info">截止时间</label>  
                    <el-date-picker
                        v-model="newend"
                        type="datetime"
                        placeholder="选择日期时间">
                    </el-date-picker>
                </div>  

                <button type="submit">确认创建</button>  
                <button @click="workback">取消</button>
            </form>  
            </div>
        </div>
        <!-- 发布作业end -->
    </div>
    <!-- 问答 -->
    <div v-show="thirdshow">
        <div>
            <button @click="showProblem('my')">我的</button>
            <button @click="showProblem('jh')">精华</button>
            <button @click="showProblem('all')">全部</button>
            <button @click="gototiwen">发布</button>
        </div>

        
        <div>
            <el-row v-for="problem in problems" :key="problem.pid">
               {{ problem.pinfo }}
               用户{{ problem.askername }}
               <button @click="huifu(problem.pid)">回复</button>
            </el-row>
        </div>
        <!-- 去提问 -->
        <div v-show="tiwenShow" class="modal">
            <div class="modal-content">
            <form @submit.prevent="submitProblems">  
                <div class="form-group">  
                <label for="new_wname">请输入问题：</label>  
                <input type="textarea" v-model="new_pinfo" required>  
                </div>  

                <button type="submit">确认提问</button>  
                <button @click="tiwenback">取消</button>
            </form>  
            </div>
        </div>
        <!-- 提问结束 -->
    </div>
    <!-- 学生管理 -->
    <div v-show="fourthshow">

    </div>

</div>

</template>

<script>
import axios from 'axios'
import Daohanglan from './daohanglan.vue';
export default {

  name: 'singleCourse',
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
      activeName: 'first',
      firstshow:true,
      sencondshow:false,
      thirdshow:false,
      fourthshow:false,
      works:[],
      fabushow:false,
      new_wname:'',
      newbegin:'',
      newend:'',
      problems:[],
      tiwenShow:false,
      new_pinfo:''


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
  
  methods: {
    
    workback(){
        this.fabushow = false
        this.new_wname = ''
        this.newbegin = ''
        this.newend = ''
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
            this.showProblem('all')
        }
        else{
            this.firstshow = false
            this.sencondshow = false
            this.thirdshow = false
            this.fourthshow = true
        }
      },
      showWork(status){
        axios.post("http://127.0.0.1:8000/showWorks/",{'cid':this.cid,'status':status},{
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
      },
    gotofabu(){
        this.fabushow = true
      },
    submitfabu(){
        var moment = require('moment')
        let g = moment.utc(this.newbegin).toDate()
        let t = moment(g).format('YYYY-MM-DD HH:mm:ss')
        let eg = moment.utc(this.newend).toDate()
        let et = moment(eg).format('YYYY-MM-DD HH:mm:ss')

        axios.post("http://127.0.0.1:8000/createWork/",{'cid':this.cid,'wname':this.new_wname,'begin':t,'end':et},{
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    })
        .then(response =>{
            console.log(response.data)
            if(response.data.status == 'success'){
            this.works = response.data.works
            this.fabushow = false
            this.new_wname = ''
            this.newbegin = ''
            this.newend = ''
            }
            
        })
        .catch(error => {
            console.error('Error:', error);
        });
        },
    deleteWork(wid){
        axios.post("http://127.0.0.1:8000/deleteWork/",{'wid':wid},{
        headers: {'Content-Type': 'multipart/form-data'}
    })
        .then(response =>{
            console.log(response.data)
            if(response.data.status == 'success'){
                this.works = response.data.works
                alert("删除成功!")
            }
            
        })
        .catch(error => {
            console.error('Error:', error);
        });
    },
    setquestions(wid){
        this.$router.push({ name: 'setquestions' ,params:{"wid":wid,'cid':this.cid}})
    },
    see(wid){
        this.$router.push({ name: 'totalAnswer' ,params:{"wid":wid,'cid':this.cid}})
    },
    showProblem(status){
        axios.post("http://127.0.0.1:8000/showProblems/",{'cid':this.cid,'status':status,'username':this.username},{
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        })
            .then(response =>{
                console.log(response.data)
                if(response.data.status == 'success'){
                this.problems = response.data.problems
                }
                
            })
            .catch(error => {
                console.error('Error:', error);
            });
    },
    gototiwen(){
        this.tiwenShow = true
    },
    tiwenback(){
        this.tiwenShow = false
    },
    submitProblems(){
        axios.post("http://127.0.0.1:8000/saveProblems/",{'cid':this.cid,'info':this.new_pinfo,'username':this.username},{
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    })
        .then(response =>{
            console.log(response.data)
            if(response.data.status == 'success'){
            this.problems = response.data.problems
            this.tiwenShow = false
            this.new_pinfo = ''
            }
            
        })
        .catch(error => {
            console.error('Error:', error);
        });
    },
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.modal {
  position: fixed;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5); /* 半透明背景 */
  display: flex;
  justify-content: center;
  align-items: center;
}
.modal-content {
  background-color: #fff;
  padding: 20px;
  border-radius: 5px;
  width: 300px;
  height: 200px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
</style>
