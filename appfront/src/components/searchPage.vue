<template>
    <div>
        <button @click="back">返回</button>
        <div class="card">
        <el-row>
                <el-col :span="8" v-for="course in courses" :key="course.cid" :offset="index > 0 ? 2 : 0">
                <el-card shadow="hover" >                
                    <div @click="see(course.cid)">
                    <img :src="course.img" alt="" />
                    <h2>{{ course.cname }}</h2>
                    <h4>{{ course.teacher }}|{{ course.status }}</h4>
                    </div>                
                </el-card>
                </el-col>
            </el-row>
        </div>
    </div>


</template>

<script>
import axios from "axios";
export default {
  name: 'searchPage',
  props: ["info"],
  data () {
    return {
      courses:''
    }
  },
  methods:{
    see(cid){
        this.$router.push({ name: 'myCourse' ,params:{'cid':cid}})
    },   
    back(){
        this.$router.push({ name: 'mainpage'})
    },
  },
  created(){
    
    axios.post("http://127.0.0.1:8000/sousuo/",{'info':this.info},{
      headers: {
        'Content-Type': 'multipart/form-data'
      }
  })
      .then(response =>{
        console.log(response.data)
       this.courses = response.data.matches
         
      })
      .catch(error => {
        
        console.error('Error:', error);
      });
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.card{
  margin:10px;
  height:400px;
  padding: 0;
}

.card img{
  display: block; /* 使图片以块级元素显示 */
  margin-left: auto;
  margin-right: auto;
  width:100%;
  height: 200px;
  object-fit: cover;
}

.card p{
  margin:5px;
}

</style>
