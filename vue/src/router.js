import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import Admin from '@/views/Admin.vue'
import Login from '@/views/Login.vue'

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/admin',
    name: 'admin',
    component: Admin
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
]

export default new VueRouter({routes})
