export default [
  {
    path: "/event/start",
    name: "MealDayStart",
    redirect: { name: "MyEvents", query: { meal_type: 'lunch_warm'}},
    component: () => import(/* webpackChunkName: "MealDayStart" */ "@/modules/meal/views/MealDayStart.vue"),
    children: [
      {
        path: "my-events",
        name: "MyEvents",
        component: () =>
          import(/* webpackChunkName: "MyEvents" */ "@/modules/meal/views/tabs/MyEvents.vue"),
      },
      {
        path: "public-events",
        name: "PublicEvents",
        component: () =>
          import(/* webpackChunkName: "PublicEvents" */ "@/modules/meal/views/tabs/PublicEvents.vue"),
      },
      {
        path: "my-recipes",
        name: "ApprovedEvents",
        component: () =>
          import(/* webpackChunkName: "ApprovedEvents" */ "@/modules/meal/views/tabs/ApprovedEvents.vue"),
      },
    ],
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
