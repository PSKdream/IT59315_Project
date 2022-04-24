import Vue from 'vue'
import VueRouter from 'vue-router'
import ColumnarTransposition from '../views/ColumnarTransposition.vue'
import VigenereCipher from '../views/VigenereCipher'
import RailFence from '../views/RailFence'
import RSA from '../views/RSA'

Vue.use(VueRouter)

const routes = [{
    path: '/',
    name: 'Columnar Transposition',
    component: ColumnarTransposition
  },
  {
    path: '/app',
    name: 'Columnar Transposition',
    component: ColumnarTransposition
  },
  {
    path: '/app/ColumnarTransposition',
    name: 'Columnar Transposition',
    component: ColumnarTransposition
  },
  {
    path: '/app/VigenereCipher',
    name: 'VigenereCipher',
    component: VigenereCipher
  },
  {
    path: '/app/RailFence',
    name: 'RailFence',
    component: RailFence
  },
  {
    path: '/app/RSA',
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
