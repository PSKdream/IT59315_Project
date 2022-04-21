import Vue from 'vue'
import VueRouter from 'vue-router'
import ColumnarTransposition from '../views/ColumnarTransposition.vue'
import VigenereCipher from '../views/VigenereCipher'
import RailFence from '../views/RailFence'
import RSA from '../views/RSA'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Columnar Transposition',
    component: ColumnarTransposition
  },
  {
    path: '/VigenereCipher',
    name: 'VigenereCipher',
    component: VigenereCipher
  },
  {
    path: '/RailFence',
    name: 'RailFence',
    component: RailFence
  },
  {
    path: '/RSA',
    name: 'RSA',
    component: RSA
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
