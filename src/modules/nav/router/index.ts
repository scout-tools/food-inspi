export default [
  {
    path: "/",
    name: "home",
    redirect: { name: "dashboardMain" },
    component: () => import(/* webpackChunkName: "dashboard" */ "@/modules/app/AppMain.vue"),
  },
];
