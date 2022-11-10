import { createRouter, createWebHistory } from 'vue-router'

import AppRouter from '@/modules/app/router'
import DashboardRouter from '@/modules/dashboard/router'
import SettingsRouter from '@/modules/settings/router'
import AuthRouter from '@/modules/auth/router'

const routes = [
  ...DashboardRouter,
  ...AppRouter,
  ...SettingsRouter,
  ...AuthRouter,
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})



export default router
