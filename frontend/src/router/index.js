import { createRouter, createWebHistory } from 'vue-router'
import DataPage from '../views/DataPage.vue'
import ImagePage from '../views/ImagePage.vue'

const routes = [
  { path: '/', redirect: '/data' },
  { path: '/data', component: DataPage },
  { path: '/images', component: ImagePage }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
