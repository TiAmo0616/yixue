<template>
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
        axios.post("http://127.0.0.1:8000/login/",{'username':this.username,'password':this.password},{
        headers: {'Content-Type': 'multipart/form-data'}
    })
        .then(response =>{
            console.log(response.data)
            if(response.data.status == 'success'){
                const role = response.data.role
                this.$store.commit('login',this.username,role);
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

</style>
