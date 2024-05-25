import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    isLoggedIn: false,
    username:'',
    role:'',
    currentrole:''
  },
  mutations: {
    login(state,username,role,currentrole) {
      state.isLoggedIn = true;
      state.username = username;
      state.role = role
      state.currentrole = currentrole
    },
    logout(state) {
      state.isLoggedIn = false;
      state.username = '';
      state.role = ''
      this.currentrole = ''
    }
  }
});



export default store;