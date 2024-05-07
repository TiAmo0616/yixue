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

                    <div class="gjlan">
                       
                        <div v-if="!this.player">
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
                        </div>
                        
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
                        <img src="../assets/t.jpeg" width="100%" height="200px">
                    </div>
                    <!-- 音频拉流，不显示画面 -->
                    <video v-show="false" id='MICVideo' controls autoplay >
                            Your browser is too old which doesn't support HTML5 video.
                    </video> 
                    <!-- 连麦开启视频 -->
                    <div v-show="this.perimit">
                        <div v-show="this.myCamera">
                            <video id='myVideo' controls autoplay ></video>
                        </div>
                        <div v-show="!this.myCamera">
                            <img src="../assets/s.jpg" width="100%" height="200px">
                        </div>
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
export default {
  name: 'studbo',
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

    }
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
        this.stop()
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
    },
    hand(){//用websocket去通知教师
        this.ishand = true
        this.perimit = true
        
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
    }
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
</style>

