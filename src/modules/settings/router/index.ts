export default [
  {
    path: "/settings",
    name: "settings",
    redirect: { name: "settingsMain" },
    component: () => import(/* webpackChunkName: "settings" */ "@/modules/settings/views/Main.vue"),
    children: [
      {
        path: "main",
        name: "settingsMain",
        component: () => import(/* webpackChunkName: "settingsMain" */ "@/modules/settings/views/Main.vue"),
      },
    ],
  },
];
