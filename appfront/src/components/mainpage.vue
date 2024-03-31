<template>
<div>
    <Daohanglan :isLoggedIn="isLoggedIn" :username="username"></Daohanglan>
    
</div>

</template>

<script>

import Daohanglan from './daohanglan.vue';
export default {
  name: 'mainpage',
  props:{
    
    },
  components:{
    Daohanglan,
  },
  data () {
    return {
      islogged:false
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
    
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
