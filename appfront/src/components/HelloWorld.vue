<template>
  <div class="hello">
    
    <h2>登录</h2>  
    <form @submit.prevent="handleSubmit">  
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
  name: 'HelloWorld',
  data () {
    return {
      username: '',  
      password: '',  
      msg: 'Welcome to Your Vue.js App'
    }
  },
  methods:{
    handleSubmit(){
      axios.post("http://127.0.0.1:8000/login/",{'username':this.username,'password':this.password},{
      headers: {
        'Content-Type': 'multipart/form-data'
      }
  })
      .then(response =>{
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
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
