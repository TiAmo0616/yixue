<template>
    <div>
        <!-- 导航栏 -->
        <div>
            <Daohanglan :isLoggedIn="isLoggedIn" :username="username"></Daohanglan>
        </div>
        <!-- 统计情况 -->
        <div>
            已交{{ this.al }}份
            未交{{ this.noal }}份
        </div>
        <!-- 展示已经交的作业 -->
        <div>
            <el-row v-for="work in works" :key="work.name">
               
                {{ work.name }}
                
               提交时间{{ work.t}}
               <button @click="see(work.wid)">查看</button>
            </el-row>
        </div>
    </div>

</template>

<script>
import axios from 'axios'
import Daohanglan from './daohanglan.vue';
export default {
  name: 'totalAnswer',
  props: ['cid','wid'],
  components:{
    Daohanglan,
  },
  computed: {
    isLoggedIn() {
      return this.$store.state.isLoggedIn;
        },
    username() {
      return this.$store.state.username;
    },
    role() {
      return this.$store.state.role;
    },
},
  data () {
    return {
      works:[],
      al:'',
      noal:'',
    }
  },
  created(){
    axios.post("http://127.0.0.1:8000/showtotalans/",{'wid':this.wid},{
      headers: {
        'Content-Type': 'multipart/form-data'
      }
  })
      .then(response =>{
        console.log(response.data)
        if(response.data.status == 'success'){
          this.works = response.data.res
          this.al = response.data.al
          this.noal = response.data.noal
        }
         
      })
      .catch(error => {
        console.error('Error:', error);
      });
  },
  methods:{

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
