<template>
<!-- 学生端在我的课堂点击已选课程后进入的具体的课程页面 -->
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
                
        学时:{{ course.xueshi }}
        {{ course.status }}
        <button v-show="!this.zhiboShow">直播未开始</button>
        <button v-show="this.zhiboShow"@click="classBegin">进入直播</button>
    </div>
    <!-- 服务 -->
    <div>
        <el-tabs v-model="activeName" @tab-click="handleClick">
            <el-tab-pane label="学习资源" name="first">学习资源</el-tab-pane>
            <el-tab-pane label="作业" name="second">作业</el-tab-pane>
            <el-tab-pane label="问答" name="third">问答</el-tab-pane>
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
                <span>{{ node.label }}</span>
                <span v-show="data.path">
                  
                  <button @click="dowloadFile(data.path,data.label)">下载</button>
                  <button @click="watchFile(data.path)">观看</button>
              
                </span>
            </span>
            </el-tree>
        </div>
    </div>
     <!-- 作业 -->
     <div v-show="sencondshow">
        <div>
            <button @click="showWork('ing')">未截止</button>
            <button @click="showWork('ed')">已截止</button>
            <button @click="showWork('all')">全部</button>
        </div>

        <div>
            <el-row v-for="work in works" :key="work.wid">  
                {{ work.wid }}
                
                {{ work.wname }}    
               开始时间{{ work.begin }}
               截止时间{{ work.end }}
               <div v-if="wids.includes(work.wid)">
                {{statuses[work.wid]}}
                <button @click="see(work.wid)">查看</button>
               </div>
               <div v-else>
                <button @click="write(work.wid)">去完成</button>
               </div>
               
            </el-row>
        </div>
     </div>
      <!-- 直播回放 -->
    <div v-show="fifthshow">
      <el-row v-for="date in mp4Files" :key="date.period">
            {{ date.period }}
            <el-row v-for="mp4 in date.records" :key="mp4.path">
                {{ mp4.rname }}
                <button @click="dowloadFile(mp4.path,mp4.rname)">下载</button>
                <button @click="watchFile(mp4.path)">观看</button>
          </el-row>
      </el-row>
    </div>

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
    }
  },
  data () {
    return {
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
      mp4Files:'',
      paths:[],
      rootpath:'',

      data:[]

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
        this.$router.push({ name: 'dianbo' ,params:{"path":path,'cid':this.cid,'role':this.role}})
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
        }
        else {
          
            this.firstshow = false
            this.sencondshow = false
            this.thirdshow = false
            this.fourthshow = false
            this.fifthshow = true
        
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

</style>
