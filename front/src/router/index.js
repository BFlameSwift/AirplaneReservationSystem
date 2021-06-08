import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../components/Login.vue'
import main from '../components/main.vue'
import Register from '../components/Register.vue'
import Personal from '../components/Personal.vue'
import HelloWorld from '../components/HelloWorld.vue'
import test from '../components/test.vue'
// import {process} from "vue-jest";
// import {process} from "vue-jest";
Vue.use(VueRouter)
// Vue.use(VueMeta)
const routes = [
  {path: '/', redirect: '/main'},
  {path: '/test/', component: test},
  {path: '/main/', component: main},
  {path: '/login/', component: Login},
  {path: '/register/', component: Register},
  {path: '/personal/', component: Personal},
  {path: '/displayFlight', component: () => import("../views/displayFlight.vue")},
  {path: '/fillOrder', component: () => import("../views/fillOrder.vue")},
  {path: '/afterBuy', component: () => import("../views/afterBuy.vue")},
  {path: '/admin', component: () => import("../views/admin.vue")},
  {path: '/addFlight', component: () => import("../views/addFlight.vue")},
  {path: '/futureFlight', component: () => import("../views/futureFlight.vue")},
  {path: '/historyFlight', component: () => import("../views/historyFlight.vue")},
  {path: '/update', component: () => import("../views/update.vue")}
]

// process.env.BASE_URL = '127.0.0.1:8000';
const router = new VueRouter({
  // mode: 'history',
  mode: 'hash',
  base: process.env.BASE_URL,
  routes
})

//挂载路由导航守卫
router.beforeEach((to, from, next) => {
  if (to.path === '/login') return next();
  if (to.path === '/register') return next();
  if (to.path === '/main') return next();
  if (to.path === '/displayFlight') return next();
  const tokenStr = window.sessionStorage.getItem('token')
  if (!tokenStr) return next('/login')
  if (tokenStr&&to.path === '/register') return next('/personal')
  if (tokenStr&&to.path === '/login') return next('/personal')
  next()
})
export default router
