<template>
    <!-- 具体课程显示页面 -->
<div>
    <!-- 导航栏 -->
    <div>
        <Daohanglan :isLoggedIn="isLoggedIn" :username="username"></Daohanglan>
    </div>
    <!-- 课程名称 -->
    <div>
        {{ courseName }}
    </div>
</div>

</template>

<script>
import Daohanglan from './daohanglan.vue';

export default {
  name: 'myCourse',
  components:{
    Daohanglan,
  },
  data () {
    return {
      
    }
  },
  created(){
    axios.post("http://127.0.0.1:8000/showCourse/",{'cid':this.cid},{
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
  methods:{

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
