export default [
  {
    path: "/recipe",
    name: "recipe",
    redirect: { name: "recipeMain" },
    component: () => import(/* webpackChunkName: "recipe" */ "@/modules/recipe/views/Main.vue"),
    children: [
      {
        path: "main",
        name: "recipeMain",
        component: () => import(/* webpackChunkName: "recipeMain" */ "@/modules/recipe/views/Main.vue"),
      },
    ],
  },
];
