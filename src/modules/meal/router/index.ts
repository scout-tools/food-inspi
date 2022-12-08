export default [
  {
    path: "/event/start",
    name: "MealDayStart",
    component: () => import(/* webpackChunkName: "MealDayStart" */ "@/modules/meal/views/MealDayStart.vue"),
  },
  {
    path: "/event/:id",
    name: "EventMain",
    redirect: { name: "EventDefault", params: { id: 1 } },
    component: () => import(/* webpackChunkName: "EventMain" */ "@/modules/meal/views/EventMain.vue"),
    children: [
      {
        path: "default",
        name: "EventDefault",
        component: () =>
          import(/* webpackChunkName: "EventDefault" */ "@/modules/meal/views/children/Default.vue"),
      },
      {
        path: "shopping-chart",
        name: "EventShoppingCart",
        component: () =>
          import(/* webpackChunkName: "EventShoppingCart" */ "@/modules/meal/views/children/ShoppingCart.vue"),
      },
      {
        path: "day/:eventDayId",
        name: "EventDay",
        component: () =>
          import(/* webpackChunkName: "EventDay" */ "@/modules/meal/views/children/EventDay.vue"),
      },
    ]
  },
];
