export default [
  {
    path: "/dashboard",
    name: "dashboard",
    redirect: { name: "dashboardMain" },
    component: () => import(/* webpackChunkName: "dashboard" */ "@/modules/dashboard/views/Main.vue"),
    children: [
      {
        path: "main",
        name: "dashboardMain",
        component: () => import(/* webpackChunkName: "dashboardMain" */ "@/modules/dashboard/views/Main.vue"),
      },
    ],
  },
];
