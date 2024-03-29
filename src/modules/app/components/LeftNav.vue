<template>
  <TransitionRoot as="template" :show="sidebarOpen">
    <Dialog
      as="div"
      class="relative z-40 lg:hidden"
      @close="sidebarOpen = false"
    >
      <TransitionChild
        as="template"
        enter="transition-opacity ease-linear duration-300"
        enter-from="opacity-0"
        enter-to="opacity-100"
        leave="transition-opacity ease-linear duration-300"
        leave-from="opacity-100"
        leave-to="opacity-0"
      >
        <div class="fixed inset-0 bg-gray-600 bg-opacity-75" />
      </TransitionChild>

      <div class="fixed inset-0 z-40 flex">
        <TransitionChild
          as="template"
          enter="transition ease-in-out duration-300 transform"
          enter-from="-translate-x-full"
          enter-to="translate-x-0"
          leave="transition ease-in-out duration-300 transform"
          leave-from="translate-x-0"
          leave-to="-translate-x-full"
        >
          <DialogPanel
            class="relative flex w-full max-w-xs flex-1 flex-col bg-white focus:outline-none"
          >
            <TransitionChild
              as="template"
              enter="ease-in-out duration-300"
              enter-from="opacity-0"
              enter-to="opacity-100"
              leave="ease-in-out duration-300"
              leave-from="opacity-100"
              leave-to="opacity-0"
            >
              <div class="absolute top-0 right-0 -mr-12 pt-2">
                <button
                  type="button"
                  class="ml-1 flex h-10 w-10 items-center justify-center rounded-full focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white"
                  @click="sidebarOpen = false"
                >
                  <span class="sr-only">Close sidebar</span>
                  <XMarkIcon class="h-6 w-6 text-white" aria-hidden="true" />
                </button>
              </div>
            </TransitionChild>
            <div class="h-0 flex-1 overflow-y-auto pt-5 pb-4">
              <div class="flex flex-shrink-0 items-center px-4">
                <router-link
                  @click="onButtonClicked"
                  :to="{ name: 'SimulatorStart' }"
                >
                  <img
                    class="h-12 w-auto"
                    src="./../assets/logo.png"
                    alt="Food Inspi"
                  />
                </router-link>
              </div>
              <nav aria-label="Sidebar" class="mt-5">
                <div class="space-y-1 px-2">
                  <router-link
                    v-for="item in navigation"
                    :key="item.name"
                    :to="{ name: item.linkName }"
                    @click="onButtonClicked"
                    :class="[
                      item.linkName === currentRoute
                        ? 'bg-gray-100 text-gray-900'
                        : 'text-gray-600 hover:bg-gray-50 hover:text-gray-900',
                      'group flex items-center px-2 py-2 text-base font-medium rounded-md',
                    ]"
                    :aria-current="
                      item.linkName === currentRoute ? 'page' : undefined
                    "
                  >
                    <component
                      :is="item.icon"
                      :class="[
                        item.linkName === currentRoute
                          ? 'text-gray-500'
                          : 'text-gray-400 group-hover:text-gray-500',
                        'mr-4 h-6 w-6',
                      ]"
                      aria-hidden="true"
                    />
                    {{ item.name }}
                  </router-link>
                </div>
                <hr class="my-5 border-t border-gray-200" aria-hidden="true" />
                <div class="px-2">
                  <router-link
                    v-for="item in secondaryNavigation"
                    :key="item.name"
                    :to="{ name: item.linkName }"
                    @click="onButtonClicked"
                    class="group flex items-center rounded-md px-2 py-2 text-base font-medium text-gray-600 hover:bg-gray-50 hover:text-gray-900"
                    :class="[
                      item.linkName === currentRoute
                        ? 'bg-gray-200 text-gray-900'
                        : 'text-gray-600 hover:bg-gray-50 hover:text-gray-900',
                      'group flex items-center px-2 py-2 text-sm font-medium rounded-md',
                    ]"
                    :aria-current="
                      item.linkName === currentRoute ? 'page' : undefined
                    "
                  >
                    <component
                      :is="item.icon"
                      class="mr-4 h-6 w-6 flex-shrink-0 text-gray-400 group-hover:text-gray-500"
                      aria-hidden="true"
                    />
                    {{ item.name }}
                  </router-link>
                  <hr
                    class="my-5 border-t border-gray-200"
                    aria-hidden="true"
                  />
                </div>
              </nav>
            </div>
          </DialogPanel>
        </TransitionChild>
        <div class="w-14 flex-shrink-0" aria-hidden="true">
          <!-- Force sidebar to shrink to fit close icon -->
        </div>
      </div>
    </Dialog>
  </TransitionRoot>

  <!-- Static sidebar for desktop -->
  <div class="hidden lg:flex lg:flex-shrink-0">
    <div class="flex w-64 flex-col">
      <!-- Sidebar component, swap this element with another sidebar if you like -->
      <div
        class="flex min-h-0 flex-1 flex-col border-r border-gray-200 bg-gray-100"
      >
        <div class="flex flex-1 flex-col overflow-y-auto pt-5 pb-4">
          <div class="flex flex-shrink-0 items-center px-4">
            <router-link :to="{ name: 'SimulatorStart' }">
              <img
                class="h-30 w-auto mx-auto"
                src="./../assets/logo.png"
                alt="Food Inspi"
              />
            </router-link>
          </div>
          <nav class="mt-5 flex-1" aria-label="Sidebar">
            <div class="space-y-1 px-2">
              <router-link
                v-for="item in navigation"
                :key="item.name"
                :to="{ name: item.linkName }"
                @click="onButtonClicked"
                :class="[
                  currentRoute.includes(item.route)
                    ? 'bg-gray-200 text-gray-900'
                    : 'text-gray-600 hover:bg-gray-50 hover:text-gray-900',
                  'group flex items-center px-2 py-2 text-sm font-medium rounded-md',
                ]"
                :aria-current="
                  currentRoute.includes(item.route) ? 'page' : undefined
                "
              >
                <component
                  :is="item.icon"
                  :class="[
                    currentRoute.includes(item.route)
                      ? 'text-gray-500'
                      : 'text-gray-400 group-hover:text-gray-500',
                    'mr-3 flex-shrink-0 h-6 w-6',
                  ]"
                  aria-hidden="true"
                />
                {{ item.name }}
              </router-link>
            </div>
            <hr class="my-5 border-t border-gray-200" aria-hidden="true" />
            <div class="flex-1 space-y-1 px-2">
              <router-link
                v-for="item in secondaryNavigation"
                :key="item.name"
                :to="{ name: item.linkName }"
                @click="onButtonClicked"
                class="group flex items-center rounded-md px-2 py-2 text-sm font-medium text-gray-600 hover:bg-gray-50 hover:text-gray-900"
                :class="[
                  currentRoute.includes(item.route)
                    ? 'bg-gray-200 text-gray-900'
                    : 'text-gray-600 hover:bg-gray-50 hover:text-gray-900',
                  'group flex items-center px-2 py-2 text-sm font-medium rounded-md',
                ]"
                :aria-current="
                  currentRoute.includes(item.route) ? 'page' : undefined
                "
              >
                <component
                  :is="item.icon"
                  class="mr-3 h-6 w-6 flex-shrink-0 text-gray-400 group-hover:text-gray-500"
                  aria-hidden="true"
                />
                {{ item.name }}
              </router-link>
              <router-link
                v-if="!isAuth"
                class="group flex items-center rounded-md px-2 py-2 text-sm font-medium text-gray-600 hover:bg-gray-50 hover:text-gray-900"
                :class="[
                  'text-gray-600 hover:bg-gray-50 hover:text-gray-900',
                  'group flex items-center px-2 py-2 text-sm font-medium rounded-md',
                ]"
                :to="{}"
                @click="onLoginClicked"
              >
                <ArrowRightIcon
                  class="mr-4 h-6 w-6 flex-shrink-0 text-gray-400 group-hover:text-gray-500"
                  aria-hidden="true"
                />
                Login
              </router-link>
              <router-link
                v-if="isAuth"
                class="group flex items-center rounded-md px-2 py-2 text-sm font-medium text-gray-600 hover:bg-gray-50 hover:text-gray-900"
                :class="[
                  'text-gray-600 hover:bg-gray-50 hover:text-gray-900',
                  'group flex items-center px-2 py-2 text-sm font-medium rounded-md',
                ]"
                :to="{}"
                @click="onLogoutClicked"
              >
                <ArrowLeftIcon
                  class="mr-4 h-6 w-6 flex-shrink-0 text-gray-400 group-hover:text-gray-500"
                  aria-hidden="true"
                />
                Logout
              </router-link>
            </div>
          </nav>
        </div>
      </div>
    </div>
  </div>
  <div v-bind="$attrs" class="flex min-w-0 flex-1 flex-col overflow-hidden">
    <div class="lg:hidden">
      <div
        class="flex items-center justify-between border-b border-gray-200 bg-gray-50 px-4 py-1.5"
      >
        <router-link :to="{ name: 'SimulatorStart' }">
          <img
            class="h-10 w-auto"
            src="./../assets/inspi_food_kopf.png"
            alt="Food Inspi"
          />
        </router-link>
        <div>
          <button
            type="button"
            class="-mr-3 inline-flex h-12 w-12 items-center justify-center rounded-md text-gray-500 hover:text-gray-900 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-blue-600"
            @click="sidebarOpen = true"
          >
            <span class="sr-only">Open sidebar</span>
            <Bars3Icon class="h-6 w-6" aria-hidden="true" />
          </button>
        </div>
      </div>
    </div>
    <div class="relative z-0 overflow-auto">
      <slot></slot>
    </div>
  </div>
</template>

<script setup lang="ts">
import {
  Dialog,
  DialogPanel,
  Popover,
  PopoverButton,
  PopoverGroup,
  PopoverPanel,
  Tab,
  TabGroup,
  TabList,
  TabPanel,
  TabPanels,
  TransitionChild,
  ComboboxOption,
  Combobox,
  ComboboxLabel,
  ComboboxInput,
  ComboboxOptions,
  ComboboxButton,
  TransitionRoot,
} from "@headlessui/vue";
import {
  Bars3Icon,
  CogIcon,
  HomeIcon,
  MagnifyingGlassCircleIcon,
  XMarkIcon,
  RocketLaunchIcon,
  ScaleIcon,
  ArrowRightIcon,
  CalendarIcon,
  ArrowLeftIcon,
} from "@heroicons/vue/24/outline";

import { ref, computed } from "vue";
import { useRoute } from "vue-router";

import { useAuthStore } from "@/modules/auth/store/index";
const authStore = useAuthStore();

function onLoginClicked() {
  authStore.login();
}
function onLogoutClicked() {
  authStore.logout();
}

function onButtonClicked() {
  sidebarOpen.value = false;
}

const isAuth = computed(() => {
  return authStore.isAuth;
});

const route = useRoute();

const secondaryNavigation = computed(() => {
  return [
    {
      name: "Hintergründe",
      linkName: "FaqMain",
      icon: MagnifyingGlassCircleIcon,
      route: "faq",
      isAuth: false,
    },
    {
      name: "Rezepte",
      linkName: "RecipesMain",
      icon: Bars3Icon,
      route: "recipe",
      isAuth: true,
    },
    {
      name: "Zutaten",
      linkName: "IngredientMain",
      icon: MagnifyingGlassCircleIcon,
      route: "ingredient",
      isAuth: true,
    },
    {
      name: "Regeln",
      linkName: "HintMain",
      icon: ScaleIcon,
      route: "hint",
      isAuth: true,
    },
    // {
    //   name: "Einstellungen",
    //   linkName: "Settings",
    //   route: "settings",
    //   icon: CogIcon,
    //   isAuth: true,
    // },
  ].filter(
    (item) => (!item.isAuth) || (item.isAuth && isAuth.value)
  );
});
const sidebarOpen = ref(false);

const currentRoute = computed(() => {
  return route.fullPath;
});

const navigation = [
  {
    name: "Simulator",
    linkName: "SimulatorStart",
    icon: RocketLaunchIcon,
    route: "simulator",
  },
  {
    name: "Planungen",
    linkName: "MealDayStart",
    icon: CalendarIcon,
    route: "event",
  },
];
</script>

<style>
</style>