<!-- <template>
    <div class="hello">
    
    <h2>登录</h2>  
    <form @submit.prevent="login">  
      <div class="form-group">  
        <label for="username">用户名:</label>  
        <input type="text" id="username" v-model="username" required>  
      </div>  
      <div class="form-group">  
        <label for="password">密码:</label>  
        <input type="password" id="password" v-model="password" required>  
      </div>  
      <button type="submit">登录</button>  
    </form>  
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
                const role = response.data.role
                this.$store.commit('login',{username:this.username,role:role});
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

<style scoped>

</style> -->
<template>
  <div>
    <div id="backgroundpic" ></div>
    

    <div id="contents">
      <img src="../assets/image/logo2.0-removebg-preview.png" alt="logo" width="100px" />
      
      

      <div class="hello">  
        <div id="topTitle">
          <p id="logintext">登录</p>
          <p @click="register">注册</p>
        </div> 
        
        
        <form @submit.prevent="login" id="login">  
          <div class="form-group">  
            <label for="username"><img src="../assets/image/login/userlogin.svg" alt="logo" width="30px" /></label>  
            <input type="text" id="username" v-model="username" required>  
          </div>  
          <div class="form-group">  
            <label for="password"><img src="../assets/image/login/key.svg" alt="logo" width="30px" /></label>  
            <input type="password" id="password" v-model="password" required>
          </div>  
          <button id="btn" type="submit">登录</button>
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
                const role = response.data.role
                this.$store.commit('login',{username:this.username,role:role});
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
  width: 900px;
  height: 500px;
  top: 0;left: 0;right: 0;bottom: 0;margin: auto;
  
}

.hello p{
  font-size: 20px;
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
  padding: 10px;
  border: 1px solid black;
  margin: 15px;
  width: 500px;
  box-sizing: border-box;
  vertical-align:middle;
  margin: 20px;
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
  width: 580px;
  height: 50px;
  border: 1px;
  font-size: 15px;
  font-weight: bold;
  margin-top: 50px;
  
  
}

#logintext{
  border-bottom: 5px solid #FAAF43;
}
</style>