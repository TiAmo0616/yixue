<template>
    <div class="play-content">
    <div>
      <video id='selfVideo' controls autoplay style="text-align:right;" width="60%">
        Your browser is too old which doesn't support HTML5 video.
      </video>

      
    </div>


    <div>
      <p>
        <label for="streamUrl">url:</label>
        <input
          type="text"
          style="co"
          v-model="playUrl"
          id="streamUrl"
        />
      </p>
      <button @click="start()">开始(start)</button>
      <button @click="stop()">停止(stop)</button>
    </div>
  </div>
</template>

<script>
import ZLMRTCClient from '../utils/ZLMRTCClient';

import {ref}from 'vue'
export default {
  setup() {
    const player = ref(null)
    const recvOnly = ref(false)
    const resArr = ref([])

    const ishttps = 'https:' === document.location.protocol
    const isLocal = 'file:' === document.location.protocol
    let url =""
      document.location.protocol +
      '//' +
      window.location.host +
      '/index/api/webrtc?app=live&stream=test&type=push'
    if (!ishttps && !isLocal) {
      alert(
        '本demo需要在https的网站访问 ,如果你要推流的话(this demo must access in site of https if you want push stream)'
      )
    }
    if (isLocal) {
      url = 'http://127.0.0.1' + '/index/api/webrtc?app=live&stream=test&type=push'
    }
    const playUrl = ref(url)

    const startPlay = () => {
      const h = 720
      const w = 1280

      player.value = new ZLMRTCClient.Endpoint({
        element: document.getElementById('video'), // video 标签
        debug: true, // 是否打印日志
        zlmsdpUrl: document.getElementById('streamUrl').value, //流地址
        simulcast: false,
        useCamera: false,
        audioEnable: true,
        videoEnable: true,
        recvOnly: false,
        resolution: { w: w, h: h },
        usedatachannel: false
      })
      console.log(player.value)
      
      player.value.on(ZLMRTCClient.Events.WEBRTC_ON_LOCAL_STREAM,function(s){
              // 获取到了本地流 
              document.getElementById('selfVideo').srcObject=s;
              document.getElementById('selfVideo').muted = true;
              //console.log('offer anwser 交换失败',e)
      });
      player.value.on(ZLMRTCClient.Events.WEBRTC_ICE_CANDIDATE_ERROR, function (e) {
        // ICE 协商出错
        console.log('ICE 协商出错')
      })

      player.value.on(ZLMRTCClient.Events.WEBRTC_ON_REMOTE_STREAMS, function (e) {
        //获取到了远端流，可以播放
        console.log('播放成功', e.streams)
      })

      player.value.on(ZLMRTCClient.Events.WEBRTC_OFFER_ANWSER_EXCHANGE_FAILED, function (e) {
        // offer anwser 交换失败
        console.log('offer anwser 交换失败', e)
        stop()
      })

      player.value.on(ZLMRTCClient.Events.CAPTURE_STREAM_FAILED, function (s) {
        // 获取本地流失败
        console.log('获取本地流失败')
      })

      player.value.on(ZLMRTCClient.Events.WEBRTC_ON_CONNECTION_STATE_CHANGE, function (state) {
        // RTC 状态变化 ,详情参考 https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/connectionState  
        console.log('当前状态==>', state)
      })

      player.value.on(ZLMRTCClient.Events.WEBRTC_ON_DATA_CHANNEL_OPEN, function (event) {
        console.log('rtc datachannel 打开 :', event)
      })

      player.value.on(ZLMRTCClient.Events.WEBRTC_ON_DATA_CHANNEL_ERR, function (event) {
        console.log('rtc datachannel 错误 :', event)
      })

      player.value.on(ZLMRTCClient.Events.WEBRTC_ON_DATA_CHANNEL_CLOSE, function (event) {
        console.log('rtc datachannel 关闭 :', event)
      })
    }

    const start = () => {
      stop()

      const h = 720
      const w = 1280
      
      if (!recvOnly.value) {
        startPlay()
      } else {
        startPlay()
      }
    }

    const stop = () => {
      if (player.value) {
        player.value.close()
        player.value = null
        const remote = document.getElementById('video')
        if (remote) {
          remote.srcObject = null
          remote.load()
        }
      }
    }

    return {
      player,
      recvOnly,
      resArr,
      playUrl,
      startPlay,
      start,
      stop
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
