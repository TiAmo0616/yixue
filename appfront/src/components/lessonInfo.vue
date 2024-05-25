<template>
<div>
  <Daohanglan :isLoggedIn="isLoggedIn" :username="username"></Daohanglan>
   <div>
      <img :src="course.img" alt="" width="200"/>         
      {{ course.cname }}
      课程码{{ this.cid }}     
      课程简介{{ this.intro }}
      学生人数：{{ course.stuNum }}
      学时:{{ this.xueshi }}
      课程状态{{ course.status }}
   </div>
   <el-button type="text" @click="dialogFormVisible = true"><img src="../assets/userinfo/pencil.svg" width="20px" /></el-button>

   <!-- 修改信息 -->
   <el-dialog title="修改个人信息" :visible.sync="dialogFormVisible">
      <el-form :model="form">
        <el-form-item label="课程名" :label-width="formLabelWidth">
          <el-input v-model="cname" autocomplete="off" clearable></el-input>
        </el-form-item>
        <el-form-item label="学时" :label-width="formLabelWidth">
          <el-input v-model="xueshi" autocomplete="off" clearable></el-input>
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
      dialogVisible: false,
      uploadVisible: false,
      formLabelWidth: '120px',
      dialogFormVisible: false,
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
        }
         
      })
      .catch(error => {
        console.error('Error:', error);
      });
      this.getmp4List()
      this.searchLM()
  },
  methods:{
    submitInfo(){
      axios.post("http://127.0.0.1:8000/editCourse/",{'cid':this.cid,'cname':this.cname,'intro':this.intro,'xueshi':this.xueshi},{
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
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
