import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import './plugins/element.js'
import './assets/css/main.css'
import './assets/css/global.css'
import './assets/css/login.css'
import moment from 'moment'//导入文件
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

Vue.prototype.$moment = moment;//赋值使用
Vue.use(ElementUI)
// Vue.config.productionTip = false
axios.defaults.baseURL = 'http://127.0.0.1:8000'
Vue.prototype.$http  = axios
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
