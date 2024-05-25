<template>
<div>
  <Daohanglan :isLoggedIn="isLoggedIn" :username="username"></Daohanglan>
   <div>
      <!-- <img :src="course.img" alt="" width="200"/>          -->
      <img :src="image" alt=""  width="200"/>
      <el-button @click="uploadVisible = true" class="btn" >更换头像</el-button>
      {{ this.cname }}
      课程码{{ this.cid }}     
      课程简介{{ this.intro }}
      学生人数：{{ course.stuNum }}
      学时:{{ this.xueshi }}
      课程状态{{ course.status }}
      任课教师{{ this.teacher }}
   </div>
   <el-button type="text" @click="dialogFormVisible = true"><img src="../assets/userinfo/pencil.svg" width="20px" /></el-button>
   <button @click="deleteCourse">删除课程</button>
   <button @click="back">返回</button>
   <!-- 修改信息 -->
   <el-dialog title="修改个人信息" :visible.sync="dialogFormVisible">
      <el-form :model="form">
        <el-form-item label="课程名" :label-width="formLabelWidth">
          <el-input v-model="cname" autocomplete="off" clearable></el-input>
        </el-form-item>
        <el-form-item label="学时" :label-width="formLabelWidth">
          <el-input v-model="xueshi" autocomplete="off" clearable></el-input>
        </el-form-item>
        <el-form-item label="任课教师" :label-width="formLabelWidth">
          <el-input v-model="teacher" autocomplete="off" clearable></el-input>
        </el-form-item>
        <el-form-item label="课程简介" :label-width="formLabelWidth">
          <el-input v-model="intro" autocomplete="off" clearable type="textarea" :rows="2" placeholder="请输入内容"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="submitInfo">确 定</el-button>
      </div>
    </el-dialog>

    <!-- 修改头像 -->
    <el-dialog title="修改头像" :visible.sync="uploadVisible" width="30%">
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

      <div slot="footer" class="dialog-footer">
        <el-button  @click="uploadVisible = false">取 消</el-button>
        <el-button type="primary" @click="handleFileUpload">确 定</el-button>
      </div>
    </el-dialog>



</div>
</template>

<script>
import axios from 'axios'
import Daohanglan from './daohanglan.vue';
export default {
  name: 'lessonInfo',
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
    },
    currentrole(){
      return this.$store.state.username.currentrole;
  }
  },
  data () {
    return {
      course:'',
      cname:'',
      intro:'',
      xueshi:'',
      teacher:'',
      dialogVisible: false,
      uploadVisible: false,
      formLabelWidth: '120px',
      dialogFormVisible: false,
      uploadVisible: false,
      fileList: [],
      imageUrl: '',
      image: null,
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
          this.cname=  this.course.cname
          this.intro = this.course.introduction
          this.xueshi = this.course.xueshi
          this.teacher = this.course.teacher
          this.image = this.course.img
        }
         
      })
      .catch(error => {
        console.error('Error:', error);
      });
      this.getmp4List()
      this.searchLM()
  },
  methods:{
    back(){
      this.$router.push({ name: 'teacherPage' })
    },
    deleteCourse(){
      axios.post("http://127.0.0.1:8000/deleteCourse/",{'cid':this.cid},{
        headers: {
          'Content-Type': 'multipart/form-data'
        }
    })
        .then(response =>{
          console.log(response.data)
          if(response.data.status == 'success'){
            alert("删除成功！")
            this.$router.push({ name: 'teacherPage' })
          }
          
        })
        .catch(error => {
          
          console.error('Error:', error);
        });
      
    },
    submitInfo(){
      axios.post("http://127.0.0.1:8000/editCourse/",{'cid':this.cid,'cname':this.cname,'intro':this.intro,'xueshi':this.xueshi,'teacher':this.teacher},{
      headers: {
        'Content-Type': 'multipart/form-data'
      }
  })
      .then(response =>{
        console.log(response.data)
        if(response.data.status == 'success'){
          this.dialogFormVisible = false; 
          
        }
         
      })
      .catch(error => {
        
        console.error('Error:', error);
      });
      
    },
    handleRemove(file, fileList) {
            this.fileList.pop();
            console.log(file, fileList);
        },
    handlePictureCardPreview(file) {
            this.dialogImageUrl = file.url;          
            this.dialogVisible = true;
        },
   
    uploadImage(){
      this.upload = true
    },
    handleChange(file,fileList){
      this.fileParam = new FormData(); //创建form对象
      this.fileParam.append("file", file["raw"]);
      this.fileParam.append("fileName", file["name"]);
      this.fileParam.append('cid',this.cid)
    },
    handleFileUpload() {
      const formData = new FormData();
      formData.append('image', this.file);
      formData.append('cid',this.cid)
      console.log(this.fileParam)
      axios.post("http://127.0.0.1:8000/changeImage/", this.fileParam)
        .then(response => {
          this.fileList = []
          this.upload = false
          // this.fileList.push(response.data)
          this.image = (response.data.url)
          // this.dialogImageUrl = response.data.url
          console.log(response.data)
        })
        .catch(error => {
          console.error('Error:', error);
        });
        this.uploadVisible=false;
    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
