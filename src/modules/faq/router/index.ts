export default [
  {
    path: "/faq",
    name: "faq",
    redirect: { name: "FaqMain" },
    component: () => import(/* webpackChunkName: "FaqMain" */ "@/modules/faq/views/Main.vue"),
    children: [
      {
        path: "main",
        name: "FaqMain",
        component: () => import(/* webpackChunkName: "FaqMain" */ "@/modules/faq/views/Main.vue"),
      },
    ],
  },
  {
    path: "/faq/norm-portion",
    name: "FaqNormPortion",
    component: () => import(/* webpackChunkName: "FaqNormPortion" */ "@/modules/faq/views/NormPortion.vue"),
  },
  {
    path: "/faq/gesund",
    name: "FaqGesund",
    component: () => import(/* webpackChunkName: "FaqGesund" */ "@/modules/faq/views/Gesund.vue"),
  },
];
