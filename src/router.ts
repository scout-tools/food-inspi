import { createRouter, createWebHistory } from "vue-router";

import { useAuthStore } from "@/modules/auth/store";

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
  scrollBehavior(to, from, savedPosition) {
    return { top: 0 };
  },
});

function sleep(ms: number) {
  // eslint-disable-next-line no-promise-executor-return
  return new Promise((resolve) => setTimeout(resolve, ms));
}

router.beforeEach(async (to, from, next) => {
  const authStore = useAuthStore();
  // if (
  //   to.matched.some((record) => {
  //     record.path.includes("landing");
  //   })
  // ) {
  //   next();
  // }

  while (!authStore.isKeycloakInit) {
    // eslint-disable-next-line no-await-in-loop
    await sleep(100);
  }
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (!authStore.isAuth) {
      authStore.login(true);
    } else {
      next();
    }
  }

  if (to.matched.some((record) => record.meta.hideForAuth)) {
    if (authStore.isAuth && !from.name) {
      next({ path: "/" });
    } else {
      next();
    }
  }

  if (!to.matched.some((record) => record.meta.hideForAuth) && !to.matched.some((record) => record.meta.requiresAuth)) {
    next();
  }
});

export default router;
