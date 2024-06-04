<template>
<div>
    <!-- 导航栏 -->
    <div>
        <Daohanglan :isLoggedIn="isLoggedIn" :username="username"></Daohanglan>
    </div>
    <!-- 我的课堂 -->
    <div class='pagebody'>
      <div class='box'>
        <div class='headinfo'>
          <h1>我的课堂</h1>
          <button @click="createCourse" class="btn" >新建课程</button>
        </div>

        <div class="tab-pane">
          <el-tabs v-model="activeName" @tab-click="handleClick">
            <el-tab-pane label="全部课程" name="all"></el-tab-pane>
            <el-tab-pane label="进行中" name="ing"></el-tab-pane>
            <el-tab-pane label="已结束" name="done"></el-tab-pane>
          </el-tabs>
        </div>

        <el-row>
          <el-col :span="8" v-for="course in courses" :key="course.cid" :offset="index > 0 ? 2 : 0">
            <el-card shadow="hover" class="card ">
              
              <div @click="enter(course.cid)">
                <img :src="course.img" alt="" />
                <h2>{{ course.cname }}</h2>
              </div>
              <p>学生人数：{{ course.stuNum }}</p>
              <p>学时:{{ course.xueshi }}</p>
              <p>{{ course.status }}</p>
              
              <!-- <button @click="closeCourse(course.cid)" v-if="course.status == '进行中'">结束课程</button> -->
            </el-card>
          </el-col>
        </el-row>

        <!-- <div>
            <el-row v-for="course in courses" :key="course.cid">
                
                <img :src="course.img" alt="" width="200"/>
               <div @click="enter(course.cid)">
                {{ course.cname }}
               </div> 
                
               学生人数：{{ course.stuNum }}
               学时:{{ course.xueshi }}
               {{ course.status }}
                <button @click="closeCourse(course.cid)" v-if="course.status == '进行中'">结束课程</button>
            </el-row>
        </div> -->
      </div>

      <div class="lastline">
        <p>Copyright © 2024 GoodGoodStudy. All rights reserved. </p>
      </div>

      

    </div>

 
    <!-- 新建课程，点击按钮触发显示 -->
    <el-dialog title="新建课程" :visible.sync="newVisible" >
      <el-form :model="form">
        <el-form-item label="课程名称" :label-width="formLabelWidth">
          <el-input v-model="cname" autocomplete="off" clearable></el-input>
        </el-form-item>
        <el-form-item label="授课教师" :label-width="formLabelWidth">
          <el-input v-model="teacher" autocomplete="off" clearable></el-input>
        </el-form-item>
        <el-form-item label="学时" :label-width="formLabelWidth">
          <el-input v-model="xueshi" autocomplete="off" clearable></el-input>
        </el-form-item>
        
        <el-form-item label="课程介绍" :label-width="formLabelWidth">
          <el-input v-model="introduction" autocomplete="off" clearable type="textarea" :rows="2" placeholder="请输入内容"></el-input>
        </el-form-item>
        <el-form-item label="上传课程封面" :label-width="formLabelWidth">
        </el-form-item>
        <div class="modal-content">
            <el-upload
            v-model="fileList"
                ref="uploadref"
                action="#"
                accept="image/png,image/gif,image/jpg,image/jpeg"
                :auto-upload="false"
                list-type="picture-card"
                :on-preview="handlePictureCardPreview"
                :on-change="handleChange"
                :on-remove="handleRemove"
                >
                <i class="el-icon-plus"></i>
            </el-upload>
      </div>         
      </el-form>
      

      <div slot="footer" class="dialog-footer">
        <el-button  @click="newVisible = false">取 消</el-button>
        <el-button type="primary" @click="submitInfo">确 定</el-button>
      </div>
    </el-dialog>

</div>

</template>

<script>
import axios from 'axios'
import Daohanglan from './daohanglan.vue';
export default {
  name: 'teacherPage',
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
      createShow:false,
      cname:'',
      teacher:'',
      introduction:'',
      xueshi:'',
      fileList:[],
      fileParam:'',
      courses:[],
      newVisible:false,
      formLabelWidth: '120px'

    }
  },
  methods:{
    createCourse(){
      this.newVisible = true
      this.fileParam = new FormData(); //创建form对象
    },
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
    handleRemove(file, fileList) {
            this.fileList.pop();
            console.log(file, fileList);
    },
    handlePictureCardPreview(file) {
            this.dialogImageUrl = file.url;
           
            this.dialogVisible = true;
    },
    handleChange(file,fileList){
      
      this.fileParam.append("file", file["raw"]);
      this.fileParam.append("fileName", file["name"]);
      

    },
    gotoCreate(){
        this.createShow = true
    },
    createback(){
        this.createShow = false
    },
    submitInfo(){
      this.fileParam.append('username',this.username)
      this.fileParam.append('cname',this.cname)
      this.fileParam.append('teacher',this.teacher)
      this.fileParam.append('introduction',this.introduction)
      this.fileParam.append('xueshi',this.xueshi)
      axios.post("http://127.0.0.1:8000/createCourse/",this.fileParam,{
      headers: {
        'Content-Type': 'multipart/form-data'
      }
  })
      .then(response =>{
        console.log(response.data)
        if(response.data.status == 'success'){
        this.courses = response.data.courses
          this.createShow = false
          this.cname = ''
          this.teacher = ''
          this.introduction = ''
          this.fileList = []
          this.file = ''
          this.xueshi = ''
        }
         
      })
      .catch(error => {
        
        console.error('Error:', error);
      });
      this.newVisible = false;
    },
    closeCourse(cid){
      axios.post("http://127.0.0.1:8000/closeCourse/",{'cid':cid,'username':this.username},{
      headers: {
        'Content-Type': 'multipart/form-data'
      }
  })
      .then(response =>{
        console.log(response.data)
        if(response.data.status == 'success'){
          const fname = response.data.cname;
          alert("您已结束 "+fname+" 课程")
          this.courses = response.data.courses
        }
         
      })
      .catch(error => {
        
        console.error('Error:', error);
      });
      
    },
    listing(s){
      axios.post("http://127.0.0.1:8000/listing/",{'username':this.username,'s':s},{
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
    enter(cid){
      this.$router.push({ name: 'singleCourse' ,params:{"cid":cid}})
    }
  },
  created(){
    axios.post("http://127.0.0.1:8000/teacherCourse/",{'username':this.username},{
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
  width: 500px;
  height: 400px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

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

.headinfo button{
  background-color: white;
  border:2px solid #F59A23;
  color: black;
  font-size: 15px;
  border-radius: 10px; 
  height: 50px;
  margin-right: 30px;
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

/* .card button{
  background-color: #F59A23;
  border:1px solid;
  color: white;
  font-size: 15px;
  border-radius: 10px; 
  height: 40px;
} */

.lastline p{
  position: relative;
  bottom: 0;
  font-size: 10px;  
}
</style>
