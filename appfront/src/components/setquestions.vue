<template>
  <div>
    <!-- 导航栏 -->
    <div>
      <Daohanglan :isLoggedIn="isLoggedIn" :username="username"></Daohanglan>
    </div>
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

    <div class="pagebody">
      <!-- 提交本次作业设置 -->
      <button @click="back">提交本次作业设置</button>
      <div class="box">
        <!-- 一题一题设置 -->
        <div>
          <h3>请输入题目：</h3>
          <form @submit.prevent="saveq">
            <!-- 先选择题目类型 -->
            <div class="form-group">
              <el-radio-group v-model="kind" @change="showset">
                <el-radio :label="1">单选题</el-radio>
                <el-radio :label="2">判断题</el-radio>
                <el-radio :label="3">填空题</el-radio>
                <el-radio :label="4">简答题</el-radio>
              </el-radio-group>
            </div>

            <!-- 不同类型的设置方式不一样 -->
            <div v-show="v1">
              <!-- 设置分数 -->
              <div class="box1">
              <el-row :gutter="20">
                <el-col :span="6" :offset="6">
                  
                  <div class="form-group">
                    <label for="qname">题号</label>
                    <input
                      type="textarea"
                      id="qname"
                      v-model="qname"
                      required
                      this.input=""
                    />
                  </div>
                </el-col>
                <el-col :span="9">
                  <div>
                    本题分数：
                    <input type="text" v-model="qscore" required this.input="" />
                  </div>
                  
                </el-col>                
              </el-row>
</div>
              <div class="box2">
              <div class="form-group">

                <label for="info">题目要求</label>
                <input type="textarea" :rows="2"  v-model="info" id="info" required>
                
                
              </div>
              </div>
              <div>
                <h4>请输入各选项</h4>
                <el-row :gutter="20">
                  <el-col :span="6">
                    <h5>A</h5>
                    <el-input
                      placeholder="请输入内容"
                      v-model="aq"
                      clearable
                      
                    ></el-input>
                  </el-col>
                  <el-col :span="6">
                    <h5>B</h5>
                    <el-input
                      placeholder="请输入内容"
                      v-model="bq"
                      clearable
                    ></el-input>
                  </el-col>
                  <el-col :span="6">
                    <h5>C</h5>
                    <el-input
                      placeholder="请输入内容"
                      v-model="cq"
                      clearable
                    ></el-input>
                  </el-col>
                  <el-col :span="6">
                    <h5>D</h5>
                    <el-input
                      placeholder="请输入内容"
                      v-model="dq"
                      clearable
                    ></el-input>
                  </el-col>
                </el-row>
              </div>
              <div>
                <h4>本题答案：</h4>
                <el-radio-group v-model="ans">
                  <el-radio :label="1">A</el-radio>
                  <el-radio :label="2">B</el-radio>
                  <el-radio :label="3">C</el-radio>
                  <el-radio :label="4">D</el-radio>
                </el-radio-group>
              </div>
            </div>
            <div v-show="v2">
              <!-- 设置分数 -->
              <div class="box1">
                <el-row :gutter="20">
                <el-col :span="6" :offset="6">
                  <div class="form-group">
                <label for="qname">题号</label>
                <input type="textarea" id="qname" v-model="qname" required />
              </div>
              
              </el-col>
                <el-col :span="9">
              <div>
                本题分数
                <input type="text" v-model="qscore" required this.input="" />
              </div>
              </el-col>                
              </el-row>
              </div>
              <div class="box2">
              <div class="form-group">
                <label for="info">题目要求</label>
                <input type="textarea" id="info" v-model="info" required this.input="" />
              </div>
              
              </div>
              
              <div>
                <h4>本题答案：</h4>
                <el-radio-group v-model="ans">
                  <el-radio :label="1">正确</el-radio>
                  <el-radio :label="0">错误</el-radio>
                </el-radio-group>
              </div>
            </div>
            <div v-show="v4">
              <!-- 设置分数 -->
              <div class="box1">
              <el-row :gutter="20">
                <el-col :span="6" :offset="6">
              <div class="form-group">
                <label for="qname">题号</label>
                <input type="textarea" id="qname" v-model="qname" required />
              </div>
              
              </el-col>
                <el-col :span="9">
              <div>
                本题分数：
                <input type="text" v-model="qscore" required this.input="" />
              </div>
              </el-col>                
              </el-row>
</div>
<div class="box2">
              <div class="form-group">
                <br />
                <label for="info">题目要求</label>
                <br />
                <el-input type="textarea" id="info" v-model="info" required :rows="5" class="input"/>
              </div>
              </div>
              <div class="box2">
              <div class="form-group">
                <br />
                <label for="q_ans">参考答案</label>
                <br />
                <el-input type="textarea" id="q_ans" v-model="ans" required :rows="5" class="input"/>
              </div>
            </div>
            </div>
            <button type="submit" v-if="v1 || v2 || v4">保存题目</button>
            
          </form>
        </div>
        <button @click="showqs">预览</button>
        <!-- 预览 -->
        <div v-show="pshow" class="showbox">
          <el-row v-for="question in questions" :key="question.qid">
            <el-divider></el-divider>
            
            <div v-if="question.kind == '单选题'">
              第{{ question.qname }}题
              {{ question.kind }}
              <br />
              {{ question.info }}
              <br />
              <el-radio-group>
                <el-radio :label="1">A.{{ question.a }}</el-radio>
                <el-radio :label="2">B.{{ question.b }}</el-radio>
                <el-radio :label="3">C.{{ question.c }}</el-radio>
                <el-radio :label="4">D.{{ question.d }}</el-radio>
              </el-radio-group>
              <div>答案：{{ question.ans }}</div>
            </div>
            <div v-else-if="question.kind == '判断题'">
              第{{ question.qname }}题
              {{ question.kind }}
              <br />
              {{ question.info }}
              <br />
              <el-radio-group>
                <el-radio :label="1">正确</el-radio>
                <el-radio :label="0">错误</el-radio>
              </el-radio-group>
              <div>答案:{{ question.ans }}</div>
            </div>
            <div v-else>
              第{{ question.qname }}题
              {{ question.kind }}
              <br />
              {{ question.info }}
              <div>答案:{{ question.ans }}</div>
            </div>
            <button @click="deleteq(question.qid)">删除本题</button>
          </el-row>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Daohanglan from "./daohanglan.vue";
export default {
  name: "setquestions",
  props: ["wid", "cid"],
  components: {
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
  },
  data() {
    return {
      info: "",
      ans: "",
      kind: "",
      questions: [],
      qname: "",
      pshow: false,
      v1: false,
      v2: false,
      v4: false,
      aq: "",
      bq: "",
      cq: "",
      dq: "",
      qscore: "",
    };
  },
  methods: {
    back() {
      this.$router.push({ name: "singleCourse", params: { cid: this.cid } });
    },
    showset() {
      console.log(this.kind);
      this.pshow = false;
      if (this.kind == "1") {
        this.v1 = true;
        this.v2 = false;
        this.v3 = false;
        this.v4 = false;
      } else if (this.kind == "2") {
        this.v1 = false;

        this.v3 = false;
        this.v4 = false;
        this.v2 = true;
      } else {
        this.v1 = false;
        this.v2 = false;
        this.v3 = false;
        this.v4 = true;
      }
    },
    showqs() {
      axios
        .post(
          "http://127.0.0.1:8000/showQuestions/",
          { wid: this.wid },
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        )
        .then((response) => {
          console.log(response.data);
          if (response.data.status == "success") {
            this.pshow = true;
            this.questions = response.data.qs;
          }
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    },
    saveq() {
      console.log(this.kind);
      axios
        .post(
          "http://127.0.0.1:8000/saveq/",
          {
            wid: this.wid,
            qname: this.qname,
            info: this.info,
            ans: this.ans,
            kind: this.kind,
            a: this.aq,
            b: this.bq,
            c: this.cq,
            d: this.dq,
            score: this.qscore,
          },
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        )
        .then((response) => {
          console.log(response.data);
          if (response.data.status == "success") {
            this.qname = "";
            this.info = "";
            this.ans = "";
            this.kind = "";
            this.aq = "";
            this.bq = "";
            this.cq = "";
            this.dq = "";
            this.qscore = '';
            this.v1 = false;
            this.v2 = false;
            this.v4 = false;
          }
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    },
    deleteq(qid) {
      axios
        .post(
          "http://127.0.0.1:8000/deleteq/",
          { wid: this.wid, qid: qid },
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        )
        .then((response) => {
          console.log(response.data);
          if (response.data.status == "success") {
            this.questions = response.data.qs;
          }
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    },
  },
};
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

.box1{
  margin-top: 30px;
  margin-bottom: 20px;
}

.box2 input{
  width:300px;
  margin-bottom: 20px;
}



button{
  background-color: white;
  border:2px solid #F59A23;
  color: black;
  font-size: 15px;
  border-radius: 10px;
  margin-top: 10px;
  margin-bottom: 10px;
}

.showbox button{
position: absolute;
  bottom: 0px;
  right: 30px;
}

.input{
    width:60vw;
    margin-top: 10px;
    margin-bottom: 10px;
}
</style>
