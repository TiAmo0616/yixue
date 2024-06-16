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
    <!-- 统计情况 -->
    <div>
      <el-row :gutter="20">
        <el-col :span="6" :offset="6">
          <el-statistic title="已交">
            <template slot="formatter">
              {{ this.al }}
            </template>
          </el-statistic>
        </el-col>
        <el-col :span="6">
          <el-statistic title="未交">
            <template slot="formatter">
              {{ this.noal }}
            </template>
          </el-statistic>
        </el-col>
      </el-row>
    </div>
    <!-- 展示已经交的作业 -->
    <div class="box">
      <el-row v-for="work in works" :key="work.name" class="each">
        <el-divider></el-divider>
        姓名：
        {{ work.username }}
        <br />
        提交时间{{ work.t }}
        <div v-if="work.status == '待批改'">
          <button @click="see(work.username, work.status)">去批改</button>
        </div>
        <div v-else>
          已批改
          <button @click="see(work.username, work.status)">查看</button>
        </div>
      </el-row>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Daohanglan from "./daohanglan.vue";
export default {
  name: "totalAnswer",
  props: ["cid", "wid"],
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
      works: [],
      al: "",
      noal: "",
    };
  },
  created() {
    axios
      .post(
        "http://127.0.0.1:8000/showtotalans/",
        { wid: this.wid, cid: this.cid },
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      )
      .then((response) => {
        console.log(response.data);
        if (response.data.status == "success") {
          this.works = response.data.res;
          this.al = response.data.al;
          this.noal = response.data.noal;
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  },
  methods: {
    back() {
      this.$router.push({ name: "singleCourse", params: { cid: this.cid } });
    },
    see(name, status) {
      this.$router.push({
        name: "judgeWork",
        params: { wid: this.wid, cid: this.cid, name: name, status: status },
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

.each{
  margin-top: 10px;
}

.box{
  width: 60vw;
  margin: 0 auto;
}

.box button{
  background-color: #f59a23b0;
  color: white;
  border: #f59a23;
  font-size: 15px;
  border-radius: 10px;
  margin-top: 10px;
  height: 30px;
  width: 60px;
}
</style>
