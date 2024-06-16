<template>
  <!-- 具体课程显示页面 -->
  <div>
    <!-- 导航栏 -->
    <div>
      <Daohanglan :isLoggedIn="isLoggedIn" :username="username"></Daohanglan>
    </div>

    <!-- 课程名称 -->
    <div class="cnamebox">
      <h1>{{ course.cname }}</h1>
    </div>

    <div class="contentbox">
      <el-row :gutter="24">
        <el-col :span="10">
          <div class="pic">
            <img :src="course.img" alt="" width="450" />
          </div>
        </el-col>

        <el-col :span="8">
          <div class="infobox">
            <div>
              <div>
                <h3>课程介绍:</h3>
                <p>{{ course.introduction }}</p>
              </div>
              <div class="info">
                <h3>授课教师:</h3>
                <p>{{ course.teacher }}</p>
              </div>
              <div class="info">
                <h3>累计选课:</h3>
                <p>{{ course.stuNum }}人</p>
              </div>
              <div class="info">
                <h3>学时:</h3>
                <p>{{ course.xueshi }}</p>
              </div>

              <h3 class="status">{{ course.status }}</h3>
            </div>
          </div>
        </el-col>

        <el-col :span="6">
          <!-- 选课 -->
          <div>
            <div v-if="this.currentrole == '学生'">
              <div v-if="already == 0">
                <button @click="pick" class="pickbtn">选课</button>
              </div>
              <div v-else><h2>已选课</h2></div>
            </div>
          </div>
        </el-col>
      </el-row>

      <div class="lastline">
        <p>Copyright © 2024 GoodGoodStudy. All rights reserved.</p>
      </div>
    </div>


  </div>
</template>

<script>
import Daohanglan from "./daohanglan.vue";
import axios from "axios";
export default {
  name: "myCourse",
  props: ["cid"],
  components: {
    Daohanglan,
  },
  data() {
    return {
      course: "",
      already: 0,
    };
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
  created() {
    axios
      .post(
        "http://127.0.0.1:8000/showCourse/",
        { cid: this.cid, username: this.username },
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      )
      .then((response) => {
        console.log(response.data);
        if (response.data.status == "success") {
          this.course = response.data.course;
          this.already = this.course.already;
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  },
  methods: {
    pick() {
      if (this.isLoggedIn) {
        axios
          .post(
            "http://127.0.0.1:8000/pickCourse/",
            { cid: this.cid, username: this.username },
            {
              headers: {
                "Content-Type": "multipart/form-data",
              },
            }
          )
          .then((response) => {
            console.log(response.data);
            if (response.data.status == "success") {
              this.course = response.data.course;
              this.already = 1;
            }
          })
          .catch((error) => {
            console.error("Error:", error);
          });
      } else {
        this.$router.push({ name: "login" });
      }
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.cnamebox {
  height: 100px;
  background-image: linear-gradient(#f59a23, #f5f5f5);
  display: flex;
  text-align: center;
  justify-content: center;
}

.contentbox {
  background-color: #f5f5f5;
  /* position: fixed; */
  overflow-y: scroll;
  max-width: 100vw;
  margin: 0 auto;
  overflow: hidden;
  height:800px
}

.pic {
  margin-top: 20px;
}

.infobox {
  display: flex;
  text-align: left;
}

.info {
  display: flex;
  align-items: baseline;
}

.info p {
  text-align: left;
  margin-top: 0;
  word-wrap: break-word;
  max-width: 500px;
  margin-left: 10px;
}

.info h3 {
  text-align: left;
  margin-top: 0;
}

.status {
  margin: 0;
}

.pickbtn{
  background-color: #f59a23b0;
  color: white;
  border:white;
  font-size: 15px;
  border-radius: 10px;
  margin: 20px;
  height:40px;
  width:100px;
  margin-top:100px;
}

.lastline p {
  position: relative;
  bottom: 0;
  font-size: 10px;
}
</style>
