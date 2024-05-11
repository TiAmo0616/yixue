<template>
    <div class="play-content">
        <el-row>
            <el-col :span="18">
                <!-- 主要直播界面，屏幕共享，如果不共享就是摄像头画面 -->
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
                    <div class="gjlan">
                        <div>
                            <el-button type="primary" @click="hand">举手</el-button>
                            
                        </div>
                        <div v-if="this.perimit">
                            <button v-show="!this.myMIC" @click="pushMIC">开启麦克风</button>
                            <button v-show="this.myMIC" @click="stoppushMIC">关闭麦克风</button>
                            <button v-show="!this.myCamera" @click="pushCamera">开启摄像头</button>
                            <button v-show="this.myCamera" @click="stopPushCamera">关闭摄像头</button>
                            <button @click="closeHand">关闭举手</button>
                        </div>
                        <button @click="stop()">离开直播</button>
                        <!-- <div v-if="!this.player">
                            <button @click="start">进入直播</button>
                        </div>
                        <div v-else>
                            <div>
                                <button @click="hand">举手</button>
                            </div>
                            <div v-if="this.perimit">
                                <button v-show="!this.myMIC" @click="pushMIC">开启麦克风</button>
                                <button v-show="this.myMIC" @click="stoppushMIC">关闭麦克风</button>
                                <button v-show="!this.myCamera" @click="pushCamera">开启摄像头</button>
                                <button v-show="this.myCamera" @click="stopPushCamera">关闭摄像头</button>
                                <button @click="closeHand">关闭举手</button>
                            </div>
                            <button @click="stop()">离开直播</button>
                        </div> -->
                        
                    </div>
            </el-col>
            <el-col :span="6">
                <!-- 右侧小屏，摄像头画面,如果不开摄像头就是头像 -->
                <div id="rside">
                    <!-- <video id='cameraVideo' controls autoplay >
                            Your browser is too old which doesn't support HTML5 video.
                    </video>  -->
                    <div v-show="this.have1">
                        <video id='cameraVideo' controls autoplay>
                            Your browser is too old which doesn't support HTML5 video.
                        </video>   
                    </div>
                    <div v-show="!this.have1">
                        <!-- <img src="../assets/t.jpeg" width="100%" height="200px"> -->
                        <img :src="image" alt="" width="100%" height="200px"/>
                    </div>
                    <!-- 音频拉流，不显示画面 -->
                    <video v-show="false" id='MICVideo' controls autoplay >
                            Your browser is too old which doesn't support HTML5 video.
                    </video> 
                    <!-- 连麦开启视频 -->
                    <div v-show="this.perimit ||  this.otherHand">
                        <div v-show="this.myCamera">
                            <video id='myVideo' controls autoplay ></video>
                        </div>
                        <div v-show="!this.myCamera">
                            <img :src="myImage"  alt="" width="100%" height="200px">
                        </div>
                        <video v-show="false" id='myMIC' controls autoplay >
                            Your browser is too old which doesn't support HTML5 video.
                        </video> 
                    </div>
                    
                    <!-- 聊天界面 -->
                    <div class="rsidechat">

                    </div>
                    <!-- 发送消息界面 -->
                    <div class="rsidebottom">

                    </div>
                   
                </div>
            </el-col>
       </el-row>
    </div>
</template>

<script>
import ZLMRTCClient from '../utils/ZLMRTCClient';
import axios from 'axios'
export default {
  name: 'studbo',
  props: ['uid','cid','teacherid'],
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
        audioEnable:false,
        videoEnable:true,
        recvOnly:false,
        usescreen:false,
        ishand:false,
        perimit:false,//是否可以连麦
        player2:null,
        have1:false,
        pusher1:null,
        pusher2:null,
        myCamera:false,
        myMIC:false,
        image:'',

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

        player3:null,
        player4:null,
        otherHand:false,
        myImage:'',
    }
  },
  created(){
    console.log(this.teacherid)
    axios.post("http://127.0.0.1:8000/showzhiboInfo/",{'username':this.teacherid,'myName':this.uid},{
      headers: {
        'Content-Type': 'multipart/form-data'
      }
  })
      .then(response =>{
        console.log(response.data)
        this.image = response.data.img
        this.myImage = response.data.myImage
        console.log(this.myImage)
        this.start()
        this.startPlayer3()
        this.startPlayer4()
      })

      .catch(error => {
        
        console.error('Error:', error);
      });
      
  },
  methods:{
    startPlay () {
       
        
        this.player = new ZLMRTCClient.Endpoint({
            element: document.getElementById('selfVideo'), // video 标签
            debug: false, // 是否打印日志
            zlmsdpUrl: "https://zlm.com/index/api/webrtc?app=live&stream=test&type=play", //流地址
            simulcast: false,
            useCamera: false,
            audioEnable: true,
            videoEnable: true,
            recvOnly: true,
            resolution: { w: this.w, h: this.h },
            usedatachannel: false
        })
        this.player.on(ZLMRTCClient.Events.WEBRTC_ICE_CANDIDATE_ERROR, function (e) {
        // ICE 协商出错
        console.log('ICE 协商出错')
      })

      this.player.on(ZLMRTCClient.Events.WEBRTC_ON_REMOTE_STREAMS, function (e) {
        //获取到了远端流，可以播放
        console.log('播放成功', e.streams)
      })

      this.player.on(ZLMRTCClient.Events.WEBRTC_OFFER_ANWSER_EXCHANGE_FAILED,  (e)=> {
        // offer anwser 交换失败
        console.log('offer anwser 交换失败', e)
        //this.stop()
        this.startPlay()
      })

      this.player.on(ZLMRTCClient.Events.CAPTURE_STREAM_FAILED, function (s) {
        // 获取本地流失败
        console.log('获取本地流失败')
      })

      this.player.on(ZLMRTCClient.Events.WEBRTC_ON_CONNECTION_STATE_CHANGE, (state)=> {
        // RTC 状态变化 ,详情参考 https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/connectionState  
        console.log('桌面当前状态==>', state)
       if(state == 'failed'|| state=='disconnected'){
        this.stopdesk()
        this.startPlay()
       }
      })

      this.player.on(ZLMRTCClient.Events.WEBRTC_ON_DATA_CHANNEL_OPEN, function (event) {
        console.log('rtc datachannel 打开 :', event)
      })

      this.player.on(ZLMRTCClient.Events.WEBRTC_ON_DATA_CHANNEL_ERR, function (event) {
        console.log('rtc datachannel 错误 :', event)
      })

      this.player.on(ZLMRTCClient.Events.WEBRTC_ON_DATA_CHANNEL_CLOSE, function (event) {
        console.log('rtc datachannel 关闭 :', event)
      })

      
    
      
      
      
    },
    startPlayer3(){
        this.player3 = new ZLMRTCClient.Endpoint({
            element: document.getElementById('myVideo'), // video 标签
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
        
        this.player3.on(ZLMRTCClient.Events.WEBRTC_OFFER_ANWSER_EXCHANGE_FAILED, (e) =>{
            // offer anwser 交换失败
            console.log('offer anwser 交换失败', e)
            //this.stop()
            this.startPlayer3()
        })
        this.player3.on(ZLMRTCClient.Events.WEBRTC_ON_CONNECTION_STATE_CHANGE, (state) =>{
       
        if(state == 'connected'){
           this.otherHand = true
            this.myCamera = true
        }
        else if(state== 'failed'){
            
            this.myCamera = false
            this.startPlayer3()
        }
        
        console.log('举手学生摄像头当前状态==>', state)
      })
            

    },
    startPlayer4(){
        this.player4 = new ZLMRTCClient.Endpoint({
            element: document.getElementById('myMIC'), // video 标签
            debug: false, // 是否打印日志
            zlmsdpUrl: "https://zlm.com/index/api/webrtc?app=live&stream=studentMIC&type=play", //流地址
            simulcast: false,
            useCamera: false,
            audioEnable: true,
            videoEnable: true,
            recvOnly: true,
            resolution: { w: this.w, h: this.h },
            usedatachannel: false
            })
        
        this.player4.on(ZLMRTCClient.Events.WEBRTC_OFFER_ANWSER_EXCHANGE_FAILED, (e) =>{
            // offer anwser 交换失败
            console.log('offer anwser 交换失败', e)
            //this.stop()
            this.startPlayer4()
        })
        this.player4.on(ZLMRTCClient.Events.WEBRTC_ON_CONNECTION_STATE_CHANGE, (state) =>{
       
        if(state == 'connected' || state == 'connecting'){
            
        }
        else if(state== 'failed'){
           
            this.startPlayer4()
        }
        
        console.log('举手学生麦克风当前状态==>', state)
      })
            

    },
    startPlayCamera(){
        this.player1 = new ZLMRTCClient.Endpoint({
            element: document.getElementById('cameraVideo'), // video 标签
            debug: false, // 是否打印日志
            zlmsdpUrl: "https://zlm.com/index/api/webrtc?app=live&stream=test1&type=play", //流地址
            simulcast: false,
            useCamera: false,
            audioEnable: true,
            videoEnable: true,
            recvOnly: true,
            resolution: { w: this.w, h: this.h },
            usedatachannel: false
            })
        
        this.player1.on(ZLMRTCClient.Events.WEBRTC_OFFER_ANWSER_EXCHANGE_FAILED, (e) =>{
            // offer anwser 交换失败
            console.log('offer anwser 交换失败', e)
            //this.stop()
            this.startPlayCamera()
        })
        this.player1.on(ZLMRTCClient.Events.WEBRTC_ON_CONNECTION_STATE_CHANGE, (state) =>{
       
        if(state == 'connected' || state == 'connecting'){
            this.have1 = true
        }
        else if(state== 'failed'){
            this.have1 = false
            this.startPlayCamera()
        }
        
        console.log('摄像头当前状态==>', state)
      })
            

    },
    startPlayMIC(){
        this.player2 = new ZLMRTCClient.Endpoint({
            element: document.getElementById('MICVideo'), // video 标签
            debug: false, // 是否打印日志
            zlmsdpUrl: "https://zlm.com/index/api/webrtc?app=live&stream=test2&type=play", //流地址
            simulcast: false,
            useCamera: false,
            audioEnable: true,
            videoEnable: false,
            recvOnly: true,
            resolution: { w: this.w, h: this.h },
            usedatachannel: false
            })

        this.player2.on(ZLMRTCClient.Events.WEBRTC_OFFER_ANWSER_EXCHANGE_FAILED, (e) =>{
            // offer anwser 交换失败
            console.log('offer anwser 交换失败', e)
            this.startPlayMIC()
        })
        this.player2.on(ZLMRTCClient.Events.WEBRTC_ON_CONNECTION_STATE_CHANGE, (state) =>{
        if(state== 'failed'){
            this.startPlayMIC()
        }
        
        console.log('麦克风当前状态==>', state)
      })
           
        

    },
    
    start(){       
        this.startPlay(),
        this.startPlayCamera(),
        this.startPlayMIC()
    },
    stopdesk(){
        if (this.player) {
        this.player.close()
        this.player= null
      }
    },
    stop(){
      if (this.player) {
        this.player.close()
        this.player= null
        // const remote = document.getElementById('selfVideo')
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
        this.stopPushCamera()
        this.stoppushMIC()
        setTimeout(() => {
            this.$router.push({ name: 'studentCourse' ,params:{'cid':this.cid}})
        }, 1000);
    },
    hand(){//用websocket去通知教师
        this.ishand = true
        this.drawws.send("hand,"+this.uid+","+this.myImage+",")
        
    },
    pushCamera(){
        this.myCamera = true
        this.pusher1 = new ZLMRTCClient.Endpoint({
            element: '', // video 标签
            debug: false, // 是否打印日志
            zlmsdpUrl: "https://zlm.com/index/api/webrtc?app=live&stream=studentCamera&type=push", //流地址
            simulcast: false,
            useCamera: true,
            audioEnable: false,
            videoEnable: true,
            recvOnly: false,
            resolution: { w: this.w, h: this.h },
            usedatachannel: false
            })
        return new Promise((resolve) => {
        this.pusher1.on(ZLMRTCClient.Events.WEBRTC_ON_LOCAL_STREAM,function(s){
                // 获取到了本地流 
                document.getElementById('myVideo').srcObject=s;
                document.getElementById('myVideo').muted = true;
                resolve();
    });
        
        
        this.pusher1.on(ZLMRTCClient.Events.WEBRTC_ICE_CANDIDATE_ERROR, function (e) {
            // ICE 协商出错
            console.log('ICE 协商出错')
        })

        this.pusher1.on(ZLMRTCClient.Events.WEBRTC_OFFER_ANWSER_EXCHANGE_FAILED, function (e) {
            // offer anwser 交换失败
            console.log('offer anwser 交换失败', e)
            stop()
        })

        this.pusher1.on(ZLMRTCClient.Events.CAPTURE_STREAM_FAILED, function (s) {
            // 获取本地流失败
            console.log('获取本地流失败')
            resolve()
        })

        this.pusher1.on(ZLMRTCClient.Events.WEBRTC_ON_CONNECTION_STATE_CHANGE, function (state) {
            // RTC 状态变化 ,详情参考 https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/connectionState  
            console.log('我的摄像头当前状态==>', state)
        })
    });
    },
    stopPushCamera(){
        if(this.pusher1){
            this.pusher1.close()
            this.pusher1= null
            this.myCamera = false
        }
    },
    stoppushMIC(){
        if(this.pusher2){
            this.pusher2.close()
            this.pusher2= null
            this.myMIC = false
        }
    },
    pushMIC(){
        this.myMIC = true
        this.pusher2 = new ZLMRTCClient.Endpoint({
            element: '', // video 标签
            debug: false, // 是否打印日志
            zlmsdpUrl: "https://zlm.com/index/api/webrtc?app=live&stream=studentMIC&type=push", //流地址
            simulcast: false,
            useCamera: false,
            audioEnable: true,
            videoEnable: false,
            recvOnly: false,
            resolution: { w: this.w, h: this.h },
            usedatachannel: false
            })
        return new Promise((resolve) => {
        this.pusher2.on(ZLMRTCClient.Events.WEBRTC_ON_LOCAL_STREAM,function(s){
                // 获取到了本地流 
                
                resolve();
    });
        
        
        this.pusher2.on(ZLMRTCClient.Events.WEBRTC_ICE_CANDIDATE_ERROR, function (e) {
            // ICE 协商出错
            console.log('ICE 协商出错')
        })

        this.pusher2.on(ZLMRTCClient.Events.WEBRTC_OFFER_ANWSER_EXCHANGE_FAILED, function (e) {
            // offer anwser 交换失败
            console.log('offer anwser 交换失败', e)
            stop()
        })

        this.pusher2.on(ZLMRTCClient.Events.CAPTURE_STREAM_FAILED, function (s) {
            // 获取本地流失败
            console.log('获取本地流失败')
            resolve()
        })

        this.pusher2.on(ZLMRTCClient.Events.WEBRTC_ON_CONNECTION_STATE_CHANGE, function (state) {
            // RTC 状态变化 ,详情参考 https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/connectionState  
            console.log('我的麦克风当前状态==>', state)
        })
    });
    },
    closeHand(){
        this.perimit = false
        this.stopPushCamera()
        this.stoppushMIC()
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
    stopOtherPlay(){
        if(this.player3){
            this.player3.close()
            this.player3= null
        }
        if(this.player4){
            this.player4.close()
            this.player4= null
        }
        this.myCamera = false
        this.myMIC = false
        this.otherHand = false
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
        else if(data['kind'] == 'close'){
            this.boardShow = false
        }
        else if(data['kind'] == 'dianming'){
            //this.dianmingShow = true
            alert("随机点名选中"+data['msg'])
        }
        else if(data['kind'] == 'over'){
            
            this.stop()
            alert("直播已结束！")
            
        }
        else if(data['kind'] == 'hand'){
            // do nothing
        }
        else if(data['kind'] == 'permit'){
            if(data['msg'] == this.uid){
                this.stopOtherPlay()
                this.perimit = true
            }
            else{
                console.log(data)
                this.myImage = data['image']
                this.stopOtherPlay()
                this.otherHand = true
                this.startPlayer3()
                this.startPlayer4()
            }
        }
        else if(data['kind'] == 'refuse'){
            if(data['msg'] == this.uid){
                this.permit = false
                this.closeHand()
                const h = this.$createElement;
                this.$notify({
                title: '消息',
                message: h('i', { style: 'color: teal'}, '您的音视频权限已被教师关闭!')})
            }
            else{
                this.stopOtherPlay()
            }
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

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#selfVideo{
   height:100%;
}
#cameraVideo{
    text-align:right;
    width:100%; 
    height:25%;
}
#myVideo{
    text-align:right;
    width:100%; 
    height:25%;
}

#rside{
    background-color: rgb(213, 218, 218);
    height: 775px;
    border: 3px black solid;
}
.mainVideo{
    height:720px;
    border:3px black solid;
}

.rsidebottom{
    
    background-color: rgb(254, 254, 254);
    height:14%;
    width:100%
}
.rsidechat{
    width:100%;
    height:60%;
}
.gjlan{
    border: 3px black solid;
    height:50px;
    width:100%;
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
    margin: 20px;
    padding: 15px;
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

