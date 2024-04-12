<template>
    <div>
        <!-- 导航栏 -->
        <div>
            <Daohanglan :isLoggedIn="isLoggedIn" :username="username"></Daohanglan>
        </div>
        <!-- 学生信息 -->
        <div>
            {{ name }}的答卷：
        </div>
        <!-- 显示作答情况 -->
        <div v-if="status == '待批改'">
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

                    <el-input placeholder="请输入内容"
                
                    v-model="answers[question.qid]"  
                    clearable
                    :disabled="true">
                    </el-input>

                    <div>
                        得分:
                        <el-input 
                            v-model="scores[question.qid]"  
                            @input="updatescore(question.qid, $event.target.value)" 
                            clearable>
                            </el-input>
                        点评：
                        <el-input 
                        type="textarea"
                        :rows="5"
                        v-model="judgements[question.qid]"  
                        @input="updatejudgement(question.qid, $event.target.value)" 
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
                        @input="updatescore(question.qid, $event.target.value)" 
                        clearable>
                        </el-input>
                    点评：
                    <el-input 
                    type="textarea"
                    :rows="5"
                    v-model="judgements[question.qid]"  
                    @input="updatejudgement(question.qid, $event.target.value)" 
                    clearable>
                    </el-input>
                </div>
               </div>
               
           </el-row>
           <!-- 提交批改 -->
            <div>
                <button @click="submitcheck">发布批改</button>
            </div>
        </div>
        <!-- 已批改，查看 -->
        <div v-else>
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
  name: 'judgeWork',
  props: ['wid','cid','name','status'],
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
    axios.post("http://127.0.0.1:8000/seeStudentWork/",{'wid':this.wid,'name':this.name},{
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
    updatescore(qid,value){
        scores[qid] = value
    },
    updatejudgement(qid,value){
        this.judgements[qid] = value
    },
    submitcheck(){
        const scoredata = JSON.stringify(this.scores);
        const judgedata = JSON.stringify(this.judgements);
        axios.post("http://127.0.0.1:8000/saveCheck/",
        {'judges':judgedata,'scores':scoredata,'name':this.name,'wid':this.wid},{
      headers: {
        'Content-Type': 'multipart/form-data'
      }
  })
      .then(response =>{
        console.log(response.data)
        alert('您已完成批改！')
        this.$router.push({ name: 'totalAnswer' ,params:{'cid':this.cid,'wid':this.wid}})
      })
      .catch(error => {
        console.error('Error:', error);
      });
    },
    back(){
        this.$router.push({ name: 'totalAnswer' ,params:{'cid':this.cid,'wid':this.wid}})
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
