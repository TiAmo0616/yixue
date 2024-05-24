<template >
<div >
  <Daohanglan :isLoggedIn="isLoggedIn" :username="username"></Daohanglan>

  <div v-show="show" class="pagebody" >
    
      <el-row :gutter="20">

        <!-- 用户信息 -->
        <el-col :span="16">
          <div class="userinfo">
            <div class="title">
              <p>基本信息</p>
              <!-- <el-button type="text" @click="dialogFormVisible = true"><img src="../assets/userinfo/pencil.svg" width="20px" /></el-button> -->
            </div>

            <el-row>
              <el-col :span="6">
                <div class="pic">
                  <img :src="image" alt=""/>
                  <el-button @click="uploadVisible = true" class="btn" >更换头像</el-button>
                  
                </div>
              </el-col>

              <el-col :span="18">                
                <div class="info">
                  <div>
                    <h3>姓名：</h3>                  
                    <p>{{ name }}</p>
                  </div>

                  <div>
                    <h3>身份：</h3>                  
                    <p>{{ role }}</p>
                  </div>
                  <div>
                  <h3>性别：</h3>                 
                  <p>{{ sex }}</p>
                  </div>

                  <div>
                    <h3>个人简介：</h3>
                    <p>{{ info }}</p>
                  </div>
                </div>
              </el-col>
              </el-row>
                    
          </div>
        </el-col>

        <!-- 右侧两块 -->
        <el-col :span="8">
          <div class="changebtn">
            <div class="pw">
              <p>修改密码</p>
              <el-button @click="passwdFormVisible = true" class="btn">修改密码</el-button>
            </div>

            <div class="cancel">
              <p>注销</p>
              <el-button @click="zhuxiaoFormVisible = true" class="btn" >注销账号</el-button>
            </div>
          </div>
        </el-col>
      </el-row>

      <div class="lastline">
        <p>Copyright © 2024 GoodGoodStudy. All rights reserved. </p>
      </div>
      
    </div>


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


    <!-- 修改信息 -->
    <el-dialog title="修改个人信息" :visible.sync="dialogFormVisible">
      <el-form :model="form">
        <el-form-item label="姓名" :label-width="formLabelWidth">
          <el-input v-model="name" autocomplete="off" clearable></el-input>
        </el-form-item>
        <el-form-item label="性别" :label-width="formLabelWidth">
          <el-select v-model="sex" placeholder="请选择性别">
            <el-option
                    v-for="item in options"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                  </el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="个人简介" :label-width="formLabelWidth">
          <el-input v-model="info" autocomplete="off" clearable type="textarea" :rows="2" placeholder="请输入内容"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="submitInfo">确 定</el-button>
      </div>
    </el-dialog>


    <!-- 修改密码 -->
    <el-dialog title="修改密码" :visible.sync="passwdFormVisible" width="40%">
      <el-form :model="form">
        <el-form-item label="请输入新密码" :label-width="formLabelWidth" >
          <el-input v-model="newPasswd" autocomplete="off" show-password></el-input>
        </el-form-item>       
        <el-form-item label="请重新输入密码" :label-width="formLabelWidth">
          <el-input v-model="confirm_newPasswd" autocomplete="off" show-password></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="passwdFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="submitPasswd">确 定</el-button>
      </div>
    </el-dialog>

    <!-- 确认是否注销 -->
    <el-dialog title="注销账号" :visible.sync="zhuxiaoFormVisible" width="30%">
      
      <div slot="footer" class="dialog-footer">
        <el-button type="primary" @click="zhuxiaoFormVisible = false">取 消</el-button>
        <el-button @click="submitzhuxiao">确 定</el-button>
      </div>
    </el-dialog>

</div>

</template>

<script>
import axios from 'axios'
import Daohanglan from './daohanglan.vue';

export default {
  name: 'userInfo',
  components:{
    Daohanglan,
  },
  data () {
    return {

      zhuxiaoShow:false,
      editPassword:false,
      showUpload: true,
      fileList: [],
      newPasswd:'',
      confirm_newPasswd:'',
      upload:false,
      imageUrl: '',
      image: null,
      dialogVisible: false,
      fileParam: "",
      file: null,
      sex:'',
      info:'',
      edit:false,
      show:true,
      name:'',
      options: [{
          value: '男',
          label: '男'
        }, {
          value: '女',
          label: '女'
        }, ],      
      dialogFormVisible: false,
      passwdFormVisible: false,
      zhuxiaoFormVisible: false,
      uploadVisible: false,
      formLabelWidth: '120px'
    }
  },
  created(){
    axios.post("http://127.0.0.1:8000/showInfo/",{'username':this.username},{
      headers: {
        'Content-Type': 'multipart/form-data'
      }
  })
      .then(response =>{
        console.log(response.data)
        this.name = response.data.name
        this.sex = response.data.sex
        this.info = response.data.info
        this.image = response.data.img
        // this.image = require("../assets/logo.png")
        console.log(response.data.img)
        //require("../assets/logo.png")
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
    }
  },
  methods:{
    submitzhuxiao(){
      axios.post("http://127.0.0.1:8000/deleteUser/",{'username':this.username},{
      headers: {
        'Content-Type': 'multipart/form-data'
      }
  })
      .then(response =>{
        console.log(response.data)
        if(response.data.status == 'success'){
          this.zhuxiaoFormVisible=false;
          this.$store.commit("logout")
          this.$router.push({ name: 'mainpage'});
        }
         
      })
      .catch(error => {
        
        console.error('Error:', error);
      });
    },
    zhuxiao(){
      this.show = false
      this.zhuxiaoShow = true
    },
    zhuxiaoback(){
      this.zhuxiaoShow =  false
      this.show = true
    },
    editInfo(){
      this.show = false
      this.edit = true
    },
    changePasswd(){
      this.editPassword = true
      this.show = false
    },
    submitPasswd(){
      if (this.newPasswd == this.confirm_newPasswd){
        axios.post("http://127.0.0.1:8000/changePasswd/",{'username':this.username,'passwd':this.newPasswd},{
      headers: {
        'Content-Type': 'multipart/form-data'
      }
  })
      .then(response =>{
        console.log(response.data)
        if(response.data.status == 'success'){
          this.editPassword = false
          this.show = true
        }
         
      })
      .catch(error => {
        
        console.error('Error:', error);
      });

      this.passwdFormVisible = false;
      }
      else{
        alert("两次输入的密码不同！")
      }
    },
    submitInfo(){
      axios.post("http://127.0.0.1:8000/edit/",{'username':this.username,'sex':this.sex,'info':this.info,'name':this.name},{
      headers: {
        'Content-Type': 'multipart/form-data'
      }
  })
      .then(response =>{
        console.log(response.data)
        if(response.data.status == 'success'){
          this.edit = false
          this.show = true
        }
         
      })
      .catch(error => {
        
        console.error('Error:', error);
      });
      this.dialogFormVisible = false; 
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
      this.fileParam.append('username',this.username)
    },
    handleFileUpload() {
      const formData = new FormData();
      formData.append('image', this.file);
      formData.append('username',this.username)
      console.log(this.fileParam)
      axios.post("http://127.0.0.1:8000/handleImage/", this.fileParam)
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
  padding-bottom: 0;
}

.pagebody{
  width: 100%;
  height: 100%;
  background-color: #f5f5f5;
  /* position: fixed; */
  height: 100vh;
  overflow-y: scroll;
  max-width: 100vw;
  margin: 0 auto;
  overflow:hidden;
}

.userinfo{
  background-color: white;
  border: 1px solid #797979;
  margin-top:30px;
  margin:30px 0 30px 50px;
}

.pic img{
  
	object-fit: cover;		
  width:100px;
  height:100px;
}
.title{
  display: flex;
}

.title p{
  font-size: 20px;  
  font-weight: bold;
  margin: 30px;
  margin-top: 10px;
  text-align: left;
}

.title button{
  border:0;
  background-color: white;
  padding: 0;
  margin-top: 15px;
  height: 20px;
}

.info p{
  text-align: left;
  margin-top: 0;
  
}

.info h3{
  text-align: left;
  margin-left: 50px;
  margin-top: 0;
}

.info div{
  display: flex;
  align-items: baseline;
  margin-bottom: 20px;
}

.pw,.cancel{
  background-color: white;
  border: 1px solid #797979;
  margin:30px 50px 30px 50px;
}

.changebtn p{
  font-size: 20px;  
  font-weight: bold;
  margin: 30px;
  margin-top: 10px;
  text-align: left;
}

/* .changebtn button{
  background-color: white;
  border:3px solid #F59A23;
  color: black;
  height: 40px;
  font-size: 15px;
  font-weight: bold;
  margin-top: 20px;
  border-radius: 10px;
  margin-bottom: 20px;
} */

.lastline p{
  position: relative;
  bottom: 0;
  font-size: 10px;  
}

.btn{
  background-color: white;
  border:2px solid #F59A23;
  color: black;
  
  font-size: 15px;
  border-radius: 10px;
  margin-bottom: 20px;
}


</style>
