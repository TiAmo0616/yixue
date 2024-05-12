<template>
<div>
    <div id="backgroundpic" ></div>

    <div id="contents">
      <img src="../assets/image/logo2.0-removebg-preview.png" alt="logo" width="100px" />

      <div class="hello">
        <div id="topTitle">
          <p>登录</p>
          <p id="registertext">注册</p>
        </div>
          
        <form @submit.prevent="register">  

          <div class="form-group"> 
            
            <el-form ref="form" :model="form" label-width="0px" id="firstform">
              <el-form-item >
                <label><img src="../assets/image/register/people.svg" alt="logo" width="30px" /></label>
                <el-select v-model="role" placeholder="请选择身份" class="select-width">
                  <el-option label="老师" value="老师"></el-option>
                  <el-option label="学生" value="学生"></el-option>
                </el-select>
              </el-form-item>
            </el-form> 
          </div>

          <div class="form-group">
            <label for="username"><img src="../assets/image/register/userlogin.svg" alt="logo" width="30px" /></label>  
            <input type="text" id="username" placeholder=" 请输入用户名" v-model="username" required>  
          </div>  
          <div class="form-group">  
            <label for="password"><img src="../assets/image/register/key.svg" alt="logo" width="30px" /></label>  
            <input type="password" id="password" placeholder=" 请输入密码" v-model="password" required>  
          </div>  
          <div class="form-group">  
            <label for="password"><img src="../assets/image/register/redo.svg" alt="logo" width="30px" /></label>  
            <input type="password" id="password" placeholder=" 请重新输入密码" v-model="confirm_password" required>  
          </div>  
          <button id="btn" type="submit">注册</button>  
        </form>  
      </div>
    </div>
</div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'register',
  data () {
    return {
      username:'',
      password:'',
      confirm_password:'',
      role:''
    }
  },
  methods:{
    register(){
        if(this.password==this.confirm_password){
            axios.post("http://127.0.0.1:8000/register/",{'username':this.username,'password':this.password,'role':this.role},{
                headers: {'Content-Type': 'multipart/form-data'}})
                .then(response =>{
                    console.log(response.data)
                    if(response.data.status == 'success'){
                        this.$router.push({ name: 'login' });
                    }
                    else{alert("用户名已存在！")}
                    this.username=''
                    this.password=''
                    this.confirm_password=''
                    
                })
                .catch(error => {console.error('Error:', error); });
        }
        else{
            alert("密码不一致！请确认密码!")
            this.password=''
            this.confirm_password=''
        }
       
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

#backgroundpic{
background:url("../assets/image/background.jpg");
width:100%;
height:100%;
position:fixed;
background-size:100% 100%;
z-index:-1;
position: absolute;
  top: 0px;
}



#contents{
  background:rgba(255,255,255,0.6);
  position:relative;
  width: 70%;
  height: 450px;
  top: 0;left: 0;right: 0;bottom: 0;margin: auto;
  
}

.hello p{
  font-size: 20px;
  color: black;
  margin-bottom: 0;
}

#registertext{
  border-bottom: 5px solid #FAAF43;
}

#topTitle{
  padding-left: 50px;
  padding-right: 50px;
  padding-bottom: 0px;
  display:flex;
  justify-content: space-between;
  font-size: 0;
}

.form-group{
  margin:15px;
  vertical-align:middle;
}

.select-width {
  width: 500px; /* 您可以根据需要设置宽度 */
}

input{
  padding: 10px;
  border: 1px solid #DCDFE6;
  border-radius: 4px;
  width: 500px;
  box-sizing: border-box;
  vertical-align:middle;
  margin:2px;
}

input:focus{
outline:1px solid #409EFF;
}

input::placeholder{
  color: #C0C4CC;
  font-size: 14px;
}

label{
  vertical-align:middle;
}



#btn{
  background-color: #FAAF43;
  color: black;
  width: 550px;
  height: 40px;
  border: 1px;
  font-size: 15px;
  font-weight: bold;
  margin-top: 10px;
  border-radius: 10px;
  
}



</style>
