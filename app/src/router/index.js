import Vue from 'vue'
import VueRouter from 'vue-router'
import ColumnarTransposition from '../views/ColumnarTransposition.vue'
import VigenereCipher from '../views/VigenereCipher'
import UnknownChpher from '../views/UnknownChpher'
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
    path: '/UnknownChpher',
    name: 'UnknownChpher',
    component: UnknownChpher
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
