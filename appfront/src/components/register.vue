<template>


</template>

<script>
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
