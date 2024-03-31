<template>
  <div class="hello">
    
    <h2>注册</h2>  
    <form @submit.prevent="register">  
      <div class="form-group">  
      我是
      <el-radio v-model="role" label="老师">老师</el-radio>
      <el-radio v-model="role" label="学生">学生</el-radio>
      </div> 
      <div class="form-group">  
        <label for="username">用户名:</label>  
        <input type="text" id="username" v-model="username" required>  
      </div>  
      <div class="form-group">  
        <label for="password">密码:</label>  
        <input type="password" id="password" v-model="password" required>  
      </div>  
      <div class="form-group">  
        <label for="password">确认密码:</label>  
        <input type="password" id="password" v-model="confirm_password" required>  
      </div>  
      <button type="submit">注册</button>  
    </form>  
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

</style>
