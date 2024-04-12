<template>
    <div>
        <!-- 导航栏 -->
        <div>
            <Daohanglan :isLoggedIn="isLoggedIn" :username="username"></Daohanglan>
        </div>
        <!-- 返回 -->
        <div>
            <el-page-header @back="goBack">
            </el-page-header>
        </div>
        <!-- 学生信息 -->
        <div>
            我的答卷：
        </div>
        <div>
            <el-row v-for="question in questions" :key="question.qid">
                <div v-if="question.kind == '单选题'">
                    ({{ question.score }}分)
                    {{ question.qname }}
                    {{ question.kind }}
                    <br>
                    {{ question.info }}
                    <br>
                    <el-radio-group v-model="answers[question.qid]"  :disabled="true" >
                        <el-radio :label="1">A.{{ question.a }}</el-radio>
                        <el-radio :label="2">B.{{ question.b }}</el-radio>
                        <el-radio :label="3">C.{{ question.c }}</el-radio>
                        <el-radio :label="4">D.{{ question.d }}</el-radio>
                    </el-radio-group>
                    <div>
                        得分：
                        {{ question.score }}
                    </div>
                </div>

                <div v-else-if="question.kind == '判断题'">
                   ({{ question.score }}分)
                    {{ question.qname }}
                    {{ question.kind }}
                    <br>
                    {{ question.info }}
                    <br>
                    <el-radio-group v-model="answers[question.qid]"  :disabled="true">
                        <el-radio :label="5">正确</el-radio>
                        <el-radio :label="6">错误</el-radio>
                    </el-radio-group>
                    <div>
                        得分：
                        {{ question.score }}
                    </div>
                </div>
                
                <div v-else-if="question.kind =='填空题'">
                    ({{ question.score }}分)
                    {{ question.qname }}
                    {{ question.kind }}
                    <br>
                    {{ question.info }}

                    <el-input
                    v-model="answers[question.qid]"  
                    clearable
                    :disabled="true">
                    </el-input>

                    <div>
                        得分:
                        <el-input 
                            v-model="scores[question.qid]" 
                            :disabled="true" 
                            clearable>
                            </el-input>
                        点评：
                        <el-input 
                        :disabled="true"
                        type="textarea"
                        :rows="5"
                        v-model="judgements[question.qid]"  
                        clearable>
                        </el-input>

                    </div>
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
                
                :disabled="true"></el-input>
                
                <div>
                    得分:
                    <el-input 
                        v-model="scores[question.qid]"  
                        :disabled="true"
                        clearable>
                        </el-input>
                    点评：
                    <el-input 
                    type="textarea"
                    :rows="5"
                    v-model="judgements[question.qid]"  
                    :disabled="true"
                    clearable>
                    </el-input>
                </div>
               </div>
               
           </el-row>
           <button @click="back">返回</button>
        </div>
    </div>

</template>

<script>
import axios from 'axios'
import Daohanglan from './daohanglan.vue';
export default {
  name: 'myWork',
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
      scores:{},
      judgements:{},
    }
  },
  created(){
    axios.post("http://127.0.0.1:8000/seeStudentWork/",{'wid':this.wid,'name':this.username},{
      headers: {
        'Content-Type': 'multipart/form-data'
      }
  })
      .then(response =>{
        console.log(response.data)
        if(response.data.status == 'success'){
          this.questions = response.data.works
          this.answers = response.data.answers
          this.scores = response.data.scores
          this.judgements = response.data.judgements
        }
         
      })
      .catch(error => {
        console.error('Error:', error);
      });
  },
  methods:{
    back(){
        this.$router.push({ name: 'studentCourse' ,params:{'cid':this.cid,'wid':this.wid}})
    },
    goBack(){
        this.$router.push({ name: 'studentCourse' ,params:{'cid':this.cid,'wid':this.wid}})
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
