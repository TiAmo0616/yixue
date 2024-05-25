<template>
  <div>
    <div id="backgroundpic" ></div>
    
    

    <div id="contents">
      <img src="../assets/image/logo2.0-removebg-preview.png" alt="logo" width="100px" />
      
      

      <div class="hello">  
        <div id="topTitle">
          <p id="logintext">登录</p>
          <button @click="register" ><p>注册</p></button>
        </div> 
        
        
        <form @submit.prevent="login" id="login">  
          <div class="form-group">  
            <label for="username"><img src="../assets/image/login/userlogin.svg" alt="logo" width="50px" /></label>  
            <input type="text" id="username"  placeholder="请输入用户名" v-model="username" required> 
          </div>  
          <div class="form-group">  
            <label for="password"><img src="../assets/image/login/key.svg" alt="logo" width="50px" /></label>  
            <input type="password" id="password" placeholder="请输入密码" v-model="password" required>
          </div>         
          <button id="btn" type="submit" >登录</button>
        </form> 

        


      </div>
    </div>
  </div> 
</template>

<script>
import axios from 'axios'
export default {
  name: 'login',
  data () {
    return {
      username:'',
      password:'',

    }
  },
  methods:{
    login(){
        axios.post("http://127.0.0.1:8000/login/",{username:this.username,password:this.password},{
        headers: {'Content-Type': 'multipart/form-data'}
    })
        .then(response =>{
            console.log(response.data)
            if(response.data.status == 'success'){
                          // 一、使用本地存储localStorage实现登录存储的功能、
                
                const role = response.data.role
                this.$store.commit('login',{username:this.username,role:role,currentrole:role});
                localStorage.setItem('userInfo', {username:this.username,role:role,currentrole:role});
                this.$router.push({ name: 'mainpage' ,params:{"username":this.username,'role':role}});
            }
            else if(response.data.status == 'unmatch'){alert("用户名密码错误！")}
            else{alert("用户名不存在！")}
            this.username=''
            this.password=''
            
        })
        .catch(error => {console.error('Error:', error); });
    },
    register(){
        this.$router.push({ name: 'register' })
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
  width: 70%;
  height: 80vh;
  
  left: 0;right: 0;margin: auto;
  margin-top: 10vh;
  
}

.hello p{
  font-size: 30px;
  color: black;
  
}

#topTitle{
  padding-left: 50px;
  padding-right: 50px;
  display:flex;
  justify-content: space-between;
  margin:0;border:0;
  font-size: 0;
}

input{
  padding: 20px;
  border: 1px solid #DCDFE6;
  width: 60%;
  box-sizing: border-box;
  vertical-align:middle;
  margin: 20px;
  border-radius: 4px;
}

input:focus{
outline:1px solid #409EFF;
}

input::placeholder{
  color: #C0C4CC;
  font-size: 20px;
}

.form-group{
  margin:20px
}

label{
  vertical-align:middle;
}

form{
  margin: 20px;
  margin-top: 0px;
}

#btn{
  background-color: #FAAF43;
  color: black;
  width: 60%;
  height: 70px;
  border: 1px;
  font-size: 25px;
  font-weight: bold;
  margin-top: 50px;
  border-radius: 10px;
  
}

#logintext{
  border-bottom: 5px solid #FAAF43;
}

.hello button{
  border :0;
}
</style>