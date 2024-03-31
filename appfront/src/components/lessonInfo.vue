<template>
<div>

    <p>累计选课:{{ studentsNum }}</p>
    <button @click="choose">选课</button>

</div>
</template>

<script>
import Daohanglan from './daohanglan.vue';
export default {
  name: 'lessonInfo',
  data () {
    return {
      studentsNum:'',
    }
  },
  methods:{
    choose(){
        
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
