<template>
    <div>
        <video id="videoPlayer" width="1200" height="600" controls type="video/mp4">
        Your browser does not support the video tag.
        </video>
        <button @click="back">返回</button>
    </div>

</template>

<script>
export default {
  name: 'dianbo',
  props: ['cid','path','role'],
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  mounted(){
    console.log(this.path)
    document.getElementById('videoPlayer').src = "https://zlm.com/index/api/downloadFile?file_path="+this.path
  },
  methods:{
    back(){
        if(this.role == '学生'){
            this.$router.push({ name: 'studentCourse' ,params:{'cid':this.cid}})
        }
        else{
            this.$router.push({ name: 'singleCourse' ,params:{'cid':this.cid}})
        }
        
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
