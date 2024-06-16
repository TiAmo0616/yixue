<template>
  <div>
    <!-- 导航栏 -->
    <div>
      <Daohanglan :isLoggedIn="isLoggedIn" :username="username"></Daohanglan>
    </div>
    <!-- 顶栏 -->
    <div class="headbox">
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

      <el-row>
        <el-col :span="8">
          <div class="imgbox">
            <img :src="course.img" alt="" width="200" />
          </div>
        </el-col>
        <el-col :span="8">
          <div class="cnamebox">
            <h1>{{ course.cname }}</h1>
          </div>
        </el-col>
        <el-col :span="8">
          <div class="rightbtn">
            <button @click="setClass">课程设置</button>
            <button @click="classBegin">开始直播</button>
          </div>
        </el-col>
      </el-row>
    </div>

    <!-- 服务 -->
    <el-row>
      <el-col :span="16">
        <div class="grid-content bg-purple">
          <el-tabs v-model="activeName" @tab-click="handleClick">
            <el-tab-pane label="学习资源" name="first">
              <!-- 学习资源（录播课程） -->
              <div v-show="firstshow">
                <div class="block">
                  <el-tree
                    :data="data"
                    node-key="id"
                    default-expand-all
                    :expand-on-click-node="false"
                  >
                    <span class="custom-tree-node" slot-scope="{ node, data }">
                      <!-- <span>{{ node.label }}</span> -->
                      <input
                        v-if="isLabelEditing && editId == node.id"
                        type="text"
                        v-model="data.label"
                      />
                      <span v-else>{{ node.label }}</span>
                      <!-- <span v-if="!isEditing">{{ node.label }}</span>
                <input v-else type="text" v-model="data.label" /> -->
                      <el-button
                        v-if="isLabelEditing && editId == node.id"
                        type="text"
                        size="mini"
                        @click="editLabel(node, data)"
                        >确认</el-button
                      >
                      <el-button
                        v-else
                        type="text"
                        size="mini"
                        @click="startEdit(node)"
                        >编辑</el-button
                      >
                      <span>
                        <el-button
                          type="text"
                          size="mini"
                          @click="append(data)"
                        >
                          增加子级目录
                        </el-button>
                        <el-button
                          type="text"
                          size="mini"
                          @click="remove(node, data)"
                        >
                          删除目录
                        </el-button>
                        <el-button
                          type="text"
                          size="mini"
                          @click="upload(data)"
                        >
                          上传文件
                        </el-button>
                      </span>
                    </span>
                  </el-tree>
                </div>

                
              </div>
            </el-tab-pane>

            <!-- 作业 -->
            <el-tab-pane label="作业" name="second">
              <div v-show="sencondshow">
      <div class="workbtn">
        <button @click="showWork('ing')">未截止</button>
        <button @click="showWork('ed')">已截止</button>
        <button @click="showWork('all')">全部</button>
        <button @click="workFormVisible = true" class="newworkbtn">发布</button>
      </div>

      <div>
        <el-row v-for="work in works" :key="work.wid">
          <el-divider></el-divider>
          <el-row :gutter="20">
            <el-col :span="3" :offset="6">
              <h4>{{ work.wname }}</h4>
            </el-col>
            <el-col :span="10" :offset="5">
          
          
          <div class="workbox">  
            <button @click="see(work.wid)">查看</button>
            <button @click="setquestions(work.wid)">设置题目</button>
            <button @click="deleteWork(work.wid)">删除</button>                      
          </div>
          </el-col>
          </el-row>
          <p>开始时间：{{ work.begin }} 截止时间：{{ work.end }}</p>
          
        </el-row>
      </div>
      
    </div>
            </el-tab-pane>

            <!-- 问答 -->
            <el-tab-pane label="问答" name="third">
              <div class="askbtn">
                <button @click="showProblem('my')">我的</button>
                <button @click="showProblem('jh')">精华</button>
                <button @click="showProblem('all')">全部</button>
                <button @click="askFormVisible = true" class="sendaskbtn">发布</button>
              </div>

              <div>
                <el-row v-for="problem in problems" :key="problem.pid">
                  <el-divider></el-divider>
                  <div class="question">
                    <h4>{{ problem.pinfo }}</h4>
                    <div class="qinfobox">
                      <p>用户:{{ problem.askername }}</p>
                      <p>发布时间:{{ problem.t }}</p>
                      <p></p>
                      <div v-if="problem.jh == 1" class="jh">精华</div>
                      <button @click="huifu(problem.pid)">查看详情</button>
                      <button
                        v-if="problem.jh == 0"
                        @click="setjh(problem.pid)"
                      >
                        设为精华
                      </button>
                    </div>
                  </div>
                </el-row>
              </div>
              
            </el-tab-pane>

            <!-- 评论 -->
            <el-tab-pane label="评论" name="fourth">
                <div class="workbtn">
                    <button @click="commentFormVisible = true" class="newworkbtn">发布评论</button>
                </div>
                <div>
                <el-row v-for="comment in comments" :key="comment.comid">
                    <el-divider></el-divider>
                    <div class="question">
                    <h4>{{ comment.info }}</h4>
                    <div class="qinfobox">
                        <p>用户:{{ comment.username }}  时间:{{ comment.t }}</p>
                        <button v-if="comment.username == username" @click="deleteComment(comment.comid)" class="deletebtn">
                        删除
                        </button>
                        <div class="like">
                            <button @click="dianzan(comment.comid)" v-if="comment.showZan == 'off'"><img src="../assets/image/like1.png"></button>
                            <button v-else @click="dianzan(comment.comid)"><img src="../assets/image/like2.png"></button>
                            <p>{{ comment.zan }}</p>
                        </div>
                    </div>
                    </div>
                </el-row>
                </div>
                
            </el-tab-pane>

            <!-- 直播回放 -->
            <el-tab-pane label="直播回放" name="fifth">
              <div v-show="fifthshow">
                <el-row v-for="date in mp4Files" :key="date">
                  <el-divider></el-divider>
                  <h5>{{ date.period }}</h5>
                  <el-row v-for="mp4 in date.records" :key="mp4.path">
                    <div class="videobox">
                    <h4>{{ mp4.rname }}</h4>
                    <button @click="dowloadFile(mp4.path, mp4.rname)">
                      下载
                    </button>
                    <button @click="watchFile(mp4.path)">观看</button>
                    <button @click="openRenameDialog(mp4.rname)">重命名</button>
                    <button @click="deletelubo(mp4.rname)">删除</button>
                    
                
                    </div>
                  </el-row>
                </el-row>
                
              </div>
            </el-tab-pane>
          </el-tabs>
        </div>
      </el-col>

      <el-col :span="8">
        <div class="info">
          <div>
            <h3>课程码：</h3>
            <p>{{ this.cid }}</p>
          </div>
          <div>
            <h3>学生人数：</h3>
            <p>{{ course.stuNum }}</p>
          </div>
          <div>
            <h3>学时：</h3>
            <p>{{ course.xueshi }}</p>
          </div>
          <div>
            <h3>课程状态：</h3>
            <p>{{ course.status }}</p>
          </div>
        </div>
      </el-col>
    </el-row>

    
    <!-- 发布问答弹窗 -->
    <el-dialog title="发布问答" :visible.sync="askFormVisible">
      <el-form :model="form">
        <el-form-item label="问题" >
          <el-input v-model="new_pinfo" autocomplete="off" clearable type="textarea" :rows="2" placeholder="请输入问题" this.input=''></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="askFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="submitProblems">确 定</el-button>
      </div>
    </el-dialog>

    <!-- 发布作业弹窗 -->
    <el-dialog title="发布作业" :visible.sync="workFormVisible">
      <el-form :model="form">
        <el-form-item label="作业标题：" :label-width="formLabelWidth" >
          <el-input v-model="new_wname" autocomplete="off" this.input=''></el-input>
        </el-form-item>
      </el-form>
      <div class="form-group">
              <label for="info">开始时间</label>
              <el-date-picker
                v-model="newbegin"
                type="datetime"
                placeholder="选择日期时间"
              >
              </el-date-picker>
            </div>
      <div class="form-group">
              <label for="info">截止时间</label>
              <el-date-picker
                v-model="newend"
                type="datetime"
                placeholder="选择日期时间"
              >
              </el-date-picker>
            </div>
      <div slot="footer" class="dialog-footer">
        <el-button @click="workFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="submitfabu">确 定</el-button>
      </div>
    </el-dialog>

    <!-- 重命名视频 -->
    <el-dialog title="重命名" :visible.sync="renameFormVisible">
      <el-form :model="form">
        <el-form-item label="视频名：" :label-width="formLabelWidth" >
          <el-input v-model="newrname" autocomplete="off" clearable this.input=''></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="renameFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="submitRename()">确 定</el-button>
      </div>
    </el-dialog>

    <el-dialog title="上传文件" :visible.sync="uploadFormVisible">
      <el-form :model="form">
        <input
                    type="file"
                    ref="videoInput"
                    @change="handleFileChange"
                  />
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="uploadFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="uploadVideo">确 定</el-button>
      </div>
    </el-dialog>
    <!-- 发布评论 -->
    <el-dialog title="发布评论" :visible.sync="commentFormVisible">
      <el-form :model="form">
        <el-form-item label="请写下评论：" >
          <el-input v-model="newcomment" autocomplete="off" clearable this.input=''></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="commentFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="submitComment()">确 定</el-button>
      </div>
    </el-dialog>
     
     <!-- 发布评论 -->
     <el-dialog title="发布评论" :visible.sync="commentFormVisible">
      <el-form :model="form">
        <el-form-item label="请写下评论：" :label-width="formLabelWidth" >
          <el-input v-model="newcomment" autocomplete="off" clearable this.input=''></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="commentFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="submitComment()">确 定</el-button>
      </div>
    </el-dialog>
              
    <!-- 正在上传 -->
    <el-dialog title="正在上传" :visible.sync="uploadingFormVisible">
      正在上传
      <i class="el-icon-loading"></i>
    </el-dialog>
                
  </div>
</template>

<script>
import axios from "axios";
import Daohanglan from "./daohanglan.vue";

export default {
  name: "singleCourse",
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
    //const data=[{id:0,label:'学习资源',children:[],path:''}]
    return {
      course: "",
      activeName: "first",
      firstshow: true,
      sencondshow: false,
      thirdshow: false,
      fourthshow: false,
      fifthshow: false,
      works: [],
      fabushow: false,
      new_wname: "",
      newbegin: "",
      newend: "",
      problems: [],
      tiwenShow: false,
      new_pinfo: "",

      mp4Files: [],
      paths: [],
      rootpath: "",
      isRenaming: false,
      newrname: "",
      oldrname: "",

      //data: JSON.parse(JSON.stringify(data)),
      data: [],
      isEditing: false,
      isUpload: false,
      currentData: null,
      beginId: 0,
      editId: "",
      isLabelEditing: false,
      askFormVisible: false,
      workFormVisible: false,
      renameFormVisible : false,
      uploadFormVisible :false,

      comments:[],
      newcomment:'',
      commentFormVisible:false,
      uploadingFormVisible:false,
  };
  },
  created() {
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
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      });
    this.getmp4List();
    this.searchLM();
  },

  methods: {
    dianzan(comid){
        axios.post( "http://127.0.0.1:8000/dianzan/",   { comid:comid,username:this.username},
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      )
      .then((response) => {
        console.log(response.data);
        if (response.data.status == "success") {
           this.showComments()
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      });
    },
    deleteComment(comid){
        axios.post( "http://127.0.0.1:8000/deleteComment/",   { cid: this.cid ,comid:comid},
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      )
      .then((response) => {
        console.log(response.data);
        if (response.data.status == "success") {
            alert("删除成功！")
           this.showComments()
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      });
    },
    showComments(){
        axios.post( "http://127.0.0.1:8000/showComments/",   { cid: this.cid,username:this.username},
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      )
      .then((response) => {
        console.log(response.data);
        if (response.data.status == "success") {
            this.comments = response.data.res;
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      });
    },
    submitComment(){
        axios.post( "http://127.0.0.1:8000/createComment/",   { cid: this.cid ,username:this.username,info:this.newcomment},
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      )
      .then((response) => {
        console.log(response.data);
        if (response.data.status == "success") {
            this.commentFormVisible = false
            this.newcomment = ''
           this.showComments()
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      });
    },
    deletelubo(rname){
        axios.post( "http://127.0.0.1:8000/deletelubo/",   { cid: this.cid ,rname:rname},
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      )
      .then((response) => {
        console.log(response.data);
        if (response.data.status == "success") {
            alert("删除成功！")
            this.getmp4List();
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      });
    },
    back() {
      this.$router.push({ name: "teacherPage" });
    },
    setjh(pid) {
      axios
        .post(
          "http://127.0.0.1:8000/setjh/",
          { pid: pid },
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        )
        .then((response) => {
          console.log(response.data);
          if (response.data.status == "success") {
            console.log(response.data);
            this.$message({
          message: '设置成功',
          type: 'success'
        });
            
            this.showProblem("all");
          }
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    },
    huifu(pid) {
      this.$router.push({
        name: "problem",
        params: { cid: this.cid, pid: pid },
      });
    },
    setClass() {
      this.$router.push({ name: "lessonInfo", params: { cid: this.cid } });
    },
    searchLM() {
      axios
        .post(
          "http://127.0.0.1:8000/searchLM/",
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
            console.log(response.data);
            this.data = response.data.res;
            this.beginId = response.data.maxId;
            console.log(this.data);
          }
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    },
    upload(data) {
      this.uploadFormVisible=true;
      this.currentData = data;
    },
    startEdit(node) {
      this.isEditing = true;
      this.isLabelEditing = true;
      this.editId = node.id;
    },
    editLabel(node, data) {
      this.isEditing = false;
      this.isLabelEditing = false;
      console.log(node);
      axios
        .post(
          "http://127.0.0.1:8000/editDirectory/",
          { cid: this.cid, id: node.data.did, label: node.label },
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        )
        .then((response) => {
          console.log(response.data);
          if (response.data.status == "success") {
            console.log(response.data);
          }
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    },
    //只是创建目录
    append(data) {
      let id = this.beginId++;
      axios
        .post(
          "http://127.0.0.1:8000/appendLM/",
          {
            cid: this.cid,
            id: id,
            label: "目录" + id,
            pdid: data.did,
            path: "",
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
            console.log(response.data);
            const newChild = {
              id: id,
              label: "目录" + id,
              children: [],
              path: "",
            };
            if (!data.children) {
              this.$set(data, "children", []);
            }
            data.children.push(newChild);
          }
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    },
    //上传视频作为子目录
    appendVideo(data, rname, path) {
      let id = this.beginId++;
      console.log(data);
      axios
        .post(
          "http://127.0.0.1:8000/appendLM/",
          { cid: this.cid, id: id, label: rname, pdid: data.did, path: path },
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        )
        .then((response) => {
          console.log(response.data);
          if (response.data.status == "success") {
            console.log(response.data);
            const newChild = { id: id, label: rname, children: [], path: path };
            if (!data.children) {
              this.$set(data, "children", []);
            }
            data.children.push(newChild);
          }
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    },
    handleFileChange(event) {
      this.videoFile = event.target.files[0];
    },
    remove(node, data) {
      axios
        .post(
          "http://127.0.0.1:8000/deleteLM/",
          { cid: this.cid, id: data.did },
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        )
        .then((response) => {
          console.log(response.data);
          if (response.data.status == "success") {
            console.log(response.data);
            const parent = node.parent;
            const children = parent.data.children || parent.data;
            const index = children.findIndex((d) => d.did === data.did);
            children.splice(index, 1);
            this.$message({
          message: '已删除',
          type: 'success'
        });
          }
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    },
    renderContent(h, { node, data, store }) {
      return (
        <span class="custom-tree-node">
          <span>{node.label}</span>
          <span>
            <el-button
              size="mini"
              type="text"
              on-click={() => this.append(data)}
            >
              Append
            </el-button>
            <el-button
              size="mini"
              type="text"
              on-click={() => this.remove(node, data)}
            >
              Delete
            </el-button>
          </span>
        </span>
      );
    },
    uploadVideo() {
      if (!this.videoFile) {
        alert("请先选择视频文件。");
        return;
      }
      this.uploadFormVisible = false
      this.uploadingFormVisible = true
      const formData = new FormData();
      formData.append("video", this.videoFile);

      axios
        .post("http://127.0.0.1:8000/uploadVideo/", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then((response) => {
          console.log(response.data);
          if (response.data.status == "success") {
            this.uploadingFormVisible = false
            this.$message({
              message: '上传成功！',
              type: 'success'
            });
            this.isUpload = false;
            console.log(this.currentData);
            this.appendVideo(
              this.currentData,
              response.data.rname,
              response.data.path
            );
          }
        })
        .catch((error) => {
          console.error("Error:", error);
          this.$message.error('上传失败！');
        });
    },
    openRenameDialog(oldrname) {
      
      this.renameFormVisible = true;
      this.oldrname = oldrname;
    },
    submitRename() {
      axios
        .post(
          "http://127.0.0.1:8000/reName/",
          { cid: this.cid, rname: this.oldrname, newrname: this.newrname },
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        )
        .then((response) => {
          console.log(response.data);
          if (response.data.status == "success") {
            this.getmp4List();
          }
        })
        .catch((error) => {
          console.error("Error:", error);
        });
        this.renameFormVisible = false;
    },
    watchFile(path) {
      this.$router.push({
        name: "dianbo",
        params: { path: path, cid: this.cid },
      });
    },
    getmp4List() {
      axios
        .post(
          "http://127.0.0.1:8000/getRecordsList/",
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
            this.mp4Files = response.data.res;
          }
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    },
    dowloadFile(filepath, rname) {
      const downloadUrl =
        "https://zlm.com/index/api/downloadFile?file_path=" + filepath;

      fetch(downloadUrl)
        .then((response) => response.blob())
        .then((blob) => {
          const url = window.URL.createObjectURL(blob);
          const link = document.createElement("a");
          link.href = url;
          link.download = rname; // 指定下载文件的名称
          document.body.appendChild(link);
          link.click();
          document.body.removeChild(link);
          window.URL.revokeObjectURL(url);
        })
        .catch((error) => console.error("下载失败:", error));
    },
    workback() {
      this.fabushow = false;
      this.new_wname = "";
      this.newbegin = "";
      this.newend = "";
    },
    handleClick(tab) {
      if (tab.name == "first") {
        this.searchLM();
        this.firstshow = true;
        this.sencondshow = false;
        this.thirdshow = false;
        this.fourthshow = false;
      } else if (tab.name == "second") {
        axios
          .post(
            "http://127.0.0.1:8000/showWorks/",
            { cid: this.cid, status: "all" },
            {
              headers: {
                "Content-Type": "multipart/form-data",
              },
            }
          )
          .then((response) => {
            console.log(response.data);
            if (response.data.status == "success") {
              this.works = response.data.works;
            }
          })
          .catch((error) => {
            console.error("Error:", error);
          });
        this.firstshow = false;
        this.sencondshow = true;
        this.thirdshow = false;
        this.fourthshow = false;
      } else if (tab.name == "third") {
        this.firstshow = false;
        this.sencondshow = false;
        this.thirdshow = true;
        this.fourthshow = false;
        this.showProblem("all");
      } else if (tab.name == "fourth") {
        this.firstshow = false;
        this.sencondshow = false;
        this.thirdshow = false;
        this.fourthshow = true;
        this.showComments()
      } else {
        this.firstshow = false;
        this.sencondshow = false;
        this.thirdshow = false;
        this.fourthshow = false;
        this.fifthshow = true;
        this.getmp4List()
      }
    },
    showWork(status) {
      axios
        .post(
          "http://127.0.0.1:8000/showWorks/",
          { cid: this.cid, status: status },
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        )
        .then((response) => {
          console.log(response.data);
          if (response.data.status == "success") {
            this.works = response.data.works;
          }
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    },
    gotofabu() {
      this.fabushow = true;
    },
    submitfabu() {
      if (this.new_wname === ""){
        this.$message.error('作业标题不能为空');
        return;
      }
      if (this.newbegin === ""){
        this.$message.error('请设置开始时间');
        return;
      }
      if (this.newend === ""){
        this.$message.error('请设置截至时间');
        return;
      }
      var moment = require("moment");
      let g = moment.utc(this.newbegin).toDate();
      let t = moment(g).format("YYYY-MM-DD HH:mm:ss");
      let eg = moment.utc(this.newend).toDate();
      let et = moment(eg).format("YYYY-MM-DD HH:mm:ss");
      
      axios
        .post(
          "http://127.0.0.1:8000/createWork/",
          { cid: this.cid, wname: this.new_wname, begin: t, end: et },
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        )
        .then((response) => {
          console.log(response.data);
          if (response.data.status == "success") {
            this.works = response.data.works;
            this.fabushow = false;
            this.new_wname = "";
            this.newbegin = "";
            this.newend = "";
          }
        })
        .catch((error) => {
          console.error("Error:", error);
        });
        this.workFormVisible=false;
    },
    deleteWork(wid) {
      axios
        .post(
          "http://127.0.0.1:8000/deleteWork/",
          { wid: wid },
          {
            headers: { "Content-Type": "multipart/form-data" },
          }
        )
        .then((response) => {
          console.log(response.data);
          if (response.data.status == "success") {
            this.works = response.data.works;
            alert("删除成功!");
          }
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    },
    setquestions(wid) {
      this.$router.push({
        name: "setquestions",
        params: { wid: wid, cid: this.cid },
      });
    },
    see(wid) {
      this.$router.push({
        name: "totalAnswer",
        params: { wid: wid, cid: this.cid },
      });
    },
    showProblem(status) {
      axios
        .post(
          "http://127.0.0.1:8000/showProblems/",
          { cid: this.cid, status: status, username: this.username },
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        )
        .then((response) => {
          console.log(response.data);
          if (response.data.status == "success") {
            this.problems = response.data.problems;
          }
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    },
    gototiwen() {
      this.tiwenShow = true;
    },
    tiwenback() {
      this.tiwenShow = false;
    },
    submitProblems() {
      if (this.new_pinfo === ""){
        this.$message.error('问题不能为空');
        return;
      }
      axios
        .post(
          "http://127.0.0.1:8000/saveProblems/",
          { cid: this.cid, info: this.new_pinfo, username: this.username },
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        )
        .then((response) => {
          console.log(response.data);
          if (response.data.status == "success") {
            this.problems = response.data.problems;
            this.tiwenShow = false;
            this.new_pinfo = "";
          }
        })
        .catch((error) => {
          console.error("Error:", error);
        });
        this.askFormVisible=false;
    },
    classBegin() {
      axios
        .post(
          "http://127.0.0.1:8000/beginClass/",
          { cid: this.cid },
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        )
        .then((response) => {
          console.log(response.data);
          this.$router.push({
            name: "zhibodemo",
            params: { uid: this.username, cid: this.cid },
          });
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    },
  },
};
</script>

<style scoped>
.modal {
  position: fixed;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5); /* 半透明背景 */
  display: flex;
  justify-content: center;
  align-items: center;
}
.modal-content {
  background-color: #fff;
  padding: 20px;
  border-radius: 5px;
  width: 300px;
  height: 200px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.headbox {
  background: linear-gradient(#f59a23, white);
}

/* 返回 */
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
  vertical-align: middle; /* 垂直居中对齐 */
  width: 30px; /* 设置图片宽度 */
  height: auto; /* 保持图片宽高比 */
}

.back-text {
  display: inline-block;
  vertical-align: middle; /* 垂直居中对齐 */
  font-size: 20px;
}

/* 按钮 */
.rightbtn {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
}

.rightbtn button {
  background-color: #f59a23b0;
  color: white;
  border: #f59a23;
  font-size: 15px;
  border-radius: 10px;
  margin: 15px;
  height: 40px;
  width: 100px;
}

.info {
  border: 1px #797979 solid;
  margin: 50px;
  padding-top: 20px;
}
.info p {
  text-align: left;
  margin-top: 0;
  word-wrap: break-word;
  max-width: 300px;
}

.info h3 {
  text-align: left;
  margin-left: 30px;
  margin-top: 0;
}

.info div {
  display: flex;
  align-items: baseline;
  margin-top: 0px;
}

.askbtn {
  display: flex;
}

.sendaskbtn {
  background-color: #f59a23b0;
  color: white;
  border: #f59a23;
  font-size: 15px;
  border-radius: 10px;
  margin-bottom: 20px;
  margin-left: 10px;
  margin-right: 20px;
  height: 40px;
  width: 60px;
}

.askbtn button:not(.sendaskbtn) {
  background-color: white;
  border: 2px solid #f59a23;
  color: black;
  font-size: 15px;
  border-radius: 10px;
  margin-bottom: 20px;
  margin-left: 10px;
  margin-right: 20px;
  height: 40px;
  width: 60px;
}

.question {
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  position: relative; 
}

.question h4{
  margin-top: 0;
}
.question p {
  margin-top: 0;
  margin-left: 10px;
  word-wrap: break-word;
}
.jh {
  position: absolute;
  top: 0;
  right: 0px;
}

.question button {
  background-color: white;
  border: 2px solid #f59a23;
  color: black;
  font-size: 15px;
  border-radius: 10px;
  height: 40px;
  width: 80px;
}

.workbtn {
  display: flex;
}

.newworkbtn {
  background-color: #f59a23b0;
  color: white;
  border: #f59a23;
  font-size: 15px;
  border-radius: 10px;
  margin-bottom: 20px;
  margin-left: 10px;
  margin-right: 20px;
  height: 40px;
  width: 80px;
}

.workbtn button:not(.newworkbtn) {
  background-color: white;
  border: 2px solid #f59a23;
  color: black;
  font-size: 15px;
  border-radius: 10px;
  margin-bottom: 20px;
  margin-left: 10px;
  margin-right: 20px;
  height: 40px;
  width: 80px;
}

.workbox button{
  background-color: white;
  border: 2px solid #f59a23;
  color: black;
  font-size: 13px;
  border-radius: 10px;
  height: 30px;
  width: 80px;
}

h4{
  margin-top: 0;
}

.videobox button{
  background-color: white;
  border: 2px solid #f59a23;
  color: black;
  font-size: 13px;
  border-radius: 10px;
  height: 30px;
  width: 80px;
}
.like{
  position: absolute;
  top: 0;
  right: 0px;
  display: flex; 
  align-items: center;
}

.like button{
  border:0;
  margin-right: 0;
}

.like img {
  display: block; /* 移除img的默认行内间距 */
}

.like p {
  margin:0;
  margin-left: 10px;
  display: flex;
  align-items: center;
  font-size: 15px;
}

.like button{
  width:24px;
  height:24px;
}





</style>
