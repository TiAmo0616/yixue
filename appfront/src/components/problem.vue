<template>
<div>
    <!-- 导航栏 -->
    <div>
        <Daohanglan :isLoggedIn="isLoggedIn" :username="username"></Daohanglan>
    </div>
    <!-- 提问的问题 -->
    <div>
        {{ info }}
        提问者{{ asker }}
        提问时间{{ askTime }}
        <div v-if="jh == 1">精华</div>
    </div>
    <!-- 所有回复 -->
    <div>
        <el-row v-for="ans in answers" :key="ans.aid">
            {{ ans.info }}
            回复者{{ ans.answerer }}
            回复时间{{ ans.answerTime }}
            
            <button v-if="ans.answerer == username" @click="deleteAnswer(ans.aid)">删除</button>
        </el-row>
    </div>
    <!-- 写回复 -->
    <div>
        <el-input type="textarea" :rows="2" placeholder="请输入内容" v-model="answerText"></el-input>
        <button @click="huifu">回复</button>
    </div>
    <button @click="back">返回</button>
</div>

</template>

<script>
import axios from 'axios'
import Daohanglan from './daohanglan.vue';

export default {
  name: 'problem',
  props: ['cid','pid'],
  components:{
    Daohanglan,
  },
  computed: {
    isLoggedIn() {
      return this.$store.state.isLoggedIn;
    },
    username() {
      return this.$store.state.username.username;
    },
    role() {
      return this.$store.state.username.role;
    },
    currentrole(){
      return this.$store.state.username.currentrole;
  }
  },
  data () {
    return {
      info:'',
      asker:'',
      askTime:'',
      jh:'',
      resolved:'',
      answers:[],
      answerText:'',

    }
  },
  created(){
    axios.post("http://127.0.0.1:8000/searchProblem/",{'cid':this.cid,'pid':this.pid},{
      headers: {
        'Content-Type': 'multipart/form-data'
      }
  })
      .then(response =>{
        console.log(response.data)
        if(response.data.status == 'success'){
          this.info = response.data.info
          this.asker = response.data.asker
          this.askTime = response.data.t
          this.jh = response.data.jh
          this.resolved = response.data.resolved
          this.answers = response.data.res
        }
         
      })
      .catch(error => {
        console.error('Error:', error);
      });
  },
  methods:{
    back(){
        if(this.currentrole == '学生'){
            this.$router.push({ name: 'studentCourse' ,params:{'cid':this.cid}})
        }else{
            this.$router.push({ name: 'singleCourse' ,params:{'cid':this.cid}})
        }
    },
    deleteAnswer(aid){
        axios.post("http://127.0.0.1:8000/deleteAnswer/",{'aid':aid,},{
      headers: {
        'Content-Type': 'multipart/form-data'
      }
  })
      .then(response =>{
        console.log(response.data)
        if(response.data.status == 'success'){
          alert("删除成功！")
          this.showAns()
        }
         
      })
      .catch(error => {
        console.error('Error:', error);
      });
    },
    huifu(){
        axios.post("http://127.0.0.1:8000/createAnswer/",{'cid':this.cid,'pid':this.pid,'ans':this.answerText,'answerer':this.username},{
      headers: {
        'Content-Type': 'multipart/form-data'
      }
  })
      .then(response =>{
        console.log(response.data)
        if(response.data.status == 'success'){
            this.answerText = ''
          alert("回复成功！")
          this.showAns()
        }
         
      })
      .catch(error => {
        console.error('Error:', error);
      });
    },
    showAns(){
        axios.post("http://127.0.0.1:8000/showAns/",{'pid':this.pid},{
      headers: {
        'Content-Type': 'multipart/form-data'
      }
  })
      .then(response =>{
        console.log(response.data)
        if(response.data.status == 'success'){
          this.answers = response.data.res
        }
         
      })
      .catch(error => {
        console.error('Error:', error);
      });
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
