<template>
<div>
  <Daohanglan :isLoggedIn="isLoggedIn" :username="username"></Daohanglan>
  <div v-show="show">
    <div>
      
            <img :src="image" alt="" />

        <el-button @click="uploadImage">更换头像</el-button>
    </div>
    姓名：{{ name }}
    身份：{{ role }}
    性别：{{ sex }}
    个人简介：{{ info }}
    <button @click="editInfo">修改</button>

    <div>
      <button @click="changePasswd">修改密码</button>
    </div>

    <div>
      <button @click="zhuxiao">注销账号</button>
    </div>

  </div>

  <!-- 修改头像 -->
  <div v-show="upload" class="modal">
        <div class="modal-content">
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
          <el-button @click="handleFileUpload">确认</el-button>
        </div>
      </div>

  <!-- 修改信息 -->
  <div v-show="edit" class="modal">
        <div class="modal-content">
          <form @submit.prevent="submitInfo">  
            <div class="form-group">  
              <label for="username">姓名:</label>  
              <input type="text" id="username" v-model="name" required>  
            </div>  
            <div class="form-group">  
              <label for="password">性别:</label>  
              <el-select v-model="sex" placeholder="请选择">
                <el-option
                  v-for="item in options"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
            </el-select>
            </div>  
            <div class="form-group">  
              <label for="info">个人简介：</label>  
              <input type="textarea" id="username" v-model="info" required>  
            </div>  
            <button type="submit">确认修改</button>  
          </form>  
        </div>
  </div>

  <!-- 修改密码 -->
  <div v-show="editPassword" class="modal">
        <div class="modal-content">
          <form @submit.prevent="submitPasswd">  
            <div class="form-group">  
              <label for="username">输入新密码:</label>  
              <input type="password" id="newPasswd" v-model="newPasswd" required>  
            </div>  
            
            <div class="form-group">  
              <label for="info">确认密码：</label>  
              <input type="password" id="confirm_newPasswd" v-model="confirm_newPasswd" required>  
            </div>  
            <button type="submit">确认修改</button>  
          </form>  
        </div>
  </div>

  <!-- 确认是否注销 -->
  <div v-show="zhuxiaoShow" class="modal">
        <div class="modal-content">
              请确定是否注销
          <button type="submit" @click="submitzhuxiao">确认注销</button>  
          <button type="submit" @click="zhuxiaoback">返回</button>  
        </div>
  </div>
  

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
