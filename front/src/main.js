import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import './plugins/element.js'
import './assets/css/main.css'
import './assets/css/global.css'
import './assets/css/login.css'

// Vue.config.productionTip = false
axios.defaults.baseURL = 'http://127.0.0.1:8000'
Vue.prototype.$http  = axios
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
