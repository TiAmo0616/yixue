<template>
    <div class="shouye">
        <!-- Unnamed (未登录导航栏) -->

      <!-- Unnamed (动态面板) -->
      <div id="u41" class="ax_default">
        <div id="u41_state0" class="panel_state" data-label="State1" style="">
          <div id="u41_state0_content" class="panel_state_content">

            <!-- Unnamed (矩形) -->
            <div id="u42" class="ax_default _形状">
              <div id="u42_div" class=""></div>
              <div id="u42_text" class="text " style="display:none; visibility: hidden">
                <p></p>
              </div>
            </div>

            <!-- Unnamed (文本框) -->
            <div id="u43" class="ax_default text_field">
              <div id="u43_div" class=""></div>
              <input id="u43_input" type="search" value="" class="u43_input"/>
            </div>

            <!-- Unnamed (图片 ) -->
            <div id="u44" class="ax_default image">
              <img id="u44_img" class="img " src="src/assets/shouye/u5.png"/>
              <div id="u44_text" class="text " style="display:none; visibility: hidden">
                <p></p>
              </div>
            </div>

            <!-- Unnamed (形状) -->
            <div id="u45" class="ax_default icon">
              <img id="u45_img" class="img " src="src/assets/shouye/u6.svg"/>
              <div id="u45_text" class="text " style="display:none; visibility: hidden">
                <p></p>
              </div>
            </div>

            <!-- Unnamed (形状) -->
            <div id="u46" class="ax_default icon">
              <img id="u46_img" class="img " src="src/assets/shouye/u7.svg"/>
              <div id="u46_text" class="text " style="display:none; visibility: hidden">
                <p></p>
              </div>
            </div>

            <!-- Unnamed (矩形) -->
            <div id="u47" class="ax_default _三级标题">
              <div id="u47_div" class=""></div>
              <div id="u47_text" class="text ">
                <p><span>我的课堂</span></p>
              </div>
            </div>

            <!-- Unnamed (形状) -->
            <div id="u48" class="ax_default icon">
              <img id="u48_img" class="img " src="src/assets/shouye/u11.svg"/>
              <div id="u48_text" class="text " style="display:none; visibility: hidden">
                <p></p>
              </div>
            </div>

            <!-- Unnamed (矩形) -->
            <div id="u49" class="ax_default _三级标题">
              <div id="u49_div" class=""></div>
              <div id="u49_text" class="text ">
                <p><span>登录|注册</span></p>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div id="u40" style="display:none; visibility:hidden;"></div>

    </div>
  </template>
  
  <script>
  export default {
    name: 'shouye',
    data () {
      return {
        
      }
    }
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  .ax_default {
  font-family:'Arial Normal', 'Arial';
  font-weight:400;
  font-style:normal;
  font-size:13px;
  letter-spacing:normal;
  color:#333333;
  vertical-align:none;
  text-align:center;
  line-height:normal;
  text-transform:none;
}

.text_field {
  color:#000000;
  text-align:left;
}
.text_area {
  color:#000000;
  text-align:left;
}
.droplist {
  color:#000000;
  text-align:left;
}
.list_box {
  color:#000000;
  text-align:left;
}

.form_hint {
  color:#999999;
}


textarea, select, input, button { outline: none; }
.mobileFrameCursor div * {
    cursor: inherit !important;
}

a {
    color: inherit;
}

p {
    margin: 0px;
    text-rendering: optimizeLegibility;
    font-feature-settings: "kern" 1;
    -webkit-font-feature-settings: "kern";
    -moz-font-feature-settings: "kern";
    -moz-font-feature-settings: "kern=1";
    font-kerning: normal;
}

ul {
    margin:0px;
}

iframe {
    background: #FFFFFF;
}

/* to match IE with C, FF */
input {
    padding: 1px 0px 1px 0px;
    box-sizing: border-box;
    -moz-box-sizing: border-box;
}

input[type=text]::-ms-clear {
    width: 0;
    height: 0;
    display: none;
}

textarea {
    margin: 0px;
    box-sizing: border-box;
    -moz-box-sizing: border-box;
}

.focused:focus, .selectedFocused:focus {
    outline: none;
}

div.intcases {
    font-family: arial; 
    font-size: 12px;
    text-align:left; 
    border:1px solid #AAA; 
    background:#FFF none repeat scroll 0% 0%; 
    z-index:9999; 
    visibility:hidden; 
    position:absolute;
    padding: 0px;
    border-radius: 3px;
    white-space: nowrap;
}

div.intcaselink {
    cursor: pointer;
    padding: 3px 8px 3px 8px;
    margin: 5px;
    background:#EEE none repeat scroll 0% 0%; 
    border:1px solid #AAA;
    border-radius: 3px;
}

div.refpageimage {
    position: absolute;
    left: 0px;
    top: 0px;
    font-size: 0px;
    width: 16px;
    height: 16px;
    cursor: pointer;
    /* background-image: url(images/newwindow.gif); */
    background-repeat: no-repeat;
}

div.annnoteimage {
    position: absolute;
    left: 0px;
    top: 0px;
    font-size: 0px;
    /*width: 16px;
    height: 12px;*/
    cursor: help;
    /*background-image: url(images/note.gif);*/
    /*background-repeat: no-repeat;*/
    width: 13px;
    height: 12px;
    padding-top: 1px;
    text-align: center;
    background-color: #138CDD;
    -moz-box-shadow: 1px 1px 3px #aaa;
    -webkit-box-shadow: 1px 1px 3px #aaa;
    box-shadow: 1px 1px 3px #aaa;
}

div.annnoteline {
    display: inline-block;
    width: 9px;
    height: 1px;
    border-bottom: 1px solid white;
    margin-top: 1px;
}

div.annnotelabel {
    /*position: absolute;
    left: 0px;
    top: 0px;*/
    font-family: Helvetica,Arial;
    white-space: nowrap;
    
    padding-top: 1px;
    background-color: #fff849;
    font-size: 10px;
    font-weight: bold;
    line-height: 14px;
    margin-right: 3px;
    padding: 0px 4px;
    color: #000;

    -moz-box-shadow: 1px 1px 3px #aaa;
    -webkit-box-shadow: 1px 1px 3px #aaa;
    box-shadow: 1px 1px 3px #aaa;
}

div.annnote {
    display: flex;
    position: absolute;
    cursor: help;
    line-height: 14px;
}

.annotation {
    font-size: 12px;
    padding-left: 2px;
    margin-bottom: 5px;
}

.annotationName {
    /*font-size: 13px;
    font-weight: bold;
    margin-bottom: 3px;
    white-space: nowrap;*/

    font-family: 'Trebuchet MS';
    font-size: 14px;
    font-weight: bold;
    margin-bottom: 5px;
    white-space: nowrap;
}

.annotationValue {
    font-family: Arial, Helvetica, Sans-Serif;
    font-size: 12px;
    color: #4a4a4a;
    line-height: 21px;
    margin-bottom: 20px;
}

.noteLink {
    text-decoration: inherit;
    color: inherit;
}

.noteLink:hover {
    background-color: white;
}

/* this is a fix for the issue where dialogs jump around and takes the text-align from the body */
.dialogFix {
    position:absolute;
    text-align:left;
    border: 1px solid #8f949a;
}


@keyframes pulsate {
  from {
    box-shadow: 0 0 10px #15d6ba;
  }
  to {
    box-shadow: 0 0 20px #15d6ba;
  }
}

@-webkit-keyframes pulsate {
  from {
    -webkit-box-shadow: 0 0 10px #15d6ba;
    box-shadow: 0 0 10px #15d6ba;
  }
  to {
    -webkit-box-shadow: 0 0 20px #15d6ba;
    box-shadow: 0 0 20px #15d6ba;
  }
}
 
@-moz-keyframes pulsate {
  from {
    -moz-box-shadow: 0 0 10px #15d6ba;
    box-shadow: 0 0 10px #15d6ba;
  }
  to {
    -moz-box-shadow: 0 0 20px #15d6ba;
    box-shadow: 0 0 20px #15d6ba;
  }
}

.legacyPulsateBorder {
    /*border: 5px solid #15d6ba;
    margin: -5px;*/
    -moz-box-shadow: 0 0 10px 3px #15d6ba;
    box-shadow: 0 0 10px 3px #15d6ba;
}

.pulsateBorder {
  animation-name: pulsate;
  animation-timing-function: ease-in-out;
  animation-duration: 0.9s;
  animation-iteration-count: infinite;
  animation-direction: alternate;
  
  -webkit-animation-name: pulsate;
  -webkit-animation-timing-function: ease-in-out;
  -webkit-animation-duration: 0.9s;
  -webkit-animation-iteration-count: infinite;
  -webkit-animation-direction: alternate;

  -moz-animation-name: pulsate;
  -moz-animation-timing-function: ease-in-out;
  -moz-animation-duration: 0.9s;
  -moz-animation-iteration-count: infinite;
  -moz-animation-direction: alternate;
}

.ax_default_hidden, .ax_default_unplaced{
    display: none;
    visibility: hidden;
}

.widgetNoteSelected {
    -moz-box-shadow: 0 0 10px 3px #138CDD;
    box-shadow: 0 0 10px 3px #138CDD;
    /*-moz-box-shadow: 0 0 20px #3915d6;
    box-shadow: 0 0 20px #3915d6;*/
    /*border: 3px solid #3915d6;*/
    /*margin: -3px;*/
}


.singleImg {
    display: none;
    visibility: hidden;
}

#ios-safari {
    overflow: auto;
    -webkit-overflow-scrolling: touch;
}

#ios-safari-html {
    display: block;
    overflow: auto;
    -webkit-overflow-scrolling: touch;
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
}

#ios-safari-fixed {
    position: absolute;
    pointer-events: none;
    width: initial;
}

#ios-safari-fixed div {
    pointer-events: auto;
}
.form_sketch {
  border-color:transparent;
  background-color:transparent;
}
#base {
  position:absolute;
  z-index:0;
}
#u41 {
  position:fixed;
  left:0px;
  top:0px;
}
#u41_state0 {
  position:relative;
  left:0px;
  top:0px;
  width:1920px;
  height:81px;
  background-image:none;
  border:none;
  border-radius:0px;
  -moz-box-shadow:none;
  -webkit-box-shadow:none;
  box-shadow:none;
}
#u41_state0_content {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:1px;
  height:1px;
}
#u42_div {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:1920px;
  height:81px;
  background:inherit;
  background-color:rgba(255, 255, 255, 1);
  border:none;
  border-radius:0px;
  -moz-box-shadow:none;
  -webkit-box-shadow:none;
  box-shadow:none;
}
#u42 {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:1920px;
  height:81px;
  display:flex;
}
#u42 .text {
  position:absolute;
  align-self:center;
  padding:2px 2px 2px 2px;
  box-sizing:border-box;
  width:100%;
}
#u42_text {
  border-width:0px;
  word-wrap:break-word;
  text-transform:none;
  visibility:hidden;
}
#u43_input {
  position:absolute;
  left:0px;
  top:0px;
  width:600px;
  height:50px;
  padding:3px 2px 3px 2px;
  font-family:'Arial Normal', 'Arial';
  font-weight:400;
  font-style:normal;
  font-size:20px;
  letter-spacing:normal;
  color:#000000;
  vertical-align:none;
  text-align:left;
  text-transform:none;
  background-color:transparent;
  border-color:transparent;
}
#u43_input.disabled {
  position:absolute;
  left:0px;
  top:0px;
  width:600px;
  height:50px;
  padding:3px 2px 3px 2px;
  font-family:'Arial Normal', 'Arial';
  font-weight:400;
  font-style:normal;
  font-size:20px;
  letter-spacing:normal;
  color:#000000;
  vertical-align:none;
  text-align:left;
  text-transform:none;
  background-color:transparent;
  border-color:transparent;
}
#u43_div {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:600px;
  height:50px;
  background:inherit;
  background-color:rgba(255, 255, 255, 1);
  box-sizing:border-box;
  border-width:1px;
  border-style:solid;
  border-color:rgba(121, 121, 121, 1);
  border-radius:50px;
  -moz-box-shadow:none;
  -webkit-box-shadow:none;
  box-shadow:none;
  font-size:20px;
}
#u43 {
  border-width:0px;
  position:absolute;
  left:190px;
  top:15px;
  width:600px;
  height:50px;
  display:flex;
  font-size:20px;
}
#u43 .text {
  position:absolute;
  align-self:center;
  padding:2px 2px 2px 2px;
  box-sizing:border-box;
  width:100%;
}
#u43_div.disabled {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:600px;
  height:50px;
  background:inherit;
  background-color:rgba(240, 240, 240, 1);
  box-sizing:border-box;
  border-width:1px;
  border-style:solid;
  border-color:rgba(121, 121, 121, 1);
  border-radius:50px;
  -moz-box-shadow:none;
  -webkit-box-shadow:none;
  box-shadow:none;
  font-size:20px;
}
#u43.disabled {
}
#u44_img {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:101px;
  height:80px;
}
#u44 {
  border-width:0px;
  position:absolute;
  left:41px;
  top:0px;
  width:101px;
  height:80px;
  display:flex;
}
#u44 .text {
  position:absolute;
  align-self:center;
  padding:2px 2px 2px 2px;
  box-sizing:border-box;
  width:100%;
}
#u44_text {
  border-width:0px;
  word-wrap:break-word;
  text-transform:none;
  visibility:hidden;
}
#u45_img {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:35px;
  height:35px;
}
#u45 {
  border-width:0px;
  position:absolute;
  left:826px;
  top:22px;
  width:35px;
  height:35px;
  display:flex;
  color:#808080;
}
#u45 .text {
  position:absolute;
  align-self:center;
  padding:2px 2px 2px 2px;
  box-sizing:border-box;
  width:100%;
}
#u45_text {
  border-width:0px;
  word-wrap:break-word;
  text-transform:none;
  visibility:hidden;
}
#u46_img {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:37px;
  height:35px;
}
#u46 {
  border-width:0px;
  position:absolute;
  left:1710px;
  top:16px;
  width:37px;
  height:35px;
  display:flex;
  font-size:10px;
  color:#808080;
}
#u46 .text {
  position:absolute;
  align-self:center;
  padding:2px 2px 2px 2px;
  box-sizing:border-box;
  width:100%;
}
#u46_text {
  border-width:0px;
  word-wrap:break-word;
  text-transform:none;
  visibility:hidden;
}
#u47_div {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:108px;
  height:21px;
  background:inherit;
  background-color:rgba(255, 255, 255, 0);
  border:none;
  border-radius:0px;
  -moz-box-shadow:none;
  -webkit-box-shadow:none;
  box-shadow:none;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial';
  font-weight:700;
  font-style:normal;
}
#u47 {
  border-width:0px;
  position:absolute;
  left:1693px;
  top:54px;
  width:108px;
  height:21px;
  display:flex;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial';
  font-weight:700;
  font-style:normal;
}
#u47 .text {
  position:absolute;
  align-self:flex-start;
  padding:0px 0px 0px 0px;
  box-sizing:border-box;
  width:100%;
}
#u47_text {
  border-width:0px;
  word-wrap:break-word;
  text-transform:none;
}
#u48_img {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:35px;
  height:35px;
}
#u48 {
  border-width:0px;
  position:absolute;
  left:1825px;
  top:16px;
  width:35px;
  height:35px;
  display:flex;
}
#u48 .text {
  position:absolute;
  align-self:center;
  padding:2px 2px 2px 2px;
  box-sizing:border-box;
  width:100%;
}
#u48_text {
  border-width:0px;
  word-wrap:break-word;
  text-transform:none;
  visibility:hidden;
}
#u49_div {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:88px;
  height:21px;
  background:inherit;
  background-color:rgba(255, 255, 255, 0);
  border:none;
  border-radius:0px;
  -moz-box-shadow:none;
  -webkit-box-shadow:none;
  box-shadow:none;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial';
  font-weight:700;
  font-style:normal;
}
#u49 {
  border-width:0px;
  position:absolute;
  left:1801px;
  top:54px;
  width:88px;
  height:21px;
  display:flex;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial';
  font-weight:700;
  font-style:normal;
}
#u49 .text {
  position:absolute;
  align-self:flex-start;
  padding:0px 0px 0px 0px;
  box-sizing:border-box;
  width:100%;
}
#u49_text {
  border-width:0px;
  word-wrap:break-word;
  text-transform:none;
}
#u50 {
  position:absolute;
  left:0px;
  top:80px;
}
#u50_state0 {
  position:relative;
  left:0px;
  top:0px;
  width:1920px;
  height:439px;
  background-image:none;
  border:none;
  border-radius:0px;
  -moz-box-shadow:none;
  -webkit-box-shadow:none;
  box-shadow:none;
}
#u50_state0_content {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:1px;
  height:1px;
}
#u51 {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:0px;
  height:0px;
}
#u52_img {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:1920px;
  height:438px;
}
#u52 {
  border-width:0px;
  position:absolute;
  left:0px;
  top:1px;
  width:1920px;
  height:438px;
  display:flex;
}
#u52 .text {
  position:absolute;
  align-self:center;
  padding:2px 2px 2px 2px;
  box-sizing:border-box;
  width:100%;
}
#u52_text {
  border-width:0px;
  word-wrap:break-word;
  text-transform:none;
  visibility:hidden;
}
#u53_div {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:1050px;
  height:439px;
  background:inherit;
  background-color:rgba(255, 255, 255, 0.498039215686275);
  border:none;
  border-radius:0px;
  -moz-box-shadow:none;
  -webkit-box-shadow:none;
  box-shadow:none;
}
#u53 {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:1050px;
  height:439px;
  display:flex;
}
#u53 .text {
  position:absolute;
  align-self:center;
  padding:2px 2px 2px 2px;
  box-sizing:border-box;
  width:100%;
}
#u53_text {
  border-width:0px;
  word-wrap:break-word;
  text-transform:none;
  visibility:hidden;
}
#u54_div {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:405px;
  height:58px;
  background:inherit;
  background-color:rgba(255, 255, 255, 0);
  border:none;
  border-radius:0px;
  -moz-box-shadow:none;
  -webkit-box-shadow:none;
  box-shadow:none;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial';
  font-weight:700;
  font-style:normal;
  font-size:50px;
}
#u54 {
  border-width:0px;
  position:absolute;
  left:143px;
  top:81px;
  width:405px;
  height:58px;
  display:flex;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial';
  font-weight:700;
  font-style:normal;
  font-size:50px;
}
#u54 .text {
  position:absolute;
  align-self:flex-start;
  padding:0px 0px 0px 0px;
  box-sizing:border-box;
  width:100%;
}
#u54_text {
  border-width:0px;
  word-wrap:break-word;
  text-transform:none;
}
#u55_div {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:224px;
  height:83px;
  background:inherit;
  background-color:rgba(129, 211, 248, 0.501960784313725);
  box-sizing:border-box;
  border-width:1px;
  border-style:solid;
  border-color:rgba(0, 0, 0, 1);
  border-radius:0px;
  -moz-box-shadow:none;
  -webkit-box-shadow:none;
  box-shadow:none;
  font-size:30px;
}
#u55 {
  border-width:0px;
  position:absolute;
  left:736px;
  top:259px;
  width:224px;
  height:83px;
  display:flex;
  font-size:30px;
}
#u55 .text {
  position:absolute;
  align-self:center;
  padding:2px 2px 2px 2px;
  box-sizing:border-box;
  width:100%;
}
#u55_text {
  border-width:0px;
  word-wrap:break-word;
  text-transform:none;
}
#u56_img {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:19px;
  height:30px;
}
#u56 {
  border-width:0px;
  position:absolute;
  left:20px;
  top:195px;
  width:19px;
  height:30px;
  display:flex;
}
#u56 .text {
  position:absolute;
  align-self:center;
  padding:2px 2px 2px 2px;
  box-sizing:border-box;
  width:100%;
}
#u56_text {
  border-width:0px;
  word-wrap:break-word;
  text-transform:none;
  visibility:hidden;
}
#u57_img {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:19px;
  height:30px;
}
#u57 {
  border-width:0px;
  position:absolute;
  left:1856px;
  top:195px;
  width:19px;
  height:30px;
  display:flex;
}
#u57 .text {
  position:absolute;
  align-self:center;
  padding:2px 2px 2px 2px;
  box-sizing:border-box;
  width:100%;
}
#u57_text {
  border-width:0px;
  word-wrap:break-word;
  text-transform:none;
  visibility:hidden;
}
#u50_state1 {
  position:relative;
  left:0px;
  top:0px;
  width:1920px;
  height:439px;
  background-image:none;
  border:none;
  border-radius:0px;
  -moz-box-shadow:none;
  -webkit-box-shadow:none;
  box-shadow:none;
  visibility:hidden;
}
#u50_state1_content {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:1px;
  height:1px;
}
#u58_img {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:1920px;
  height:438px;
}
#u58 {
  border-width:0px;
  position:absolute;
  left:0px;
  top:1px;
  width:1920px;
  height:438px;
  display:flex;
}
#u58 .text {
  position:absolute;
  align-self:center;
  padding:2px 2px 2px 2px;
  box-sizing:border-box;
  width:100%;
}
#u58_text {
  border-width:0px;
  word-wrap:break-word;
  text-transform:none;
  visibility:hidden;
}
#u59_div {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:1050px;
  height:439px;
  background:inherit;
  background-color:rgba(255, 255, 255, 0.498039215686275);
  border:none;
  border-radius:0px;
  -moz-box-shadow:none;
  -webkit-box-shadow:none;
  box-shadow:none;
}
#u59 {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:1050px;
  height:439px;
  display:flex;
}
#u59 .text {
  position:absolute;
  align-self:center;
  padding:2px 2px 2px 2px;
  box-sizing:border-box;
  width:100%;
}
#u59_text {
  border-width:0px;
  word-wrap:break-word;
  text-transform:none;
  visibility:hidden;
}
#u60_div {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:405px;
  height:58px;
  background:inherit;
  background-color:rgba(255, 255, 255, 0);
  border:none;
  border-radius:0px;
  -moz-box-shadow:none;
  -webkit-box-shadow:none;
  box-shadow:none;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial';
  font-weight:700;
  font-style:normal;
  font-size:50px;
}
#u60 {
  border-width:0px;
  position:absolute;
  left:143px;
  top:81px;
  width:405px;
  height:58px;
  display:flex;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial';
  font-weight:700;
  font-style:normal;
  font-size:50px;
}
#u60 .text {
  position:absolute;
  align-self:flex-start;
  padding:0px 0px 0px 0px;
  box-sizing:border-box;
  width:100%;
}
#u60_text {
  border-width:0px;
  word-wrap:break-word;
  text-transform:none;
}
#u61_div {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:224px;
  height:83px;
  background:inherit;
  background-color:rgba(129, 211, 248, 0.501960784313725);
  box-sizing:border-box;
  border-width:1px;
  border-style:solid;
  border-color:rgba(0, 0, 0, 1);
  border-radius:0px;
  -moz-box-shadow:none;
  -webkit-box-shadow:none;
  box-shadow:none;
  font-size:30px;
}
#u61 {
  border-width:0px;
  position:absolute;
  left:736px;
  top:259px;
  width:224px;
  height:83px;
  display:flex;
  font-size:30px;
}
#u61 .text {
  position:absolute;
  align-self:center;
  padding:2px 2px 2px 2px;
  box-sizing:border-box;
  width:100%;
}
#u61_text {
  border-width:0px;
  word-wrap:break-word;
  text-transform:none;
}
#u62_img {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:19px;
  height:30px;
}
#u62 {
  border-width:0px;
  position:absolute;
  left:20px;
  top:195px;
  width:19px;
  height:30px;
  display:flex;
}
#u62 .text {
  position:absolute;
  align-self:center;
  padding:2px 2px 2px 2px;
  box-sizing:border-box;
  width:100%;
}
#u62_text {
  border-width:0px;
  word-wrap:break-word;
  text-transform:none;
  visibility:hidden;
}
#u63_img {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:19px;
  height:30px;
}
#u63 {
  border-width:0px;
  position:absolute;
  left:1856px;
  top:195px;
  width:19px;
  height:30px;
  display:flex;
}
#u63 .text {
  position:absolute;
  align-self:center;
  padding:2px 2px 2px 2px;
  box-sizing:border-box;
  width:100%;
}
#u63_text {
  border-width:0px;
  word-wrap:break-word;
  text-transform:none;
  visibility:hidden;
}
#u64_div {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:196px;
  height:37px;
  background:inherit;
  background-color:rgba(255, 255, 255, 0);
  border:none;
  border-radius:0px;
  -moz-box-shadow:none;
  -webkit-box-shadow:none;
  box-shadow:none;
}
#u64 {
  border-width:0px;
  position:absolute;
  left:92px;
  top:607px;
  width:196px;
  height:37px;
  display:flex;
}
#u64 .text {
  position:absolute;
  align-self:flex-start;
  padding:0px 0px 0px 0px;
  box-sizing:border-box;
  width:100%;
}
#u64_text {
  border-width:0px;
  word-wrap:break-word;
  text-transform:none;
}
#u65_img {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:254px;
  height:170px;
}
#u65 {
  border-width:0px;
  position:absolute;
  left:190px;
  top:733px;
  width:254px;
  height:170px;
  display:flex;
}
#u65 .text {
  position:absolute;
  align-self:center;
  padding:2px 2px 2px 2px;
  box-sizing:border-box;
  width:100%;
}
#u65_text {
  border-width:0px;
  word-wrap:break-word;
  text-transform:none;
  visibility:hidden;
}
#u66_img {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:272px;
  height:170px;
}
#u66 {
  border-width:0px;
  position:absolute;
  left:824px;
  top:733px;
  width:272px;
  height:170px;
  display:flex;
}
#u66 .text {
  position:absolute;
  align-self:center;
  padding:2px 2px 2px 2px;
  box-sizing:border-box;
  width:100%;
}
#u66_text {
  border-width:0px;
  word-wrap:break-word;
  text-transform:none;
  visibility:hidden;
}
#u67_img {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:272px;
  height:170px;
}
#u67 {
  border-width:0px;
  position:absolute;
  left:1476px;
  top:733px;
  width:272px;
  height:170px;
  display:flex;
}
#u67 .text {
  position:absolute;
  align-self:center;
  padding:2px 2px 2px 2px;
  box-sizing:border-box;
  width:100%;
}
#u67_text {
  border-width:0px;
  word-wrap:break-word;
  text-transform:none;
  visibility:hidden;
}
#u68_div {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:136px;
  height:28px;
  background:inherit;
  background-color:rgba(255, 255, 255, 0);
  border:none;
  border-radius:0px;
  -moz-box-shadow:none;
  -webkit-box-shadow:none;
  box-shadow:none;
}
#u68 {
  border-width:0px;
  position:absolute;
  left:914px;
  top:940px;
  width:136px;
  height:28px;
  display:flex;
}
#u68 .text {
  position:absolute;
  align-self:flex-start;
  padding:0px 0px 0px 0px;
  box-sizing:border-box;
  width:100%;
}
#u68_text {
  border-width:0px;
  word-wrap:break-word;
  text-transform:none;
}
#u69_div {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:174px;
  height:28px;
  background:inherit;
  background-color:rgba(255, 255, 255, 0);
  border:none;
  border-radius:0px;
  -moz-box-shadow:none;
  -webkit-box-shadow:none;
  box-shadow:none;
}
#u69 {
  border-width:0px;
  position:absolute;
  left:230px;
  top:940px;
  width:174px;
  height:28px;
  display:flex;
}
#u69 .text {
  position:absolute;
  align-self:flex-start;
  padding:0px 0px 0px 0px;
  box-sizing:border-box;
  width:100%;
}
#u69_text {
  border-width:0px;
  word-wrap:break-word;
  text-transform:none;
}
#u70_div {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:112px;
  height:28px;
  background:inherit;
  background-color:rgba(255, 255, 255, 0);
  border:none;
  border-radius:0px;
  -moz-box-shadow:none;
  -webkit-box-shadow:none;
  box-shadow:none;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial';
  font-weight:700;
  font-style:normal;
}
#u70 {
  border-width:0px;
  position:absolute;
  left:1556px;
  top:940px;
  width:112px;
  height:28px;
  display:flex;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial';
  font-weight:700;
  font-style:normal;
}
#u70 .text {
  position:absolute;
  align-self:flex-start;
  padding:0px 0px 0px 0px;
  box-sizing:border-box;
  width:100%;
}
#u70_text {
  border-width:0px;
  word-wrap:break-word;
  text-transform:none;
}
#u71_div {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:127px;
  height:30px;
  background:inherit;
  background-color:rgba(255, 255, 255, 0);
  border:none;
  border-radius:0px;
  -moz-box-shadow:none;
  -webkit-box-shadow:none;
  box-shadow:none;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial';
  font-weight:700;
  font-style:normal;
  color:#7F7F7F;
}
#u71 {
  border-width:0px;
  position:absolute;
  left:243px;
  top:985px;
  width:127px;
  height:30px;
  display:flex;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial';
  font-weight:700;
  font-style:normal;
  color:#7F7F7F;
}
#u71 .text {
  position:absolute;
  align-self:flex-start;
  padding:0px 0px 0px 0px;
  box-sizing:border-box;
  width:100%;
}
#u71_text {
  border-width:0px;
  word-wrap:break-word;
  text-transform:none;
}
#u72_div {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:127px;
  height:30px;
  background:inherit;
  background-color:rgba(255, 255, 255, 0);
  border:none;
  border-radius:0px;
  -moz-box-shadow:none;
  -webkit-box-shadow:none;
  box-shadow:none;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial';
  font-weight:700;
  font-style:normal;
  color:#7F7F7F;
}
#u72 {
  border-width:0px;
  position:absolute;
  left:914px;
  top:985px;
  width:127px;
  height:30px;
  display:flex;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial';
  font-weight:700;
  font-style:normal;
  color:#7F7F7F;
}
#u72 .text {
  position:absolute;
  align-self:flex-start;
  padding:0px 0px 0px 0px;
  box-sizing:border-box;
  width:100%;
}
#u72_text {
  border-width:0px;
  word-wrap:break-word;
  text-transform:none;
}
#u73_div {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:127px;
  height:30px;
  background:inherit;
  background-color:rgba(255, 255, 255, 0);
  border:none;
  border-radius:0px;
  -moz-box-shadow:none;
  -webkit-box-shadow:none;
  box-shadow:none;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial';
  font-weight:700;
  font-style:normal;
  color:#7F7F7F;
}
#u73 {
  border-width:0px;
  position:absolute;
  left:1541px;
  top:985px;
  width:127px;
  height:30px;
  display:flex;
  font-family:'Arial Negreta', 'Arial Normal', 'Arial';
  font-weight:700;
  font-style:normal;
  color:#7F7F7F;
}
#u73 .text {
  position:absolute;
  align-self:flex-start;
  padding:0px 0px 0px 0px;
  box-sizing:border-box;
  width:100%;
}
#u73_text {
  border-width:0px;
  word-wrap:break-word;
  text-transform:none;
}
#u74_div {
  border-width:0px;
  position:absolute;
  left:0px;
  top:0px;
  width:361px;
  height:14px;
  background:inherit;
  background-color:rgba(255, 255, 255, 0);
  border:none;
  border-radius:0px;
  -moz-box-shadow:none;
  -webkit-box-shadow:none;
  box-shadow:none;
}
#u74 {
  border-width:0px;
  position:absolute;
  left:780px;
  top:1065px;
  width:361px;
  height:14px;
  display:flex;
}
#u74 .text {
  position:absolute;
  align-self:flex-start;
  padding:0px 0px 0px 0px;
  box-sizing:border-box;
  width:100%;
}
#u74_text {
  border-width:0px;
  word-wrap:break-word;
  text-transform:none;
}

  </style>
  