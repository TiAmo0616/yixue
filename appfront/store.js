import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    isLoggedIn: false,
    username:'',
    role:''
  },
  mutations: {
    login(state,username,role) {
      state.isLoggedIn = true;
      state.username = username;
      state.role = role
    },
    logout(state) {
      state.isLoggedIn = false;
      state.username = '';
      state.role = ''
    }
  }
});



export default store;