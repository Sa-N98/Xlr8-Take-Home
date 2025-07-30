import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ExperimentView from '../views/ExperimentView.vue'
import DashbordView from '../views/DashbordView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/experiment',
    name: 'experiment',
    component: ExperimentView
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: DashbordView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
