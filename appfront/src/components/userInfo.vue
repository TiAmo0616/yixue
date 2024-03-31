<template>
<div>
  用户名：{{ username }}
  身份：{{ role }}
  性别：{{ sex }}
  个人简介：{{ info }}
  <div v-show="edit">
    <form @submit.prevent="submitInfo">  
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
</div>

</template>

<script>
export default {
  name: 'userInfo',
  data () {
    return {
      sex:'',
      info:'',
      edit:false
    }
  },

  computed: {
    isLoggedIn() {
      return this.$store.state.isLoggedIn;
    },
    username() {
      return this.$store.state.username;
    },
    role() {
      return this.$store.state.role;
    }
  },
  methods:{
    editInfo(){
      this.edit = true
    },
    submitInfo(){
      
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
