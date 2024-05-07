<template>
    <div class="play-content">

       <el-row>
            <el-col :span="18">
                <!-- 主要直播界面，屏幕共享，如果不共享就是摄像头画面 -->
                <div class="mainVideo">
                    <video id='selfVideo' controls autoplay style="text-align:right;" width="100%">
                        Your browser is too old which doesn't support HTML5 video.
                    </video>   
                    
                </div>
                    <!-- 直播开启前的选择 -->
                    <div v-if="!this.isplaying">
                        <!-- <el-row>
                            <el-col :span="2">
                                <el-checkbox v-model="useCamera">摄像头</el-checkbox> 
                            </el-col>
                            <el-col :span="2">
                                <el-checkbox v-model="audioEnable">麦克风</el-checkbox>
                            </el-col>
                            <el-col :span="2">
                                <el-checkbox v-model="usescreen">屏幕共享</el-checkbox>
                            </el-col>
                            <el-col :span="2">
                                <button @click="start">开启直播</button>   
                            </el-col>
                        </el-row> -->
                        <!-- <button @click="start">开启直播</button>    -->
                    </div>
                        
                    <div v-else>
                        <el-row>
                            <el-col :span="4">
                                <div v-if="this.audioEnable">
                                    <el-button type="primary" icon="el-icon-microphone" @click="closeMIC"></el-button>
                                </div>
                                <div v-else>
                                    <el-button type="primary" icon="el-icon-turn-off-microphone" @click="openMIC"></el-button>
                                </div>
                                
                            </el-col>
                            <el-col :span="4">
                                <div v-if="!this.useCamera">
                                    <el-button type="primary" icon="el-icon-video-camera" @click="openCamera">打开</el-button>
                                </div>
                                <div v-else>
                                    <el-button type="primary" icon="el-icon-video-camera-solid" @click="closeCamera">关闭</el-button>
                                </div>
                            </el-col>
                            <el-col :span="4">
                                <div v-if="!this.usescreen">
                                    <el-button @click="openScreen">开启屏幕共享</el-button>
                                </div>
                                <div v-else>
                                    <el-button @click="closeScreen">关闭屏幕共享</el-button>
                                </div>
                               
                            </el-col>
                            <el-col :span="2">
                                <button @click="agreehand">同意举手</button>
                                <button v-show="this.agree" @click="closeHand">关闭举手</button>
                            </el-col>
                            <el-col :span="4">
                                <button @click="stop">结束直播</button>    
                            </el-col>
                        </el-row>
                      
                    </div>
            </el-col>
            <el-col :span="6">
                
                <div id="rside">
                    <!-- 教师自己的摄像头画面 -->
                    <div v-if="this.useCamera">
                        <video id='cameraVideo' controls autoplay style="text-align:right;" width="100%">
                            Your browser is too old which doesn't support HTML5 video.
                        </video>   
                    </div>
                    <div v-else>
                        <!-- <img src="../assets/t.jpeg" width="100%" height="200px"> -->
                        <img :src="image" alt="" width="100%" height="200px"/>
                    </div>

                    <!-- 连麦开启视频 -->
                    <div v-show="this.agree">
                        <div v-show="this.have2">
                        <video id='studentVideo' controls autoplay ></video>
                        </div>
                        <div v-show="!this.have2">
                            <img src="../assets/s.jpg" width="100%" height="200px">
                        </div>
                        <div>
                            <video v-show="false" id='studentAudio' controls autoplay >
                                Your browser is too old which doesn't support HTML5 video.
                        </video> 
                        </div>
                    </div>
                    

                </div>
            </el-col>
       </el-row>
    

    


    
  </div>
</template>

<script>
import axios from 'axios'
import ZLMRTCClient from '../utils/ZLMRTCClient';
export default {
  name: 'zhibodemo',
  props: ['uid','cid'],
  data () {
    return {
        streamUrl:'',
        h:720,
        w:1280,
        player:null,
        player1:null,
        recvOnl:false,
        resArr:[],
        playUrl:'',
        useCamera:false,
        audioEnable:true,
        videoEnable:false,
        recvOnly:false,
        usescreen:false,
        v1:'',
        v2:'',
        player2:null,
        isplaying:false,
        pusher1:null,
        pusher2:null,
        agree:false,
        have2:false,
        image:null,

        drawws:null,
		draw: null,
		drawColor: '#000000',
		fillColor:'#000000',
		drawLineWidth: 1,
		drawType: '画笔',
		lineEndType: '默认',
		lineNodeType: '默认',
		drawcanvas: '',
		drawctx:'',
		isDraw :1,
		msg:'',
		loadDraw:1,
		showcanvas:null,
		showctx:'',
    }
  },
  created(){
    axios.post("http://127.0.0.1:8000/showInfo/",{'username':this.uid},{
      headers: {
        'Content-Type': 'multipart/form-data'
      }
  })
      .then(response =>{
        console.log(response.data)
        this.image = response.data.img
      })

      .catch(error => {
        
        console.error('Error:', error);
      });
      this.start()
  },
  methods:{
    startPlay () {
       
        
      this.player = new ZLMRTCClient.Endpoint({
        element: document.getElementById('selfvideo'), // video 标签
        debug: false, // 是否打印日志
        zlmsdpUrl: "https://zlm.com/index/api/webrtc?app=live&stream=test&type=push", //流地址
        simulcast: false,
        useCamera: !this.usescreen,
        audioEnable: true,
        videoEnable: true,
        recvOnly: this.recvOnly,
        resolution: { w: this.w, h: this.h },
        usedatachannel: false
      })
      
      return new Promise((resolve, reject) => {
      this.player.on(ZLMRTCClient.Events.WEBRTC_ON_LOCAL_STREAM,function(s){
        
              // 获取到了本地流 
              document.getElementById('selfVideo').srcObject=s;
              document.getElementById('selfVideo').muted = true;
              resolve()
              //console.log('offer anwser 交换失败',e)
      });
      this.player.on(ZLMRTCClient.Events.WEBRTC_ICE_CANDIDATE_ERROR, function (e) {
        // ICE 协商出错
        console.log('ICE 协商出错')
      })

      this.player.on(ZLMRTCClient.Events.WEBRTC_ON_REMOTE_STREAMS, function (e) {
        //获取到了远端流，可以播放
        console.log('播放成功', e.streams)
      })

      this.player.on(ZLMRTCClient.Events.WEBRTC_OFFER_ANWSER_EXCHANGE_FAILED, function (e) {
        // offer anwser 交换失败
        console.log('offer anwser 交换失败', e)
        stop()
      })

      this.player.on(ZLMRTCClient.Events.CAPTURE_STREAM_FAILED, function (s) {
        // 获取本地流失败
        console.log('获取本地流失败')
        resolve()
      })

      this.player.on(ZLMRTCClient.Events.WEBRTC_ON_CONNECTION_STATE_CHANGE, function (state) {
        // RTC 状态变化 ,详情参考 https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/connectionState  
        console.log('桌面当前状态==>', state)
      })

      
    });
      
      
    },
    startPlayCamera(){
        this.player1 = new ZLMRTCClient.Endpoint({
            element: document.getElementById('cameravideo'), // video 标签
            debug: false, // 是否打印日志
            zlmsdpUrl: "https://zlm.com/index/api/webrtc?app=live&stream=test1&type=push", //流地址
            simulcast: false,
            useCamera: this.useCamera,
            audioEnable: false,
            videoEnable: this.useCamera,
            recvOnly: this.recvOnly,
            resolution: { w: this.w, h: this.h },
            usedatachannel: false
            })
            return new Promise((resolve) => {
        this.player1.on(ZLMRTCClient.Events.WEBRTC_ON_LOCAL_STREAM,function(s){
                // 获取到了本地流 
                document.getElementById('cameraVideo').srcObject=s;
                document.getElementById('cameraVideo').muted = true;
                resolve();
    });
        
        
        this.player1.on(ZLMRTCClient.Events.WEBRTC_ICE_CANDIDATE_ERROR, function (e) {
            // ICE 协商出错
            console.log('ICE 协商出错')
        })

        this.player1.on(ZLMRTCClient.Events.WEBRTC_OFFER_ANWSER_EXCHANGE_FAILED, function (e) {
            // offer anwser 交换失败
            console.log('offer anwser 交换失败', e)
            stop()
        })

        this.player1.on(ZLMRTCClient.Events.CAPTURE_STREAM_FAILED, function (s) {
            // 获取本地流失败
            console.log('获取本地流失败')
            resolve()
        })

        this.player1.on(ZLMRTCClient.Events.WEBRTC_ON_CONNECTION_STATE_CHANGE, function (state) {
            // RTC 状态变化 ,详情参考 https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/connectionState  
            console.log('摄像头当前状态==>', state)
        })
    });
    },
    startPlayMIC(){
        this.player2 = new ZLMRTCClient.Endpoint({
            element: '', // video 标签
            debug: false, // 是否打印日志
            zlmsdpUrl: "https://zlm.com/index/api/webrtc?app=live&stream=test2&type=push", //流地址
            simulcast: false,
            useCamera: false,
            audioEnable: this.audioEnable,
            videoEnable: false,
            recvOnly: false,
            resolution: { w: this.w, h: this.h },
            usedatachannel: false
            })
        return new Promise((resolve, reject) => {
            this.player2.on(ZLMRTCClient.Events.WEBRTC_ON_LOCAL_STREAM,function(s){
                    // 获取到了本地流 
                    resolve();
             });
        
        this.player2.on(ZLMRTCClient.Events.WEBRTC_ICE_CANDIDATE_ERROR, function (e) {
            // ICE 协商出错
            console.log('ICE 协商出错')
        })

        this.player2.on(ZLMRTCClient.Events.WEBRTC_ON_REMOTE_STREAMS, function (e) {
            //获取到了远端流，可以播放
            console.log('播放成功', e.streams)
        })

        this.player2.on(ZLMRTCClient.Events.WEBRTC_OFFER_ANWSER_EXCHANGE_FAILED, function (e) {
            // offer anwser 交换失败
            console.log('offer anwser 交换失败', e)
            stop()
        })

        this.player2.on(ZLMRTCClient.Events.CAPTURE_STREAM_FAILED, function (s) {
            // 获取本地流失败
            console.log('获取本地流失败')
        })

        this.player2.on(ZLMRTCClient.Events.WEBRTC_ON_CONNECTION_STATE_CHANGE, function (state) {
            // RTC 状态变化 ,详情参考 https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/connectionState  
            console.log('麦克风当前状态==>', state)
        })
    });
    },
    
    start(){
        // if(! this.useCamera && ! this.usescreen){
        //     this.videoEnable = false
        // }
        // if(this.useCamera && this.usescreen){
        //     this.v1 = false
        //     this.v2 = true
        // }
        // else if(this.useCamera){
        //     this.v1 = true
        //     this.v2 = true
        // }
        // else{
        //     this.v1=false
        //     this.v2=false
        // }
    this.isplaying = true
    console.log(this.isplaying)
    //this.stop()
    this.startPlayMIC()
   
    //   Promise.all([
    //     this.startPlayMIC(),
    //     this.startPlayCamera()
    // ])
     
        
      
    },
    stop(){
      if (this.player) {
        this.player.close()
        this.player= null
        // const remote = document.getElementById('video')
        // if (remote) {
        //   remote.srcObject = null
        //   remote.load()
        // }
      }
      if(this.player1){
            this.player1.close()
            this.player1= null
        }
        if(this.player2){
            this.player2.close()
            this.player2= null
        }
        if(this.pusher1){
            this.pusher1.close()
            this.pusher1= null
        }
        if(this.pusher2){
            this.pusher2.close()
            this.pusher2= null
        }
        this.isplaying = false
        this.useCamera = false
        this.usescreen = false
        setTimeout(() => {
            this.$router.push({ name: 'singleCourse' ,params:{'cid':this.cid}})
        }, 2000);
        
    },
    openMIC(){
        this.audioEnable = true
        this.startPlayMIC()
    },
    closeMIC(){
        this.audioEnable = false
        this.player2.close()
        this.player2 = null
    },
    openCamera(){
        this.useCamera = true
        this.startPlayCamera()
        
    },
    closeCamera(){
        this.useCamera = false
        this.player1.close()
        this.player1 = null
       
    },
    openScreen(){
       
        this.usescreen = true
        this.startPlay()
    },
    closeScreen(){
        this.usescreen = false;
        this.player.close()
        this.player = null
    },
    PlayStudentCamera(){
        this.pusher1 = new ZLMRTCClient.Endpoint({
            element: document.getElementById('studentVideo'), // video 标签
            debug: false, // 是否打印日志
            zlmsdpUrl: "https://zlm.com/index/api/webrtc?app=live&stream=studentCamera&type=play", //流地址
            simulcast: false,
            useCamera: false,
            audioEnable: true,
            videoEnable: true,
            recvOnly: true,
            resolution: { w: this.w, h: this.h },
            usedatachannel: false
            })
        
        this.pusher1.on(ZLMRTCClient.Events.WEBRTC_OFFER_ANWSER_EXCHANGE_FAILED, (e) =>{
            // offer anwser 交换失败
            console.log('offer anwser 交换失败', e)
            //this.stop()
            this.PlayStudentCamera()
        })
        this.pusher1.on(ZLMRTCClient.Events.WEBRTC_ON_CONNECTION_STATE_CHANGE, (state) =>{
       
        if(state == 'connected' || state == 'connecting'){
            this.have2 = true
        }
        else if(state== 'failed'){
            this.have2 = false
            this.PlayStudentCamera()
        }
        
        console.log('学生摄像头当前状态==>', state)
      })
    },
    agreehand(){
        this.agree = true
        this.PlayStudentCamera()
        this.PlayStudentMIC()
    },
    PlayStudentMIC(){
        this.pusher2 = new ZLMRTCClient.Endpoint({
            element: document.getElementById('studentAudio'), // video 标签
            debug: false, // 是否打印日志
            zlmsdpUrl: "https://zlm.com/index/api/webrtc?app=live&stream=studentMIC&type=play", //流地址
            simulcast: false,
            useCamera: false,
            audioEnable: true,
            videoEnable: false,
            recvOnly: true,
            resolution: { w: this.w, h: this.h },
            usedatachannel: false
            })
        
        this.pusher2.on(ZLMRTCClient.Events.WEBRTC_OFFER_ANWSER_EXCHANGE_FAILED, (e) =>{
            // offer anwser 交换失败
            console.log('offer anwser 交换失败', e)
            //this.stop()
            this.PlayStudentMIC()
        })
        this.pusher2.on(ZLMRTCClient.Events.WEBRTC_ON_CONNECTION_STATE_CHANGE, (state) =>{
       
        if(state== 'failed'){
           this.PlayStudentMIC()
        }
        
        console.log('学生麦克风当前状态==>', state)
      })
    },
    
    closeHand(){
        this.agree = false
        if(this.pusher1){
            this.pusher1.close()
            this.pusher1 = null
        }
        if(this.pusher2){
            this.pusher2.close()
            this.pusher2 = null
        }
    },
  },
  mounted: function(){
	this.drawcanvas = document.getElementById('drawBoard')
    this.drawctx = this.drawcanvas.getContext('2d')
	
	this.showcanvas = document.getElementById('showBoard')
    this.showctx = this.showcanvas.getContext('2d')
	this.showcanvas.style.zIndex = "-1"
	this.drawws = new WebSocket("ws://127.0.0.1:8000/"+this.username+"/canvas"+this.cid+"/")
	this.draw = new canvasDraw("drawBoard",this.ws);
	this.draw.draw();
	this.drawws.onmessage = (event) => {
		const data = JSON.parse(event.data);
		if (data['kind'] == 'history'){
			for(let i = 0; i < data['message'].length;i++){
				this.msg = data['message'][i]['message']
				this.drawctx.strokeStyle = this.msg[6]
				this.drawctx.fillStyle  = this.msg[7]
				this.drawctx.lineWidth = this.msg[8]
				this.drawctx.lineCap = this.msg[9]
				this.drawctx.lineJoin = this.msg[10]
				if(this.msg[0] == 'draw' && this.msg[1] == 'round'){
					
					this.drawctx.beginPath()
					this.drawctx.arc(this.msg[2], this.msg[3],this.msg[4],0, Math.PI *2);
					this.drawctx.fill();
					this.drawctx.stroke();
				}
				else if(this.msg[0]=='clear'){
					this.drawctx.clearRect(0,0,this.drawcanvas.width,this.drawcanvas.height);
				}
				else if(this.msg[0] == 'draw' && this.msg[1] == 'rect'){
					this.drawctx.rect(this.msg[2], this.msg[3], this.msg[4], this.msg[5]);
					this.drawctx.fill();
					this.drawctx.stroke();
				}
				else if(this.msg[0] == 'draw' && this.msg[1] == 'line'){
					this.drawctx.beginPath()
					this.drawctx.moveTo(this.msg[2],this.msg[3])
					this.drawctx.lineTo(this.msg[4],this.msg[5])
					this.drawctx.stroke();
				}
				else{
					if(this.msg[0]=="draw"||this.msg[0]=="stop"){
						if(this.isDraw==1&&this.msg[0]!='stop'){
								this.drawctx.beginPath()
								this.drawctx.moveTo(this.msg[1],this.msg[2])
								this.isDraw=0
						}else if(this.isDraw==0&&this.msg[0]=='stop'){
							this.isDraw=1
						}
						this.drawctx.lineTo(this.msg[3],this.msg[4])
						this.drawctx.stroke()
					}
				
				
				}
			}
			this.draw.ctx.strokeStyle = this.drawColor
			this.draw.ctx.fillStyle = this.fillColor
			this.draw.ctx.lineCap = this.lineEndType
			this.draw.ctx.lineJoin = this.lineNodeType
			this.draw.ctx.lineWidth = this.drawLineWidth
			//this.draw.ctx.drawType = this.drawType

		}
		else{
			this.msg = data['message']['message']
			if(data['message']['username']!=this.username){
				if(this.msg[0]=='clear'){
					this.drawctx.clearRect(0,0,this.drawcanvas.width,this.drawcanvas.height);
					this.showctx.clearRect(0,0,this.showcanvas.width,this.showcanvas.height);
				}
				else{
					this.mydraw(this.msg,this.showctx)
				}
				
			}
		}
		
	};
  },
  watch:{
	drawColor:{
		handler(newval,oldval){
			this.draw.changeColor(newval)
		}
	},
	fillColor:{
		handler(newval,oldval){
			this.draw.changeFillColor(newval)
		}
	},
	//   drawColor(){
	// 	  this.draw.changeColor(this.drawColor);
	//   },
	  drawLineWidth(){
		  this.draw.changeLineWidth(this.drawLineWidth)
	  },
	//   fillColor(){
	// 	  this.draw.changeFillColor(this.fillColor)
	//   },
	  drawType(){
		  if(this.drawType=='直线'){
			  this.draw.drawLine();
		  }else if(this.drawType=='矩形'){
			  this.draw.drawRect();
		  }else if(this.drawType=='圆'){
			  this.draw.drawRound();
		  }else{
			  this.draw.draw();
		  }
	  },
	  lineEndType(){
		  let lineEndType={
			  '默认': 'butt',
			  '半圆': 'round',
			  '矩形': 'square'
		  }
		  this.draw.changeLineEnd(lineEndType[this.lineEndType]);
	  },
	  lineNodeType(){
		  let lineNodeType={
			  '默认': 'miter',
			  '半圆': 'round',
			  '斜角': 'bevel'
		  }
		  this.draw.changeLineNode(lineNodeType[this.lineNodeType]);
	  }
  },


}
</script>


<style scoped>
input{
  width: 600px;
}
#rside{
    background-color: rgb(213, 218, 218);
    height: 720px;
}
.mainVideo{
    height:720px;
    
}
#selfVideo{
    height: 100%;
}
#studentVideo{
    text-align:right;
    width:100%; 
    height:25%;
}
</style>
