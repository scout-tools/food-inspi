export default [
  {
    path: "/",
    name: "home",
    redirect: { name: "SimulatorStart" },
    component: () => import(/* webpackChunkName: "RecipesMain" */ "@/modules/recipe/views/Main.vue")
  },
  {
    path: '/404',
    name: 'PageNotExist',
    component: () => import('@/modules/app/views/PageNotFound.vue'),
  },
  {
    path: "/:catchAll(.*)", // Unrecognized path automatically matches 404
    redirect: '/404',
  },
];
