<template>
    <div>
         <!-- 导航栏 -->
         <div>
            <Daohanglan :isLoggedIn="isLoggedIn" :username="username"></Daohanglan>
        </div>
        <!-- 返回 -->
        <div class="backbox">
          <button @click="goBack" class="backbtn">
            <img
              src="../assets/image/lessoninfo/left.svg"
              alt="logo"
              class="back-icon"
            />
          </button>
          <p class="back-text">| 返回</p>
        </div>
        
        <div class="pagebody">
          <div class="box">
        <!-- 显示所有题目 -->
        <div>
            <el-row v-for="question in questions" :key="question.qid" class="qbox">
                <div v-if="question.kind == '单选题'">
                    ({{ question.score }}分)
                    {{ question.qname }}
                    {{ question.kind }}
                    <br>
                    {{ question.info }}
                    <br>
                    <el-radio-group v-model="answers[question.qid]"  
        @input="updateInputAnswer(question.kind,question.qid, $event.target.value)"  >
                        <el-radio :label="1">A.{{ question.a }}</el-radio>
                        <el-radio :label="2">B.{{ question.b }}</el-radio>
                        <el-radio :label="3">C.{{ question.c }}</el-radio>
                        <el-radio :label="4">D.{{ question.d }}</el-radio>
                    </el-radio-group>
                </div>

                <div v-else-if="question.kind == '判断题'">
                   ({{ question.score }}分)
                    {{ question.qname }}
                    {{ question.kind }}
                    <br>
                    {{ question.info }}
                    <br>
                    <el-radio-group v-model="answers[question.qid]"  
        @input="updateInputAnswer(question.kind,question.qid, $event.target.value)">
                        <el-radio :label="5">正确</el-radio>
                        <el-radio :label="6">错误</el-radio>
                    </el-radio-group>
                </div>
                
                <div v-else-if="question.kind =='填空题'">
                    ({{ question.score }}分)
                    {{ question.qname }}
                    {{ question.kind }}
                    <br>
                    {{ question.info }}

                    <el-input placeholder="请输入内容"
                    v-model="answers[question.qid]"  
        @input="updateInputAnswer(question.kind,question.qid, $event.target.value)"
                    clearable class="writebox">
                    </el-input>

                </div>
               <div v-else>
                ({{ question.score }}分)
                {{ question.qname }}
                    {{ question.kind }}
                    <br>
                    {{ question.info }}

                <el-input
                type="textarea"
                :rows="5"
                placeholder="请输入内容"
                v-model="answers[question.qid]"  
        @input="updateInputAnswer(question.kind,question.qid, $event.target.value)"  class="writebox"></el-input>
                
               </div>

           </el-row>
        </div>
    <!-- 提交 -->
    <button @click="submitAnswers" class="submit">提交</button>
        </div>
  </div>
  </div>
</template>

<script>
import axios from 'axios'
import Daohanglan from './daohanglan.vue';
import Mainpage from './mainpage.vue';
export default {
  name: 'homework',
  props: ['wid','cid'],
  components:{
    Daohanglan,
    Mainpage,
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
    }
  },
  data () {
    return {
      questions:[],
      answers:{},
      ans:'',
      input:'',
      textarea:'',
    }
  },
  created(){
    axios.post("http://127.0.0.1:8000/showQuestions/",
        {'wid':this.wid},{
      headers: {
        'Content-Type': 'multipart/form-data'
      }
  })
      .then(response =>{
        console.log(response.data)
        if(response.data.status == 'success'){
          this.questions = response.data.qs
        }
         
      })
      .catch(error => {
        console.error('Error:', error);
      });
  },
  methods:{
    updateInputAnswer(kind,qid, value) {
        this.answers[qid] = value;
        // console.log(kind)
        // if(kind == '单选题'){
        //     if(value == 1){
        //         this.answers[qid] = 'A'
        //     }
        //     else if(value == 2){
        //         this.answers[qid] = 'B'
        //     }
        //     else if (value == 3){
        //         this.answers[qid] = 'C'
        //     }
        //     else{
        //         this.answers[qid] = 'D'
        //     }
        // }
        // else if(kind=='判断题'){
        //     if(value == 1){
        //         this.answers[qid] = '正确'
        //     }
        //     else{
        //         this.answers[qid] = '错误'
        //     }
        // }
        // else{
        //     this.answers[qid] = value;
        // }
      
    },
    submitAnswers(){
        console.log(this.answers)
        const jsonData = JSON.stringify(this.answers);
        axios.post("http://127.0.0.1:8000/saveWork/",
        {'wid':this.wid,'answers':jsonData,'name':this.username},{
      headers: {
        'Content-Type': 'multipart/form-data'
      }
  })
      .then(response =>{
        console.log(response.data)
        this.$message({
          message: '您已成功提交！',
          type: 'success'
        });
        this.$router.push({ name: 'studentCourse' ,params:{'cid':this.cid}})
      })
      .catch(error => {
        console.error('Error:', error);
      });
    },
    goBack(){
        this.$router.push({ name: 'studentCourse' ,params:{'cid':this.cid,'wid':this.wid}})
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

.pagebody {
  width: 100%;
  background-color: #f5f5f5;
  /* position: fixed; */
  overflow-y: scroll;
  max-width: 100vw;
  margin: 0 auto;
  overflow: hidden;
  height: calc(100%);
}

.box {
  background-color: white;
  border: 1px solid #797979;
  margin: 50px;
  margin-top: 30px;
}

.qbox{
  margin-top: 20px;
}

.submit{
  background-color: #f59a23b0;
  color: white;
  border: #f59a23;
  font-size: 15px;
  border-radius: 10px;
  margin-top: 20px;
  margin-bottom: 20px;
  margin-left: 10px;
  margin-right: 20px;
  height: 40px;
  width: 80px;
}

.writebox{
  width: 70vw;
  margin: 0 auto;
  margin-top: 30px;
  display: flex; 
  align-items: flex-start; 
  position: relative;
}
</style>
