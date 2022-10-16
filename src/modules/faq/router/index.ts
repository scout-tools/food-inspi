export default [
  {
    path: "/faq",
    name: "faq",
    redirect: { name: "faqMain" },
    component: () => import(/* webpackChunkName: "faq" */ "@/modules/faq/views/Main.vue"),
    children: [
      {
        path: "main",
        name: "faqMain",
        component: () => import(/* webpackChunkName: "faqMain" */ "@/modules/faq/views/Main.vue"),
      },
    ],
  },
];
