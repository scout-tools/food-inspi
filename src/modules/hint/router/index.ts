export default [
  {
    path: "/hint",
    name: "HintMain",
    component: () => import(/* webpackChunkName: "HintMain" */ "@/modules/hint/views/Main.vue"),
  },
  {
    path: "/hint/:id",
    name: "HintDetail",
    component: () => import(/* webpackChunkName: "HintDetail" */ "@/modules/hint/views/HintDetail.vue"),
  },
];
