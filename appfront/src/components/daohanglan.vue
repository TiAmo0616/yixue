<template>
    <!-- 说明：通过isLoggedIn区分已登录导航栏和未登录导航栏的差别，对应不同的内容，以下是示例 -->
    <p v-if="isLoggedIn">Welcome, {{ username }}! You are logged in.</p>
    <p v-else>Please login to access this page.</p>
</template>

<script>
import logo from "../assets/logo.png"

export default {
  name: 'daohanglan',
  
  data () {
    return {
      logo,
      isloged:false
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
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
