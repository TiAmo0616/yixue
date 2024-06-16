<template>
    <div>
      <!-- 返回 -->
    <div class="backbox">
      <button @click="back" class="backbtn">
        <img
          src="../assets/image/lessoninfo/left.svg"
          alt="logo"
          class="back-icon"
        />
      </button>
      <p class="back-text">| 返回</p>
    </div>

      
        <video id="videoPlayer" width="1200" height="600" controls type="video/mp4">
        Your browser does not support the video tag.
        </video>
        
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
.backbox {
  width: 100%;
  display: flex;
}
.backbtn {
  display: inline-block;
  vertical-align: middle;
  border: 0;
  background-color: transparent;
}

.back-icon {
  display: inline-block;
  vertical-align: middle;
  width: 30px;
  height: auto;
}

.back-text {
  display: inline-block;
  vertical-align: middle;
  font-size: 20px;
}
</style>
