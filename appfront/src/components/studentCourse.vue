<template>
<!-- 学生端在我的课堂点击已选课程后进入的具体的课程页面 -->
<div>
      <!-- 导航栏 -->
  <div>
      <Daohanglan :isLoggedIn="isLoggedIn" :username="username"></Daohanglan>
  </div>

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
    
   <!-- 课程介绍 -->
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
            <button v-show="!this.zhiboShow">直播未开始</button>
            <button v-show="this.zhiboShow" @click="classBegin">进入直播</button>
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
                    :expand-on-click-node="false">
                    <span class="custom-tree-node" slot-scope="{ node, data }">
                        <span>{{ node.label }}</span>
                        <span v-show="data.path">
                          
                          <el-button @click="dowloadFile(data.path,data.label)" size="mini" type="text">下载</el-button>
                          <el-button @click="watchFile(data.path)" size="mini" type="text">观看</el-button>
                      
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
                </div>

              <div class = "workbox">
                <el-row v-for="work in works" :key="work.wid">
                  <el-divider></el-divider>
                  <el-row :gutter="20">
                    <el-col :span="3" :offset="6">
                      <h4>{{ work.wname }}</h4>
                    </el-col>
                    <el-col :span="10" :offset="5">
                      <div v-if="wids.includes(work.wid)">
                        {{statuses[work.wid]}}
                        <button @click="see(work.wid)">查看</button>
                      </div>
                      <div v-else>
                        <button @click="write(work.wid)">去完成</button>
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
                      <p>发布时间：{{ problem.t }}</p>
                      <p></p>
                      <div v-if="problem.jh == 1" class="jh">精华</div>
                      <button @click="huifu(problem.pid)">查看详情</button>
                      
                    </div>
                  </div>
                </el-row>
              </div>
              
            </el-tab-pane>
     
      <!-- 直播回放 -->
      <el-tab-pane label="直播回放" name="fifth">
              <div v-show="fifthshow">
                <el-row v-for="date in mp4Files" :key="date.period">
                  <el-divider></el-divider>
                  <h5>{{ date.period }}</h5>
                  <el-row v-for="mp4 in date.records" :key="mp4.path">
                    <div class="videobox">
                    <h4>{{ mp4.rname }}</h4>
                    <button @click="dowloadFile(mp4.path,mp4.rname)">下载</button>
                    <button @click="watchFile(mp4.path)">观看</button>                                   
                    </div>
                  </el-row>
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

    <!-- 发布评论弹窗 -->
    <el-dialog title="发布评论" :visible.sync="commentFormVisible">
      <el-form :model="form">
        <el-form-item label="评论" >
          <el-input v-model="newcomment" autocomplete="off" clearable type="textarea" :rows="2" placeholder="请输入评论" this.input=''></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="commentFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="submitComment">确 定</el-button>
      </div>
    </el-dialog>
</div>

</template>

<script>
import axios from 'axios'
import Daohanglan from './daohanglan.vue';
export default {
  name: 'studentCourse',
  props: ['cid'],
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
    },
    currentrole(){
      return this.$store.state.username.currentrole;
  }
  },
  data () {
    return {
      activeName: 'first',
      course:'',
      works:[],
      wids:[],
      statuses:{},
      teacher:'',
      zhibo:'',
      zhiboShow:false,
      firstshow:true,
      sencondshow:false,
      thirdshow:false,
      fourthshow:false,
      fifthshow:false,
      mp4Files: [],
      paths:[],
      rootpath:'',

      data:[],

      fabushow:false,
      new_wname:'',
      newbegin:'',
      newend:'',
      problems:[],
      tiwenShow:false,
      new_pinfo:'',

      comments:[],
      newcomment:'',
      commentFormVisible:false,
      askFormVisible: false,
      workFormVisible: false,
      renameFormVisible : false,
      uploadFormVisible :false,
    }
  },
  created(){
    
    axios.post("http://127.0.0.1:8000/showCourse/",{'cid':this.cid},{
      headers: {
        'Content-Type': 'multipart/form-data'
      }
  })
      .then(response =>{
        console.log(response.data)
        if(response.data.status == 'success'){
          this.course = response.data.course
          this.teacher = this.course.u
          this.zhibo = this.course.zhibo
          if(this.zhibo == '暂无直播'){
            this.zhiboShow = false
          }else{
            this.zhiboShow = true
          }
        }
         
      })
      .catch(error => {
        console.error('Error:', error);
      });
       this.getmp4List()
      this.searchLM()
  },
  methods:{
    back() {
      this.$router.push({ name: "studentPage" });
    },
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
        axios.post( "http://127.0.0.1:8000/showComments/",   { cid: this.cid, username:this.username},
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
    huifu(pid){
        this.$router.push({ name: 'problem' ,params:{'cid':this.cid,'pid':pid}})
    },
        showProblem(status){
        axios.post("http://127.0.0.1:8000/showProblems/",{'cid':this.cid,'status':status,'username':this.username},{
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        })
            .then(response =>{
                console.log(response.data)
                if(response.data.status == 'success'){
                this.problems = response.data.problems
                }
                
            })
            .catch(error => {
                console.error('Error:', error);
            });
    },
    gototiwen(){
        this.tiwenShow = true
    },
    tiwenback(){
        this.tiwenShow = false
    },
    submitProblems(){
        axios.post("http://127.0.0.1:8000/saveProblems/",{'cid':this.cid,'info':this.new_pinfo,'username':this.username},{
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    })
        .then(response =>{
            console.log(response.data)
            if(response.data.status == 'success'){
            this.problems = response.data.problems
            this.tiwenShow = false
            this.new_pinfo = ''
            }
            
        })
        .catch(error => {
            console.error('Error:', error);
        });
        this.askFormVisible=false;
    },
    searchLM(){
        axios.post("http://127.0.0.1:8000/searchLM/",{'cid':this.cid},{
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    })
        .then(response =>{
            console.log(response.data)
            if(response.data.status == 'success'){
                console.log(response.data)
                this.data = response.data.res
                console.log(this.data)
            }
            
        })
        .catch(error => {
            console.error('Error:', error);
            
        });
    },
    watchFile(path){
        this.$router.push({ name: 'dianbo' ,params:{"path":path,'cid':this.cid,'role':this.currentrole}})
    },
    getmp4List(){
        axios.post("http://127.0.0.1:8000/getRecordsList/",{'cid':this.cid},{
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        })
            .then(response =>{
                console.log(response.data)
                if(response.data.status == 'success'){
                    this.mp4Files = response.data.res
                }
                
            })
            .catch(error => {
                console.error('Error:', error);
            });
    },
    dowloadFile(filepath,rname){
        const downloadUrl = 'https://zlm.com/index/api/downloadFile?file_path='+filepath
     
      fetch(downloadUrl)
      .then(response => response.blob())
      .then(blob => {
        const url = window.URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.href = url;
        link.download = rname; // 指定下载文件的名称
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        window.URL.revokeObjectURL(url);
      })
      .catch(error => console.error('下载失败:', error));
    },
    write(wid){
        this.$router.push({ name: 'homework' ,params:{"wid":wid,'cid':this.cid}})
    },
    handleClick(tab) {
        if(tab.name == 'first'){
          this.searchLM();
            this.firstshow = true
            this.sencondshow = false
            this.thirdshow = false
            this.fifthshow = false
        }
        else if(tab.name == 'second'){
            this.showWork('all')
        //     axios.post("http://127.0.0.1:8000/studentWorks/",{'cid':this.cid,'status':'all','username':this.username},{
        //     headers: {
        //         'Content-Type': 'multipart/form-data'
        //     }
        // })
        //     .then(response =>{
        //         console.log(response.data)
        //         if(response.data.status == 'success'){
        //         this.works = response.data.works
        //         this.wids = response.data.wids
        //         }
                
        //     })
        //     .catch(error => {
        //         console.error('Error:', error);
        //     });
            this.firstshow = false
            this.sencondshow = true
            this.thirdshow = false
            this.fifthshow = false
        }else if(tab.name == 'third'){
            this.firstshow = false
            this.sencondshow = false
            this.thirdshow = true
            this.fifthshow = false
            this.showProblem('all')
        }
        else if (tab.name == "fourth") {
            this.firstshow = false;
            this.sencondshow = false;
            this.thirdshow = false;
            this.fourthshow = true;
            this.showComments()
        }
        else {       
            this.firstshow = false
            this.sencondshow = false
            this.thirdshow = false
            this.fourthshow = false
            this.fifthshow = true
            this.getmp4List()
        }
      },
      showWork(status){
        axios.post("http://127.0.0.1:8000/studentWorks/",{'cid':this.cid,'status':status,'username':this.username},{
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        })
            .then(response =>{
                console.log(response.data)
                if(response.data.status == 'success'){
                this.works = response.data.works
                this.wids = response.data.wids
                this.statuses = response.data.statuses
                }
                
            })
            .catch(error => {
                console.error('Error:', error);
            });
      },
      
        see(wid){
      this.$router.push({ name: 'myWork' ,params:{"wid":wid,'cid':this.cid}})
      },
      classBegin(){
        this.$router.push({ name: 'studentzhibo' ,params:{"uid":this.username,'cid':this.cid,'teacherid':this.teacher}})
    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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

.workbtn {
  display: flex;
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

.workbtn button {
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

h4{
  margin-top: 0;
}

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

.videobox button{
  background-color: white;
  border: 2px solid #f59a23;
  color: black;
  font-size: 13px;
  border-radius: 10px;
  height: 30px;
  width: 80px;
}

.deletebtn{
  position: absolute;
  bottom: 0;
  right: 0px;
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
