<template>
    <div>
         <!-- 导航栏 -->
         <div>
            <Daohanglan :isLoggedIn="isLoggedIn" :username="username"></Daohanglan>
        </div>
        <!-- 显示所有题目 -->
        <div>
            <el-row v-for="question in questions" :key="question.qid">
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
                    clearable>
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
        @input="updateInputAnswer(question.kind,question.qid, $event.target.value)"  ></el-input>
                
               </div>

           </el-row>
        </div>
    <!-- 提交 -->
    <button @click="submitAnswers">提交</button>
    </div>

</template>

<script>
import axios from 'axios'
import Daohanglan from './daohanglan.vue';
export default {
  name: 'homework',
  props: ['wid','cid'],
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
