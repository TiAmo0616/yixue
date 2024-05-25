<template>
<div>
    <!-- 导航栏 -->
    <div>
        <Daohanglan :isLoggedIn="isLoggedIn" :username="username"></Daohanglan>
    </div>
    <!-- 课程介绍 -->
    <div>
        <img :src="course.img" alt="" width="200"/>
              
        {{ course.cname }}
        课程码{{ this.cid }}     
        {{ course.introduction }}
        学生人数：{{ course.stuNum }}
        学时:{{ course.xueshi }}
        {{ course.status }}
        <button @click="setClass">课程设置</button>
        <button @click="classBegin">开始直播</button>
    </div>
    <!-- 服务 -->
    <div>
        <el-tabs v-model="activeName" @tab-click="handleClick">
            <el-tab-pane label="学习资源" name="first">学习资源</el-tab-pane>
            <el-tab-pane label="作业" name="second">作业</el-tab-pane>
            <el-tab-pane label="问答" name="third">答疑</el-tab-pane>
            <el-tab-pane label="学生管理" name="fourth">学生管理</el-tab-pane>
            <el-tab-pane label="直播回放" name="fifth">直播回放</el-tab-pane>
        </el-tabs>
    </div>
    <!-- 学习资源（录播课程） -->
    <div v-show="firstshow">
        <div class="block">
            <el-tree
            :data="data"
            node-key="id"
            default-expand-all
            :expand-on-click-node="false">
            <span class="custom-tree-node" slot-scope="{ node, data }">
                <!-- <span>{{ node.label }}</span> -->
                <input v-if="isLabelEditing&&editId == node.id" type="text" v-model="data.label" />
                <span v-else>{{ node.label }}</span>
                <!-- <span v-if="!isEditing">{{ node.label }}</span>
                <input v-else type="text" v-model="data.label" /> -->
                <el-button v-if="isLabelEditing&&editId == node.id" type="text" size="mini" @click="editLabel(node,data)">确认</el-button>
                <el-button v-else type="text" size="mini" @click="startEdit(node)">编辑</el-button>
                <span>
                <el-button
                    type="text"
                    size="mini"
                    @click="append(data)">
                    增加子级目录
                </el-button>
                <el-button
                    type="text"
                    size="mini"
                    @click="remove(node, data)">
                    删除目录
                </el-button>
                <el-button
                    type="text"
                    size="mini"
                    @click="upload(data)">
                    上传文件
                </el-button>
                
              
                </span>
            </span>
            </el-tree>
        </div>


        <div v-show="isUpload">
            <input type="file" ref="videoInput" @change="handleFileChange" />
            <button @click="uploadVideo">上传资源</button>
        </div>
        
        
    </div>
    <!-- 作业 -->
    <div v-show="sencondshow">
        <div>
            <button @click="showWork('ing')">未截止</button>
            <button @click="showWork('ed')">已截止</button>
            <button @click="showWork('all')">全部</button>
            <button @click="gotofabu">发布</button>
            
        </div>

        <div>
            <el-row v-for="work in works" :key="work.wid">
               
                {{ work.wname }}
                
               开始时间{{ work.begin }}
               截止时间{{ work.end }}
               <button @click="deleteWork(work.wid)">删除</button>
               <button @click="setquestions(work.wid)">设置题目</button>
               <button @click="see(work.wid)">查看</button>
            </el-row>
        </div>
        <!-- 发布作业 -->
        <div v-show="fabushow" class="modal">
            <div class="modal-content">
            <form @submit.prevent="submitfabu">  
                <div class="form-group">  
                <label for="new_wname">作业标题：</label>  
                <input type="text" id="new_wname" v-model="new_wname" required>  
                </div>  
                
                <div class="form-group">  
                    <label for="info">开始时间</label>  
                    <el-date-picker
                        v-model="newbegin"
                        type="datetime"
                        placeholder="选择日期时间">
                    </el-date-picker>
                </div>  

                <div class="form-group">  
                    <label for="info">截止时间</label>  
                    <el-date-picker
                        v-model="newend"
                        type="datetime"
                        placeholder="选择日期时间">
                    </el-date-picker>
                </div>  

                <button type="submit">确认创建</button>  
                <button @click="workback">取消</button>
            </form>  
            </div>
        </div>
        <!-- 发布作业end -->
    </div>
    <!-- 问答 -->
    <div v-show="thirdshow">
        <div>
            <button @click="showProblem('my')">我的</button>
            <button @click="showProblem('jh')">精华</button>
            <button @click="showProblem('all')">全部</button>
            <button @click="gototiwen">发布</button>
        </div>

        
        <div>
            <el-row v-for="problem in problems" :key="problem.pid">
               {{ problem.pinfo }}
               用户{{ problem.askername }}
               <button @click="huifu(problem.pid)">回复</button>
            </el-row>
        </div>
        <!-- 去提问 -->
        <div v-show="tiwenShow" class="modal">
            <div class="modal-content">
            <form @submit.prevent="submitProblems">  
                <div class="form-group">  
                <label for="new_wname">请输入问题：</label>  
                <input type="textarea" v-model="new_pinfo" required>  
                </div>  

                <button type="submit">确认提问</button>  
                <button @click="tiwenback">取消</button>
            </form>  
            </div>
        </div>
        <!-- 提问结束 -->
    </div>
    <!-- 学生管理 -->
    <div v-show="fourthshow">

    </div>
    <!-- 直播回放 -->
    <div v-show="fifthshow">
        <el-row v-for="date in mp4Files" :key="date.period">
            {{ date.period }}
            <el-row v-for="mp4 in date.records" :key="mp4.path">
                {{ mp4.rname }}
                <button @click="dowloadFile(mp4.path,mp4.rname)">下载</button>
                <button @click="watchFile(mp4.path)">观看</button>
                <button @click="rename(mp4.rname)">重命名</button>
            </el-row>
        </el-row>
        <!-- 重命名视频文件的输入框 -->
        <div v-show="isRenaming">
            <el-input
            placeholder="请输入内容"
            v-model="newrname"
            clearable>
            </el-input>
            <button @click="submitRename">确定</button>
        </div>
    </div>

</div>

</template>

<script>
import axios from 'axios'
import Daohanglan from './daohanglan.vue';

export default {

  name: 'singleCourse',
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
    //const data=[{id:0,label:'学习资源',children:[],path:''}]
    return {
      course:'',
      activeName: 'first',
      firstshow:true,
      sencondshow:false,
      thirdshow:false,
      fourthshow:false,
      fifthshow:false,
      works:[],
      fabushow:false,
      new_wname:'',
      newbegin:'',
      newend:'',
      problems:[],
      tiwenShow:false,
      new_pinfo:'',

      mp4Files:'',
      paths:[],
      rootpath:'',
      isRenaming:false,
      newrname:'',
      oldrname:'',

      //data: JSON.parse(JSON.stringify(data)),
      data:[],
      isEditing:false,
      isUpload:false,
      currentData:null,
      beginId:0,
      editId:'',
      isLabelEditing:false,

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
        }
         
      })
      .catch(error => {
        console.error('Error:', error);
      });
      this.getmp4List()
      this.searchLM()
  },
  
  methods: {
    setClass(){
        this.$router.push({ name: 'lessonInfo' ,params:{'cid':this.cid}})
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
                this.beginId = response.data.maxId
                console.log(this.data)
            }
            
        })
        .catch(error => {
            console.error('Error:', error);
            
        });
    },
    upload(data){
        this.isUpload = true
        this.currentData = data
        
    },
    startEdit(node) {
      this.isEditing = true;
      this.isLabelEditing = true
      this.editId = node.id
    },
    editLabel(node, data) {
      this.isEditing = false;
      this.isLabelEditing = false;
      console.log(node)
      axios.post("http://127.0.0.1:8000/editDirectory/",{'cid':this.cid,'id':node.data.did,'label':node.label},{
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        })
            .then(response =>{
                console.log(response.data)
                if(response.data.status == 'success'){
                    console.log(response.data)
                }
                
            })
            .catch(error => {
                console.error('Error:', error);
                
            });

    },
    //只是创建目录
    append(data) {
        let id = this.beginId++
        axios.post("http://127.0.0.1:8000/appendLM/",{'cid':this.cid,'id':id,label:'目录'+id,'pdid':data.did,'path':''},{
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        })
            .then(response =>{
                console.log(response.data)
                if(response.data.status == 'success'){
                    console.log(response.data)
                    const newChild = { id: id, label: '目录'+id, children: [],path:'' };
                    if (!data.children) {
                        this.$set(data, 'children', []);
                    }
                    data.children.push(newChild);
                }
                
            })
            .catch(error => {
                console.error('Error:', error);
                
            });


        
      },
      //上传视频作为子目录
      appendVideo(data,rname,path) {
        let id = this.beginId++
        console.log(data)
        axios.post("http://127.0.0.1:8000/appendLM/",{'cid':this.cid,'id':id,label:rname,'pdid':data.did,'path':path},{
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        })
            .then(response =>{
                console.log(response.data)
                if(response.data.status == 'success'){
                    console.log(response.data)
                    const newChild = { id: id, label: rname, children: [],path:path };
                    if (!data.children) {
                    this.$set(data, 'children', []);
                    }
                    data.children.push(newChild);
                }
                
            })
            .catch(error => {
                console.error('Error:', error);
                
            });

        
      },
    handleFileChange(event) {
      this.videoFile = event.target.files[0];
    },
    remove(node, data) {

        axios.post("http://127.0.0.1:8000/deleteLM/",{'cid':this.cid,'id':data.did},{
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        })
            .then(response =>{
                console.log(response.data)
                if(response.data.status == 'success'){
                    console.log(response.data)
                    const parent = node.parent;
                    const children = parent.data.children || parent.data;
                    const index = children.findIndex(d => d.did === data.did);
                    children.splice(index, 1);
                }
                
            })
            .catch(error => {
                console.error('Error:', error);
                
            });



      },
      renderContent(h, { node, data, store }) {
        return (
          <span class="custom-tree-node">
            <span>{node.label}</span>
            <span>
              <el-button size="mini" type="text" on-click={ () => this.append(data) }>Append</el-button>
              <el-button size="mini" type="text" on-click={ () => this.remove(node, data) }>Delete</el-button>
            </span>
          </span>);
      },
    uploadVideo() {
      if (!this.videoFile) {
        alert('请先选择视频文件。');
        return;
      }

      const formData = new FormData();
      formData.append('video', this.videoFile);

      axios.post("http://127.0.0.1:8000/uploadVideo/",formData,{
      headers: {
        'Content-Type': 'multipart/form-data'
      }
  })
      .then(response =>{
        console.log(response.data)
        if(response.data.status == 'success'){
            alert("上传成功！")
            this.isUpload = false
            console.log(this.currentData)
            this.appendVideo(this.currentData,response.data.rname,response.data.path)
        }
         
      })
      .catch(error => {
        console.error('Error:', error);
        alert("上传失败！请重试！")
      });
      
    },
    rename(oldrname){
        this.isRenaming = true
        this.oldrname = oldrname
    },
    submitRename(){
        axios.post("http://127.0.0.1:8000/reName/",{'cid':this.cid,'rname':this.oldrname,'newrname':this.newrname},{
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        })
            .then(response =>{
                console.log(response.data)
                if(response.data.status == 'success'){
                    this.isRenaming = false
                    this.getmp4List()
                }
                
            })
            .catch(error => {
                console.error('Error:', error);
            });
    },
    watchFile(path){
        this.$router.push({ name: 'dianbo' ,params:{"path":path,'cid':this.cid}})
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
    workback(){
        this.fabushow = false
        this.new_wname = ''
        this.newbegin = ''
        this.newend = ''
    },
      handleClick(tab) {
        if(tab.name == 'first'){
            this.searchLM()
            this.firstshow = true
            this.sencondshow = false
            this.thirdshow = false
            this.fourthshow = false
        }
        else if(tab.name == 'second'){
            axios.post("http://127.0.0.1:8000/showWorks/",{'cid':this.cid,'status':'all'},{
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        })
            .then(response =>{
                console.log(response.data)
                if(response.data.status == 'success'){
                this.works = response.data.works
                }
                
            })
            .catch(error => {
                console.error('Error:', error);
            });
            this.firstshow = false
            this.sencondshow = true
            this.thirdshow = false
            this.fourthshow = false
        }else if(tab.name == 'third'){
            this.firstshow = false
            this.sencondshow = false
            this.thirdshow = true
            this.fourthshow = false
            this.showProblem('all')
        }
        else if(tab.name == 'fourth'){
            this.firstshow = false
            this.sencondshow = false
            this.thirdshow = false
            this.fourthshow = true
        }
        else{
            this.firstshow = false
            this.sencondshow = false
            this.thirdshow = false
            this.fourthshow = false
            this.fifthshow = true
        }
      },
      showWork(status){
        axios.post("http://127.0.0.1:8000/showWorks/",{'cid':this.cid,'status':status},{
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        })
            .then(response =>{
                console.log(response.data)
                if(response.data.status == 'success'){
                this.works = response.data.works
                }
                
            })
            .catch(error => {
                console.error('Error:', error);
            });
      },
    gotofabu(){
        this.fabushow = true
      },
    submitfabu(){
        var moment = require('moment')
        let g = moment.utc(this.newbegin).toDate()
        let t = moment(g).format('YYYY-MM-DD HH:mm:ss')
        let eg = moment.utc(this.newend).toDate()
        let et = moment(eg).format('YYYY-MM-DD HH:mm:ss')

        axios.post("http://127.0.0.1:8000/createWork/",{'cid':this.cid,'wname':this.new_wname,'begin':t,'end':et},{
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    })
        .then(response =>{
            console.log(response.data)
            if(response.data.status == 'success'){
            this.works = response.data.works
            this.fabushow = false
            this.new_wname = ''
            this.newbegin = ''
            this.newend = ''
            }
            
        })
        .catch(error => {
            console.error('Error:', error);
        });
        },
    deleteWork(wid){
        axios.post("http://127.0.0.1:8000/deleteWork/",{'wid':wid},{
        headers: {'Content-Type': 'multipart/form-data'}
    })
        .then(response =>{
            console.log(response.data)
            if(response.data.status == 'success'){
                this.works = response.data.works
                alert("删除成功!")
            }
            
        })
        .catch(error => {
            console.error('Error:', error);
        });
    },
    setquestions(wid){
        this.$router.push({ name: 'setquestions' ,params:{"wid":wid,'cid':this.cid}})
    },
    see(wid){
        this.$router.push({ name: 'totalAnswer' ,params:{"wid":wid,'cid':this.cid}})
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
    },
    classBegin(){
        axios.post("http://127.0.0.1:8000/beginClass/",{'cid':this.cid},{
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    })
        .then(response =>{
            console.log(response.data)
            this.$router.push({ name: 'zhibodemo' ,params:{"uid":this.username,'cid':this.cid}})
            
        })
        .catch(error => {
            console.error('Error:', error);
        });
        
    },
    }
}
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

</style>
