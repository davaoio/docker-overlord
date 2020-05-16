import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import 'bulma/css/bulma.css'
import axios from "axios";
import moment from 'moment';
import { library } from '@fortawesome/fontawesome-svg-core'
import { faUserSecret } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

// See: https://github.com/FortAwesome/vue-fontawesome
library.add(faUserSecret)

Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.prototype.moment = moment;

Vue.config.productionTip = false
Vue.config.devtools = true

if (localStorage.jwt) {
  //console.log(`[main.js] found jwt: ${localStorage.jwt}`); // eslint-disable-line no-console
  axios.defaults.headers.common['Authorization'] = localStorage.jwt;
}

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
