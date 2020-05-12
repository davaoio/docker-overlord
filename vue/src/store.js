import Vue from 'vue'
import Vuex from 'vuex'
import axios from "axios";

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    jwt: false,    
    userDetails: false,
  },
  mutations: {
    JWT_SET(state, jwt) {
      state.jwt = jwt;
    },
    USER_DETAILS_SET(state, details) {
      state.userDetails = details;
    }
  },
  actions: {
    jwtSet({commit}, jwt) {
      axios.defaults.headers.common['Authorization'] = jwt;
      commit('JWT_SET', jwt);
    },
    userDetails({commit}, details) {
      commit('USER_DETAILS_SET', details)
    }
  },
  getters: {
    loggedIn: state => state.jwt,
    userDetails: state => state.userDetails,
  }
})
