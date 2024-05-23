<template>
  <div class="hello">
    
   <button @click="getDate">获取日期</button>
   <button @click="getFileList">获取流列表</button>
    <video id="videoPlayer" width="640" height="480" controls>
      
    </video>
    <button @click="play">播放</button>
    <button @click="dowloadFile">下载</button>
    <button @click="dianbo">点播</button>
    <video width="320" height="240" controls
      src="https://zlm.com/index/api/downloadFile?file_path=/home/xu/demo1/ZLMediaKit/release/linux/Debug/www/lubo/test.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>
    <input type="file" ref="videoInput" @change="handleFileChange" />
    <button @click="uploadVideo">上传视频</button>
    
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'HelloWorld',
  data () {
    return {
      username: '',  
      password: '',  
      videoFile: null,
      msg: 'Welcome to Your Vue.js App'
    }
  },
  methods:{
    handleFileChange(event) {
      this.videoFile = event.target.files[0];
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
        
         
      })
      .catch(error => {
        console.error('Error:', error);
      });
      
    },
    dianbo(){
      axios.get("https://zlm.com/index/api/loadMP4File?secret=x5mji1hHaDRVAsMCYUIrChqhmcgbozR1&vhost=192.168.44.129&app=live&stream=7fd84787desk&file_path=/home/xu/demo1/ZLMediaKit/release/linux/Debug/www/record/live/7fd84787desk/2024-05-18/20-46-08-0.mp4",{

      }) .then(response =>{
                console.log(response.data)
                
            })

            .catch(error => {
                
                console.error('Error:', error);
            });
    },
    dowloadFile(){
      const downloadUrl = 'https://zlm.com/index/api/downloadFile?file_path=/home/xu/demo1/ZLMediaKit/release/linux/Debug/www/record/live/7fd84787desk/2024-05-18/20-46-08-0.mp4'
     
      fetch(downloadUrl)
      .then(response => response.blob())
      .then(blob => {
        const url = window.URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.href = url;
        link.download = 'video.mp4'; // 指定下载文件的名称
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        window.URL.revokeObjectURL(url);
      })
      .catch(error => console.error('下载失败:', error));

      },
    play(){
      document.getElementById('videoPlayer').src = "https://zlm.com/index/api/downloadFile?file_path=/home/xu/demo1/ZLMediaKit/release/linux/Debug/www/record/live/7fd84787desk/2024-05-18/20-46-08-0.mp4"
      
    },
    
    getDate(){
        var currentDate = new Date();
        var year = currentDate.getFullYear(); // 获取完整的年份
        var month = currentDate.getMonth() + 1; // 获取月份，注意 JavaScript 中月份是从 0 开始计数的
        var day = currentDate.getDate(); // 获取日期
        if(month<10){
            month = '0'+month
        }
        if(day.length<10){
            day = '0'+day
        }
        let today = year+'-'+month+'-'+day
        console.log(month.length)
        console.log(today)
        return today
    },
    getFileList(){//获取今天的直播录屏
        let today = this.getDate()
        axios.get("https://zlm.com/index/api/getMp4RecordFile?secret=x5mji1hHaDRVAsMCYUIrChqhmcgbozR1&vhost=192.168.44.129&app=live&stream=7fd84787"+"desk&customized_path=&period="+today,{
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        })
            .then(response =>{
                console.log(response.data)
                let rootPath = response.data.data.rootPath
                let paths = response.data.data.paths
                console.log(rootPath)
                console.log(paths)
                this.updateRecord(rootPath,paths)
            })

            .catch(error => {
                
                console.error('Error:', error);
            });
    },
    updateRecord(rootPath,paths){
      let today = this.getDate()
        axios.post("http://127.0.0.1:8000/updateRecords/",{'cid':'7fd84787','rootPath':rootPath,'paths':JSON.stringify(paths),'period':today},{
      headers: {
        'Content-Type': 'multipart/form-data'
      }
  })
      .then(response =>{
        console.log(response.data)
        
         
      })
      .catch(error => {
        console.error('Error:', error);
      });

    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
