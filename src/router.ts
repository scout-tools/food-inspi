import { createRouter, createWebHistory } from 'vue-router'

import AppRouter from '@/modules/app/router'
import DashboardRouter from '@/modules/dashboard/router'
import FaqRouter from '@/modules/faq/router'
import HintRouter from '@/modules/hint/router'
import IngredientRouter from '@/modules/ingredient/router'
import RecipeRouter from '@/modules/recipe/router'
import SettingsRouter from '@/modules/settings/router'
import AuthRouter from '@/modules/auth/router'
import SupportMain from '@/modules/support/router'
import MealMain from '@/modules/meal/router'

const routes = [
  ...AppRouter,
  ...DashboardRouter,
  ...FaqRouter,
  ...HintRouter,
  ...IngredientRouter,
  ...RecipeRouter,
  ...SettingsRouter,
  ...AuthRouter,
  ...SupportMain,
  ...MealMain
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})



export default router
