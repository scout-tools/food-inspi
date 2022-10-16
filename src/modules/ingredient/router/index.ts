export default [
  {
    path: "/ingredient/:id",
    name: "ingredientMain",
    redirect: { name: 'ingredientNutrients', params: { id: 1}},
    component: () => import(/* webpackChunkName: "ingredientMain" */ "@/modules/ingredient/views/Main.vue"),
    children: [
      {
        path: "nutrients",
        name: "ingredientNutrients",
        component: () => import(/* webpackChunkName: "ingredientNutrients" */ "@/modules/ingredient/views/tabs/Nutrients.vue"),
      },
      {
        path: "portions",
        name: "ingredientPortions",
        component: () => import(/* webpackChunkName: "ingredientPortions" */ "@/modules/ingredient/views/tabs/Portions.vue"),
      },
    ],
  },
];
