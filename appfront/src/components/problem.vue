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
    </div>

    <!-- 提问的问题 -->
    <div class="qbox">
      <h2>{{ info }}</h2>
      <el-divider></el-divider>
      <div class="info">
        <p>提问者：{{ asker }} </p>
        <p>提问时间：{{ askTime }}</p>
        <button
          v-if="asker == username"
          @click="deleteProblem"
          class="deletebtn"
        >
          删除提问
        </button>
      </div>
      <div v-if="jh == 1" class="jh">
        <h3>精华</h3>
      </div>
    </div>
    <!-- 所有回复 -->
    <div class="ansbox">
      <el-row v-for="ans in answers" :key="ans.aid">
        <el-divider></el-divider>
        <p>{{ ans.info }}</p>
        <el-col :span="12">
          <p>回复者{{ ans.answerer }}</p>
          <p>回复时间{{ ans.answerTime }}</p>
        </el-col>
        <el-col :span="6" :offset="6">
            <button v-if="ans.answerer == username" @click="deleteAnswer(ans.aid)">删除</button>
        </el-col>
      </el-row>
    </div>
    <!-- 写回复 -->
    <div class="writebox">
      <el-input
        type="textarea"
        :rows="5"
        placeholder="请输入内容"
        v-model="answerText"
        class="inputtext"
      ></el-input>
      <button @click="huifu" class="send">回复</button>
    </div>

    
  </div>

  
</template>

<script>
import axios from "axios";
import Daohanglan from "./daohanglan.vue";

export default {
  name: "problem",
  props: ["cid", "pid"],
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
    currentrole() {
      return this.$store.state.username.currentrole;
    },
  },
  data() {
    return {
      info: "",
      asker: "",
      askTime: "",
      jh: "",
      resolved: "",
      answers: [],
      answerText: "",
    };
  },
  created() {
    axios
      .post(
        "http://127.0.0.1:8000/searchProblem/",
        { cid: this.cid, pid: this.pid },
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      )
      .then((response) => {
        console.log(response.data);
        if (response.data.status == "success") {
          this.info = response.data.info;
          this.asker = response.data.asker;
          this.askTime = response.data.t;
          this.jh = response.data.jh;
          this.resolved = response.data.resolved;
          this.answers = response.data.res;
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  },
  methods: {
    deleteProblem() {
      axios
        .post(
          "http://127.0.0.1:8000/deleteProblem/",
          { pid: this.pid },
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        )
        .then((response) => {
          console.log(response.data);
          if (response.data.status == "success") {
            alert("删除成功！");
            this.back();
          }
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    },
    back() {
      if (this.currentrole == "学生") {
        this.$router.push({ name: "studentCourse", params: { cid: this.cid } });
      } else {
        this.$router.push({ name: "singleCourse", params: { cid: this.cid } });
      }
    },
    deleteAnswer(aid) {
      axios
        .post(
          "http://127.0.0.1:8000/deleteAnswer/",
          { aid: aid },
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        )
        .then((response) => {
          console.log(response.data);
          if (response.data.status == "success") {
            this.$message({
          message: '删除成功!',
          type: 'success'
        });
            this.showAns();
          }
        })
        .catch((error) => {
          console.error("Error:", error);
        });
        
    },
    huifu() {
      axios
        .post(
          "http://127.0.0.1:8000/createAnswer/",
          {
            cid: this.cid,
            pid: this.pid,
            ans: this.answerText,
            answerer: this.username,
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
            this.answerText = "";
            this.$message({
          message: '回复成功！',
          type: 'success'
        });
            this.showAns();
          }
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    },
    showAns() {
      axios
        .post(
          "http://127.0.0.1:8000/showAns/",
          { pid: this.pid },
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        )
        .then((response) => {
          console.log(response.data);
          if (response.data.status == "success") {
            this.answers = response.data.res;
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

.qbox {
  background-color: #f5f5f5;
  width: 80vw;
  margin: 0 auto;
  position: relative; 
  display: flex; 
  flex-direction: column;
}

.jh {
  position: absolute; 
  top: 0;
  right: 20px;
}

p {
  text-align: left;
  margin-top: 0;
  margin-left: 10px;
  word-wrap: break-word;
}

.info {
  display: flex;
  position: relative;
}
.deletebtn {
  background-color: #f59a23b0;
  color: white;
  border: #f59a23;
  font-size: 15px;
  border-radius: 10px;
  height: 40px;
  width: 100px;
  position: absolute; 
  bottom: 10px; 
  right: 10px;
}

.ansbox {
  width: 80vw;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
}

.ansbox button{
  background-color: white;
  border:2px solid #F59A23;
  color: black;
  font-size: 15px;
  border-radius: 10px;
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



.inputtext {
  flex-grow: 1; 
  margin-right: 4px; 
}

.send {
  position: absolute; 
  right: 5px; /* 相对于最近的已定位（positioned）祖先元素定位 */
  bottom: 0;
  background-color: #f59a23b0; 
  color: white;
  border: none;
  padding: 0.5rem 1rem; 
  cursor: pointer;
}
</style>
