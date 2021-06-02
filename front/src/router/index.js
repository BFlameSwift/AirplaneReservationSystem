import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../components/Login.vue'
import main from '../components/main.vue'
import Register from '../components/Register.vue'
import Personal from '../components/Personal.vue'
import HelloWorld from '../components/HelloWorld.vue'
// import {process} from "vue-jest";
// import {process} from "vue-jest";
Vue.use(VueRouter)
// Vue.use(VueMeta)
const routes = [
  { path: '/', redirect: '/main'},
  { path: '/HelloWorld/', component: HelloWorld},
  { path: '/main/', component: main},
  { path: '/login/', component: Login},
  { path: '/register/', component: Register},
  { path: '/personal/', component: Personal}
]

// process.env.BASE_URL = '127.0.0.1:8000';
const router = new VueRouter({
  // mode: 'history',
  mode:'hash',
  base: process.env.BASE_URL,
  routes
})
// const  router = new Router({
//   base: '/',
//   mode: 'hash',
//   routes: ROUTES
// })

export default router
