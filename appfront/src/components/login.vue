<template>


</template>

<script>
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
                this.$store.commit('login');
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
