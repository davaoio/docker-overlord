import Vue from 'vue'
import Vuex from 'vuex'
import axios from "axios";

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    jwt: false,    
    userDetails: false,
    admin: false,
  },
  mutations: {
    JWT_SET(state, jwt) {
      state.jwt = jwt;
    },
    USER_DETAILS_SET(state, details) {
      state.userDetails = details;
    },
    ADMIN_SET(state, admin) {
      state.admin = admin;
    }
  },
  actions: {
    jwtSet({commit}, jwt) {
      axios.defaults.headers.common['Authorization'] = jwt;
      commit('JWT_SET', jwt);
    },
    userDetails({commit}, details) {
      commit('USER_DETAILS_SET', details)
    },
    admin({commit}, admin) {
      commit('ADMIN_SET', admin)
    },
  },
  getters: {
    loggedIn: state => state.jwt,
    userDetails: state => state.userDetails,
    admin: state => state.admin,
  }
})
