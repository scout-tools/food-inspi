export default [
  {
    path: "/settings",
    name: "Settings",
    redirect: { name: "SettingsGeneral" },
    meta: {
      requiresAuth: true
    },
    component: () => import(/* webpackChunkName: "Settings" */ "@/modules/settings/views/Main.vue"),
    children: [
      {
        path: "general",
        name: "SettingsGeneral",
        component: () => import(/* webpackChunkName: "SettingsGeneral" */ "@/modules/settings/views/tabs/General.vue"),
      },
      {
        path: "general/edit",
        name: "SettingsGeneralEdit",
        component: () => import(/* webpackChunkName: "SettingsGeneralEdit" */ "@/modules/settings/views/tabs/GeneralEdit.vue"),
      },
      {
        path: "password",
        name: "SettingsPassword",
        component: () => import(/* webpackChunkName: "SettingsPassword" */ "@/modules/settings/views/tabs/Password.vue"),
      },
    ],
  },
];
