<template>
  <div class="flex h-full">
    <LeftNav><router-view /></LeftNav>
  </div>
</template>

<script setup>
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
} from "@heroicons/vue/24/outline";

import { ref } from "vue";
import { useRoute } from "vue-router";

import LeftNav from "@/modules/nav/components/LeftNav.vue";

const route = useRoute();

const sidebarOpen = ref(false);

const currentRoute = computed(() => {
  return route.name;
});

const navigation = [
  {
    name: "Dashboard",
    linkName: "dashboardMain",
    icon: HomeIcon,
  },
  {
    name: "Rezept",
    linkName: "recipeMain",
    icon: Bars3Icon,
  },
  {
    name: "Zutaten",
    linkName: "ingredientNutrients",
    icon: MagnifyingGlassCircleIcon,
  },
];

const secondaryNavigation = [
  {
    name: "Hintergründe",
    linkName: "faqMain",
    icon: MagnifyingGlassCircleIcon,
  },
  { name: "Einstellungen", linkName: "settingsMain", icon: CogIcon },
];
</script>