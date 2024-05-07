<template>
    <div class="play-content">

       <el-row>
            <el-col :span="16">
                <div>
                    <video id='selfVideo' controls autoplay style="text-align:right;" width="80%">
                        Your browser is too old which doesn't support HTML5 video.
                    </video>   
                    </div>

                    <div>
                        <p>
                            <label for="streamUrl">url:</label>
                            <input type="text" v-model="streamUrl" id="streamUrl"/>
                        </p>
                        <el-checkbox v-model="useCamera">摄像头</el-checkbox>
                        <el-checkbox v-model="audioEnable">麦克风</el-checkbox>
                        <el-checkbox v-model="usescreen">屏幕共享</el-checkbox>
                        <button @click="start">开启直播</button>
                        <button @click="stop()">停止(stop)</button>
                    </div>
            </el-col>
            <el-col :span="6">
                <div>
                    <video id='selfVideo' controls autoplay style="text-align:right;" width="80%">
                        Your browser is too old which doesn't support HTML5 video.
                    </video>   
                </div>
            </el-col>
       </el-row>
    

    


    
  </div>
</template>

<script>
import ZLMRTCClient from '../utils/ZLMRTCClient';
export default {
  name: 'zhibodemo',
  data () {
    return {
        streamUrl:'',
        h:720,
        w:1280,
        player:null,
        recvOnl:false,
        resArr:[],
        playUrl:'',
        useCamera:false,
        audioEnable:false,
        videoEnable:true,
        recvOnly:false,
        usescreen:false,

    }
  },
  methods:{
    startPlay () {
     
      this.player = new ZLMRTCClient.Endpoint({
        element: document.getElementById('video'), // video 标签
        debug: true, // 是否打印日志
        zlmsdpUrl: document.getElementById('streamUrl').value, //流地址
        simulcast: false,
        useCamera: this.useCamera,
        audioEnable: this.audioEnable,
        videoEnable: this.videoEnable,
        recvOnly: this.recvOnly,
        resolution: { w: this.w, h: this.h },
        usedatachannel: false
      })
      
      this.player.on(ZLMRTCClient.Events.WEBRTC_ON_LOCAL_STREAM,function(s){
              // 获取到了本地流 
              document.getElementById('selfVideo').srcObject=s;
              document.getElementById('selfVideo').muted = true;
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

      this.player.value.on(ZLMRTCClient.Events.CAPTURE_STREAM_FAILED, function (s) {
        // 获取本地流失败
        console.log('获取本地流失败')
      })

      this.player.value.on(ZLMRTCClient.Events.WEBRTC_ON_CONNECTION_STATE_CHANGE, function (state) {
        // RTC 状态变化 ,详情参考 https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/connectionState  
        console.log('当前状态==>', state)
      })

      this.player.value.on(ZLMRTCClient.Events.WEBRTC_ON_DATA_CHANNEL_OPEN, function (event) {
        console.log('rtc datachannel 打开 :', event)
      })

      this.player.value.on(ZLMRTCClient.Events.WEBRTC_ON_DATA_CHANNEL_ERR, function (event) {
        console.log('rtc datachannel 错误 :', event)
      })

      this.player.value.on(ZLMRTCClient.Events.WEBRTC_ON_DATA_CHANNEL_CLOSE, function (event) {
        console.log('rtc datachannel 关闭 :', event)
      })
    },
    start(){
        if(! this.useCamera && ! this.usescreen){
            this.videoEnable = false
        }
      this.stop()
      this.startPlay()
    },
    stop(){
      if (this.player) {
        this.player.close()
        this.player= null
        const remote = document.getElementById('video')
        if (remote) {
          remote.srcObject = null
          remote.load()
        }
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
input{
  width: 600px;
}
</style>
