export default [
  {
    path: "/",
    name: "home",
    redirect: { name: "DashboardMain" },
    component: () => import(/* webpackChunkName: "home" */ "@/modules/dashboard/views/Main.vue"),
  },
];
