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
        <button @click="gotoCreate">新建课程</button>
        <div>
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
        </div>
    </div>
    <!-- 新建课程，点击按钮触发显示 -->
    <div v-show="createShow" class="modal">
        <div class="modal-content">
            <form @submit.prevent="submitInfo">  
                <div class="form-group">  
                    <label for="username">课程名称:</label>  
                    <input type="text" v-model="cname" required>  
                </div>  
                <div class="form-group">  
                    <label for="password">授课教师:</label>  
                    <input type="text" v-model="teacher" required>  
                </div> 
                <div class="form-group">  
                    <label for="password">学时:</label>  
                    <input type="text" v-model="xueshi" required>  
                </div>  
                <div class="form-group">  
                    <label for="info">课程介绍：</label>  
                    <input type="textarea" v-model="introduction" required>  
                </div>  
                <div class="form-group">
                    上传课程封面：
                    <el-upload
                    v-model="fileList"
                        ref="uploadref"
                        action="#"
                        :auto-upload="false"
                        list-type="picture"
                        :on-preview="handlePictureCardPreview"
                        :on-change="handleChange"
                        :on-remove="handleRemove"
                    >
                        <i class="el-icon-plus"></i>
                    </el-upload>
                </div>
                <button type="submit">确认创建</button>  
                </form>  
                <button type="submit" @click="createback">取消</button>  
        </div>
    </div>

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
      return this.$store.state.username;
    },
    role() {
      return this.$store.state.role;
    },
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
     

    }
  },
  methods:{
    handleRemove(file, fileList) {
            this.fileList.pop();
            console.log(file, fileList);
    },
    handlePictureCardPreview(file) {
            this.dialogImageUrl = file.url;
           
            this.dialogVisible = true;
    },
    handleChange(file,fileList){
      this.fileParam = new FormData(); //创建form对象
      this.fileParam.append("file", file["raw"]);
      this.fileParam.append("fileName", file["name"]);
      this.fileParam.append('username',this.username)

    },
    gotoCreate(){
        this.createShow = true
    },
    createback(){
        this.createShow = false
    },
    submitInfo(){
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

</style>
