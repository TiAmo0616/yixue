<template>
    <div class="play-content">

       <el-row>
            <el-col :span="18">
                <!-- 主要直播界面，屏幕共享 -->
                <div>
                    <div class="mainVideo" v-show="!this.boardShow">
                        <video id='selfVideo' controls autoplay style="text-align:right;" width="100%">
                            Your browser is too old which doesn't support HTML5 video.
                        </video>   
                    </div>
                    <!-- 如果开启白板 -->
                    <div class="drawBoard" v-show="this.boardShow">
                        <el-row>
                            <el-col :span="4">
                                <div class="canvasSetting">
                                    <label><input name="drawType" type="radio" value="画笔" v-model="drawType"/>画笔 </label> 
                                    <br/>
                                    <label><input name="drawType" type="radio" value="直线" v-model="drawType"/>直线 </label> 
                                    <br/>
                                    <label><input name="drawType" type="radio" value="矩形" v-model="drawType"/>矩形 </label> 
                                    <br/>
                                    <label><input name="drawType" type="radio" value="圆" v-model="drawType"/>圆 </label> 
                                    <br/>
                                    填充颜色：
                                    <input type="color" v-model="fillColor"/> 
                                    <br/>
                                    选择颜色：
                                    <input type="color" v-model="drawColor"/> 
                                    <br/>
                                    笔粗细
                                    <input type="range" v-model="drawLineWidth" min="1" max="10" />{{drawLineWidth}}
                                    <br/>
                                    线端点类型
                                    <select v-model="lineEndType">
                                        <option>默认</option>
                                        <option>半圆</option>
                                        <option>矩形</option>
                                    </select>
                                    <br/>
                                    矩形角类型
                                    <select v-model="lineNodeType">
                                        <option>默认</option>
                                        <option>半圆</option>
                                        <option>斜角</option>
                                    </select>

                                </div>
                                <div>
                                    <button class="clearButton" @click="clearDraw()">清空白板</button>
                                </div>
                        
                            </el-col>
                            <el-col :span="14">
                                <div id="board" class="canvas-layers" >
                                    <canvas id="drawBoard"  width="600"  height="300" style="position:absolute; "></canvas>
                                    <canvas id="showBoard"  width="600"  height="300" style="position:absolute;"></canvas>
                                </div>
                        
                            </el-col>
                            
                        </el-row>    
	                </div>
                    <!-- 白板代码结束 -->
                </div>
                
                <!-- 工具栏 -->
                <div>
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
                                <button v-show="!this.boardShow" @click="openBoard">使用白板</button>
                                <button v-show="this.boardShow" @click="closeBoard">关闭白板</button>
                            </el-col>
                            <el-col :span="2">
                                <button @click="dianming">随机点名</button>    
                            </el-col>
                            <el-col :span="2">
                                <button @click="chat">聊天</button>    
                            </el-col>
                            <el-col :span="2">
                                <el-badge :value="this.handsNum" class="item">
                                    <el-button size="small" @click="seeHands">举手</el-button>
                                </el-badge>                     
                            </el-col>
                            <el-col :span="2">
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
                            <img :src="studentImage" width="100%" height="200px">
                        </div>
                        <div>
                            <video v-show="false" id='studentAudio' controls autoplay >
                                Your browser is too old which doesn't support HTML5 video.
                        </video> 
                        </div>
                    </div>
                    <!-- 聊天区域，举手也在这里 -->
                    <div v-show="handShow">
                        <div v-show="!agree">
                            <div  v-for="student in students" :key="student.msg">
                                <el-row>
                                    {{ student.msg }}
                                    <button  @click="agreehand(student)">同意</button>
                                    <button @click="closeHand(student)">取消</button>
                                </el-row>
                            </div> 
                        </div>
                        <div v-show="agree">
                            正在与{{ lianmaistudent }}连麦
                            <button @click="closeHand(lianmaistudent)">关闭</button>
                        </div>
                    </div>
                    <!-- 不举手就默认是聊天 -->
                    <div v-show="!handShow">

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
        boardShow:false,

        dianmingShow:false,
        handsNum:0,
        students:[],
        handShow:false,
        lianmaistudent:'',
        studentImage:'',
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
        this.drawws.send("over,")
        
        axios.post("http://127.0.0.1:8000/endClass/",{'cid':this.cid},{
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    })
        .then(response =>{
            console.log(response.data)
            setTimeout(() => {
                this.$router.push({ name: 'singleCourse' ,params:{'cid':this.cid}})
            }, 2000);
            
        })
        .catch(error => {
            console.error('Error:', error);
        });
        
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
    agreehand(student){
        if(! this.agree){
            this.agree = true
            this.drawws.send("permit,"+student['msg']+","+student['image']+",")
            this.lianmaistudent = student.msg
            this.studentImage = student['image']
            this.handsNum = this.handsNum-1
            this.PlayStudentCamera()
            this.PlayStudentMIC()
        }
        else{
            const h = this.$createElement;
                this.$notify({
                title: '温馨提示',
                message: h('i', { style: 'color: teal'}, '当前有学生正在连麦！')})
        }
        
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
    
    closeHand(student){
        this.agree = false
        this.students.splice(this.students.indexOf(student), 1)
        
        this.have2 = false
        this.drawws.send('refuse,'+student)
        if(this.pusher1){
            this.pusher1.close()
            this.pusher1 = null
        }
        if(this.pusher2){
            this.pusher2.close()
            this.pusher2 = null
        }
    },
    closeBoard(){
        this.boardShow = false
        this.drawws.send("close,")
    },
    openBoard(){
       
        this.boardShow = true
       this.drawws.send("open,")
    },
    clearDraw(){
			this.draw.clearCanvas();
			this.showctx.clearRect(0,0,this.showcanvas.width,this.showcanvas.height);
	},
	mydraw(msg,ctx1){
			ctx1.strokeStyle = msg[6]
			ctx1.fillStyle  = msg[7]
			ctx1.lineWidth = msg[8]
			ctx1.lineCap = msg[9]
			ctx1.lineJoin = msg[10]
			
			if(msg[0] == 'draw' && msg[1] == 'round'){
					
				ctx1.beginPath()
				ctx1.arc(msg[2], msg[3],msg[4],0, Math.PI *2);
				ctx1.fill();
				ctx1.stroke();
				}
			else if(msg[0] == 'draw' && msg[1] == 'rect'){
					ctx1.fillRect(msg[2], msg[3], msg[4],msg[5])
					ctx1.strokeRect(msg[2], msg[3], msg[4],msg[5])
					
				}
			else if(msg[0] == 'draw' && msg[1] == 'line'){
					ctx1.beginPath()
					ctx1.moveTo(msg[2],msg[3])
					ctx1.lineTo(msg[4],msg[5])
					ctx1.stroke();
				}
			else{
				if(msg[0]=="draw"||msg[0]=="stop"){
					if(this.loadDraw==1&&msg[0]!='stop'){
							ctx1.beginPath()
							ctx1.moveTo(msg[1],msg[2])
							this.loadDraw=0
					}else if(this.loadDraw==0&&msg[0]=='stop'){
						this.loadDraw=1
					}
					ctx1.lineTo(msg[3],msg[4])
					ctx1.stroke()
				}
				
				
				}
	},
    dianming(){
        this.drawws.send("dianming,")
    },
    seeHands(){
        this.handShow = true
    },
    chat(){
        this.handShow = false
    }
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
  mounted: function(){
	this.drawcanvas = document.getElementById('drawBoard')
    this.drawctx = this.drawcanvas.getContext('2d')
	
	this.showcanvas = document.getElementById('showBoard')
    this.showctx = this.showcanvas.getContext('2d')
	this.showcanvas.style.zIndex = "-1"
    this.drawws = new WebSocket("ws://127.0.0.1:8000/"+this.uid+"/canvas"+this.cid+"/")
    this.draw = new canvasDraw("drawBoard",this.drawws);
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
        else if(data['kind'] == 'open'){
            this.boardShow = true
        }
        else if(data['kind'] == 'over' || data['kind'] == 'permit' || data['kind'] =='refuse'){
            // do nothing
        }
        else if(data['kind'] == 'dianming'){
            //this.dianmingShow = true
            alert("随机点名选中"+data['msg'])
        }
        else if(data['kind'] == 'hand'){
            this.students.push({'msg':data['msg'],'image':data['image']})
            this.handsNum = this.handsNum+1
            
        }
		else{
			this.msg = data['message']['message']
			if(data['message']['username']!=this.uid){
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

}
class canvasDraw{
	constructor(id,ws){
		this.ws= ws;
		this.canvas = document.getElementById(id);
		this.ctx = this.canvas.getContext('2d')
		this.ctx.drawColor='#000000'
		this.ctx.fillColor = '#000000'
		this.ctx.lineWidth=1
		this.ctx.lineCap='默认'
		this.ctx.lineJoin = '默认'
		this.stage_info = this.canvas.getBoundingClientRect()
		this.path = {
			beginX: 0,
			beginY: 0,
			endX: 0,
			endY: 0
		}
		this.isDraw=false
	}
	changeColor(color){
		this.ctx.strokeStyle = color;
	}
	changeLineWidth(lineWidth){
		this.ctx.lineWidth = lineWidth;
	}
	changeFillColor(color){
		this.ctx.fillStyle = color;
	}
	changeLineEnd(lineEndtype){
		this.ctx.lineCap = lineEndtype;
	}
	changeLineNode(lineNode){
		this.ctx.lineJoin = lineNode;
	}
	drawLine(){
		this.canvas.onmousedown=()=>{
			this.ctx.beginPath()
			this.path.beginX = event.pageX - this.stage_info.left
			this.path.beginY = event.pageY - this.stage_info.top
			this.ctx.moveTo(
				this.path.beginX,
				this.path.beginY
			)
		}
		this.canvas.onmouseup=()=>{
			this.path.endX = event.pageX - this.stage_info.left
			this.path.endY = event.pageY - this.stage_info.top
			this.ctx.lineTo(
				this.path.endX,
				this.path.endY
			)
			this.ctx.stroke();
			this.ws.send(`draw,line,${this.path.beginX},${this.path.beginY},${this.path.endX},${this.path.endY},${this.ctx.strokeStyle},${this.ctx.fillStyle},${this.ctx.lineWidth},${this.ctx.lineCap},${this.ctx.lineJoin}`)
		}
	}
	drawRect(){
		this.canvas.onmousedown=()=>{
			this.ctx.beginPath()
			this.path.beginX = event.pageX - this.stage_info.left
			this.path.beginY = event.pageY - this.stage_info.top
		}
		this.canvas.onmouseup=()=>{
			this.path.endX = event.pageX - this.stage_info.left
			this.path.endY = event.pageY - this.stage_info.top
			this.ctx.rect(this.path.beginX, this.path.beginY, this.path.endX-this.path.beginX, this.path.endY-this.path.beginY);
			this.ctx.fill();
			this.ctx.stroke();
			this.ws.send(`draw,rect,${this.path.beginX},${this.path.beginY},${this.path.endX-this.path.beginX},${this.path.endY-this.path.beginY},${this.ctx.strokeStyle},${this.ctx.fillStyle},${this.ctx.lineWidth},${this.ctx.lineCap},${this.ctx.lineJoin}`)
		}
	}
	drawRound(){
		this.canvas.onmousedown=()=>{
			this.ctx.beginPath()
			this.path.beginX = event.pageX - this.stage_info.left
			this.path.beginY = event.pageY - this.stage_info.top
		}
		this.canvas.onmouseup=()=>{
			this.path.endX = event.pageX - this.stage_info.left
			this.path.endY = event.pageY - this.stage_info.top
			let width = this.path.endX-this.path.beginX;
			let height = this.path.endY-this.path.beginY;
			this.ctx.arc(this.path.beginX+width/2, this.path.beginY+height/2,Math.sqrt(width*width+height*height)/2,0, Math.PI *2);
			this.ctx.fill();
			this.ctx.stroke();
			this.ws.send(`draw,round,${this.path.beginX+width/2},${this.path.beginY+height/2},${Math.sqrt(width*width+height*height)/2},0,${this.ctx.strokeStyle},${this.ctx.fillStyle},${this.ctx.lineWidth},${this.ctx.lineCap},${this.ctx.lineJoin}`)
		}
	}
	draw(){
		let that = this
		this.canvas.onmousedown = () => {
			that.ctx.beginPath()
			that.path.beginX = event.pageX - that.stage_info.left
			that.path.beginY = event.pageY - that.stage_info.top
			that.ctx.moveTo(
				that.path.beginX,
				that.path.beginY
			)
			that.isDraw=true
		}
		this.canvas.onmousemove = () => {
			if(that.isDraw){
				that.drawing(event)
			}
		}
		this.canvas.onmouseup = () => {
			that.isDraw=false
			that.ws.send('stop,')
		}
	}
	drawing(e) {
		this.path.endX = e.pageX - this.stage_info.left
		this.path.endY = e.pageY - this.stage_info.top
		this.ctx.lineTo(
			this.path.endX,
			this.path.endY
		)
		this.ctx.stroke()
		console.log(this.ctx.strokeStyle)
		this.ws.send(`draw,${this.path.beginX},${this.path.beginY},${this.path.endX},${this.path.endY},0,${this.ctx.strokeStyle},${this.ctx.fillStyle},${this.ctx.lineWidth},${this.ctx.lineCap},${this.ctx.lineJoin}`)

	}
	clearCanvas(){
		this.ctx.clearRect(0,0,this.canvas.width,this.canvas.height); 
		this.ws.send('clear,')
	}
}
</script>


<style scoped>
input{
  width: 80px;
}
#rside{
    background-color: rgb(228, 244, 251);
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
/* 白板的CSS */

input[type="range"]{
	width: 45%;
}
#drawBoard { 
	border: 2px solid black; 
    
    /* width:800px;
    height:650px; */
    /* position:absolute; */
	
}
#showBoard{
    border: 2px solid black; 
    width:600;
    height:300;
    /* width:800px;
    height:650px; */
    /* position:absolute; */
}
.clearButton{
	vertical-align: bottom;
}
.clear{
	clear:both;
}

#board{
	position: absolute;
	background: #addcf3;
	
} 

.canvasSetting {
    margin: 10px;
    padding: 0px;
    background-color: #e8f2f8;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    font-family: 'Arial', sans-serif;
    vertical-align:top;
    text-align: left;
    display: inline-block;
  }

  .canvasSetting label {
    display: block;
    margin-bottom: 10px;
    font-weight: bold;
  }

  .canvasSetting input[type="color"],
  .canvasSetting input[type="range"],
  .canvasSetting select {
    margin-top: 5px;
  }

  .clearButton {
    display: inline-block;
    /* margin-top: 20px; */
    padding: 5px;
    background-color: #fc2727;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
    transition: background-color 0.3s ease;
	width:120px
  }

  .clearButton:hover {
    background-color: #e87f79;
  }


 /* Add some spacing between radio buttons */
 .canvasSetting > label:not(:last-child) {
    margin-bottom: 15px;
  }

  /* Style the range input */
  .canvasSetting input[type="range"] {
    -webkit-appearance: none;
    width: 100%;
    height: 10px;
    background: #d3d3d3;
    outline: none;
    opacity: 0.7;
    -webkit-transition: .2s;
    transition: opacity .2s;
  }


</style>
