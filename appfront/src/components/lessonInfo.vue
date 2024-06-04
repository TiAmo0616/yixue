<template>
  <div>
    <Daohanglan :isLoggedIn="isLoggedIn" :username="username"></Daohanglan>
    <div class="pagebody">
      <el-row :gutter="20">
        <!-- 可修改信息 -->
        <el-col :span="16">
          <div class="box">
            <!-- 返回 -->
            <div class="backbox">
              <button @click="back" class="backbtn">
                <img
                  src="../assets/image/lessoninfo/left.svg"
                  alt="logo"
                  class="back-icon"
                />
                <p class="back-text">| 返回</p>
              </button>
            </div>

            <!-- 修改图标 -->
            <div class="title">
              <h1>课程信息</h1>
              <el-button type="text" @click="dialogFormVisible = true"
                ><img src="../assets/image/userinfo/pencil.svg" width="20px"
              /></el-button>
            </div>

            <el-row :gutter="24">
              <el-col :span="6">
                <div class="pic">
                  <img :src="image" alt="" width="200" />
                  <el-button @click="uploadVisible = true" class="btn"
                    >更换图片</el-button
                  >
                </div>
              </el-col>

              <el-col :span="18">
                <div class="info">
                  <div>
                    <h3>课程名：</h3>
                    <p>{{ this.cname }}</p>
                  </div>

                  <div>
                    <h3>学时：</h3>
                    <p>{{ this.xueshi }}</p>
                  </div>

                  <div>
                    <h3>任课教师：</h3>
                    <p>{{ this.teacher }}</p>
                  </div>

                  <div>
                    <h3>课程简介：</h3>
                    <p>{{ this.intro }}</p>
                  </div>
                </div>
              </el-col>
            </el-row>
            <div></div>
          </div>
        </el-col>

        <!-- 右侧两块 -->
        <el-col :span="8">
          <div class="rightbox">
            <div class="info2">
              <div>
                <h3>课程码：</h3>
                <p>{{ this.cid }}</p>
              </div>
              <div>
                <h3>学生人数：</h3>
                <p>{{ course.stuNum }}</p>
              </div>
              <div>
                <h3>课程状态：</h3>
                <p>{{ course.status }}</p>
              </div>
            </div>

            <div class="deleteclass">
              <p>删除课程</p>
              <button @click="deleteFormVisible = true" class="btn">
                删除课程
              </button>
              <button @click="closeCourse">结束课程</button>
            </div>
          </div>
        </el-col>
      </el-row>

      <div class="lastline">
        <p>Copyright © 2024 GoodGoodStudy. All rights reserved.</p>
      </div>
    </div>
    <!-- 修改信息 -->
    <el-dialog title="修改课程信息" :visible.sync="dialogFormVisible">
      <el-form :model="form">
        <el-form-item label="课程名" :label-width="formLabelWidth">
          <el-input v-model="newcname" autocomplete="off" clearable></el-input>
        </el-form-item>
        <el-form-item label="学时" :label-width="formLabelWidth">
          <el-input v-model="newxueshi" autocomplete="off" clearable></el-input>
        </el-form-item>
        <el-form-item label="任课教师" :label-width="formLabelWidth">
          <el-input v-model="newteacher" autocomplete="off" clearable></el-input>
        </el-form-item>
        <el-form-item label="课程简介" :label-width="formLabelWidth">
          <el-input
            v-model="newintro"
            autocomplete="off"
            clearable
            type="textarea"
            :rows="2"
            placeholder="请输入内容"
          ></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="quxiao">取 消</el-button>
        <el-button type="primary" @click="submitInfo">确 定</el-button>
      </div>
    </el-dialog>

    <!-- 修改头像 -->
    <el-dialog title="修改课程图片" :visible.sync="uploadVisible" width="30%">
      <div class="modal-content">
        <el-upload
          v-model="fileList"
          ref="uploadref"
          action="#"
          accept="image/png,image/gif,image/jpg,image/jpeg"
          :auto-upload="false"
          list-type="picture-card"
          :on-preview="handlePictureCardPreview"
          :on-change="handleChange"
          :on-remove="handleRemove"
        >
          <i class="el-icon-plus"></i>
        </el-upload>
      </div>

      <div slot="footer" class="dialog-footer">
        <el-button @click="uploadVisible = false">取 消</el-button>
        <el-button type="primary" @click="handleFileUpload">确 定</el-button>
      </div>
    </el-dialog>

    <!-- 确认是否删除课程 -->
    <el-dialog title="删除课程" :visible.sync="deleteFormVisible" width="30%">
      <div slot="footer" class="dialog-footer">
        <el-button type="primary" @click="deleteFormVisible = false"
          >取 消</el-button
        >
        <el-button @click="deleteCourse">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import axios from "axios";
import Daohanglan from "./daohanglan.vue";
export default {
  name: "lessonInfo",
  props: ["cid"],
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
      course: "",
      cname: "",
      intro: "",
      xueshi: "",
      teacher: "",
      dialogVisible: false,
      uploadVisible: false,
      formLabelWidth: "120px",
      dialogFormVisible: false,
      uploadVisible: false,
      deleteFormVisible: false,
      fileList: [],
      imageUrl: "",
      image: null,
      newcname:'',
      newintro:'',
      newxueshi:'',
      newteacher:'',
    };
  },
  created() {
    this.showCourse()
  },
  methods: {
    showCourse(){
      axios
      .post(
        "http://127.0.0.1:8000/showCourse/",
        { cid: this.cid },
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
          this.cname = this.course.cname;
          this.intro = this.course.introduction;
          this.xueshi = this.course.xueshi;
          this.teacher = this.course.teacher;
          this.image = this.course.img;
          this.newcname = this.course.cname;
          this.newintro = this.course.introduction;
          this.newxueshi = this.course.xueshi;
          this.newteacher = this.course.teacher;
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      });
    },
    closeCourse(){
      axios.post("http://127.0.0.1:8000/closeCourse/",{'cid':this.cid,'username':this.username},{
      headers: {
        'Content-Type': 'multipart/form-data'
      }
  })
      .then(response =>{
        console.log(response.data)
        if(response.data.status == 'success'){
          const fname = response.data.cname;
          alert("您已结束 "+fname+" 课程")
          this.showCourse()
        }
         
      })
      .catch(error => {
        
        console.error('Error:', error);
      });
      
    },
    quxiao(){
      this.dialogFormVisible = false;
      this.newcname = this.cname
      this.newintro = this.intro
      this.newteacher = this.teacher
      this.newxueshi = this.xueshi
    },
    back() {
      this.$router.push({ name: "singleCourse", params: { cid: this.cid } });
    },
    deleteCourse() {
      axios
        .post(
          "http://127.0.0.1:8000/deleteCourse/",
          { cid: this.cid },
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
            this.$router.push({ name: "teacherPage" });
          }
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    },
    submitInfo() {
      axios
        .post(
          "http://127.0.0.1:8000/editCourse/",
          {
            cid: this.cid,
            cname: this.newcname,
            intro: this.newintro,
            xueshi: this.newxueshi,
            teacher: this.newteacher,
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
            this.dialogFormVisible = false;
            this.cname = this.newcname
            this.intro = this.newintro
            this.teacher = this.newteacher
            this.xueshi = this.newxueshi
          }
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    },
    handleRemove(file, fileList) {
      this.fileList.pop();
      console.log(file, fileList);
    },
    handlePictureCardPreview(file) {
      this.dialogImageUrl = file.url;
      this.dialogVisible = true;
    },

    uploadImage() {
      this.upload = true;
    },
    handleChange(file, fileList) {
      this.fileParam = new FormData(); //创建form对象
      this.fileParam.append("file", file["raw"]);
      this.fileParam.append("fileName", file["name"]);
      this.fileParam.append("cid", this.cid);
    },
    handleFileUpload() {
      const formData = new FormData();
      formData.append("image", this.file);
      formData.append("cid", this.cid);
      console.log(this.fileParam);
      axios
        .post("http://127.0.0.1:8000/changeImage/", this.fileParam)
        .then((response) => {
          this.fileList = [];
          this.upload = false;
          // this.fileList.push(response.data)
          this.image = response.data.url;
          // this.dialogImageUrl = response.data.url
          console.log(response.data);
        })
        .catch((error) => {
          console.error("Error:", error);
        });
      this.uploadVisible = false;
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.pagebody {
  width: 100%;
  background-color: #f5f5f5;
  /* position: fixed; */
  overflow-y: scroll;
  max-width: 100vw;
  margin: 0 auto;
  overflow: hidden;
}

.box {
  background-color: white;
  border: 1px solid #797979;
  margin: 50px;
}

.backbox {
  width: 100%;
  display: flex;
}
.backbtn {
  display: inline-block;
  vertical-align: middle;
  border: 0;
  background-color: white;
}

.back-icon {
  display: inline-block;
  vertical-align: middle; /* 垂直居中对齐 */
  width: 30px; /* 设置图片宽度 */
  height: auto; /* 保持图片宽高比 */
}

.back-text {
  display: inline-block;
  vertical-align: middle; /* 垂直居中对齐 */
  font-size: 20px;
}

.title {
  display: flex;
}

.title h1 {
  font-size: 20px;
  font-weight: bold;
  margin: 30px;
  margin-top: 10px;
  text-align: left;
}

.title button {
  border: 0;
  background-color: white;
  padding: 0;
  margin-top: 15px;
  height: 20px;
}

.pic {
  margin-left: 30px;
}
.pic img {
  object-fit: cover;
}

.info p,
.info2 p {
  text-align: left;
  margin-top: 0;
  word-wrap:break-word;
  max-width:300px;

}

.info h3,
.info2 h3 {
  text-align: left;
  margin-left: 50px;
  margin-top: 0;
}

.info div {
  display: flex;
  align-items: baseline;
  margin-bottom: 20px;
  margin-left: 30px;
}

.rightbox {
  margin-top: 50px;
}

.info2,
.deleteclass {
  background-color: white;
  border: 1px solid #797979;
  margin: 30px 50px 30px 50px;
}

.info2 div {
  display: flex;
  align-items: baseline;
  margin: 20px;
}

.btn {
  background-color: white;
  border: 2px solid #f59a23;
  color: black;

  font-size: 15px;
  border-radius: 10px;
  margin-bottom: 20px;
}
.lastline p {
  position: relative;
  bottom: 0;
  font-size: 10px;
}
</style>
