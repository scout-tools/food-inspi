<template>
  <div>
    <main class="relative z-40 flex-1 focus:outline-none">
      <!-- Breadcrumb -->
      <nav
        class="z-40 flex items-start px-4 py-3 sm:px-6 lg:px-8"
        aria-label="Breadcrumb"
      >
        <Combobox as="div" v-model="searchValue" @input="updateSearch">
          <ComboboxLabel class="block text-sm font-medium text-gray-700"
            >Wähle eine Zutat</ComboboxLabel
          >
          <div class="relative mt-1">
            <ComboboxInput
              class="
                w-full
                rounded-md
                border border-gray-300
                bg-white
                py-2
                pl-3
                pr-10
                shadow-sm
                focus:border-blue-500
                focus:outline-none
                focus:ring-1
                focus:ring-blue-500
                sm:text-sm
              "
              @change="searchValue = $event.target.value"
              :display-value="(item) => item?.name"
            />
            <ComboboxButton
              class="
                absolute
                inset-y-0
                right-0
                flex
                items-center
                rounded-r-md
                px-2
                focus:outline-none
              "
            >
              <ChevronUpDownIcon
                class="h-5 w-5 text-gray-400"
                aria-hidden="true"
              />
            </ComboboxButton>

            <ComboboxOptions
              class="
                z-10
                mt-1
                max-h-60
                w-full
                overflow-auto
                rounded-md
                bg-white
                py-1
                text-base
                shadow-lg
                ring-1 ring-black ring-opacity-5
                focus:outline-none
                sm:text-sm
              "
            >
              <ComboboxOption
                v-for="person2 in ingredients"
                :key="person2.id"
                :value="person2"
                as="template"
                v-slot="{ active2, selected2 }"
                @click="onIngredientClicked(person2.id)"
              >
                <li
                  :class="[
                    'relative cursor-default select-none py-2 pl-3 pr-9',
                    active2 ? 'bg-blue-600 text-white' : 'text-gray-900',
                  ]"
                >
                  <span
                    :class="['block truncate', selected2 && 'font-semibold']"
                  >
                    {{ person2.name }}
                  </span>

                  <span
                    v-if="selected2"
                    :class="[
                      'absolute inset-y-0 right-0 flex items-center pr-4',
                      active2 ? 'text-white' : 'text-blue-600',
                    ]"
                  >
                    <CheckIcon class="h-5 w-5" aria-hidden="true" />
                  </span>
                </li>
              </ComboboxOption>
            </ComboboxOptions>
          </div>
        </Combobox>
      </nav>

      <article v-if="ingredientDetail.name">

        <!-- Tabs -->
        <TabGroup as="div" class="mt-2">
          <div class="border-b border-gray-200">
            <TabList class="-mb-px flex space-x-8 px-4">
              <Tab
                as="template"
                v-for="category in tabs"
                :key="category.name"
                v-slot="{ selected }"
              >
                <button
                  @click="onTabClicked(category.name)"
                  :class="[
                    selected
                      ? 'text-blue-600 border-blue-600'
                      : 'text-gray-900 border-transparent',
                    'flex-1 whitespace-nowrap border-b-2 py-4 px-1 text-base font-medium',
                  ]"
                >
                  {{ category.name }}
                </button>
              </Tab>
            </TabList>
          </div>
          <TabPanels as="template">
            <Nutrients/>
            <Portions/>
          </TabPanels>
        </TabGroup>
      </article>
      <div class="xl:hidden" v-else>Bitte Wähle eine Zutat</div>
    </main>
  </div>
</template>

<script setup>
import { ref } from "vue";
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
  CalendarIcon,
  CogIcon,
  HomeIcon,
  MagnifyingGlassCircleIcon,
  MapIcon,
  MegaphoneIcon,
  SquaresPlusIcon,
  UserGroupIcon,
  XMarkIcon,
  CheckIcon,
  ChevronUpDownIcon,
} from "@heroicons/vue/24/outline";
import {
  ChevronLeftIcon,
  EnvelopeIcon,
  FunnelIcon,
  MagnifyingGlassIcon,
  PhoneIcon,
} from "@heroicons/vue/20/solid";

import Nutrients from "./tabs/Nutrients.vue"
import Portions from "./tabs/Portions.vue"

const tabs = [
  { name: "Nährwerte", id: 1, current: true, route: 'ingredientNutrients', component: 'Nutrients' },
  { name: "Portionen", id: 2, current: false, route: 'ingredientPortions', component: 'Portions' },
];

import { useRouter } from 'vue-router'


const router = useRouter()


import { onMounted, computed } from "vue";
//import users store
import { useIngredientStore } from "@/modules/ingredient/store/index.ts";
// declare store variable
const ingredientStore = useIngredientStore();

const searchValue = ref();

const ingredients = computed(() => {
  return ingredientStore.ingredients;
});
const ingredientDetail = computed(() => {
  return ingredientStore.ingredientDetail;
});
const portions = computed(() => {
  return ingredientStore.portions;
});
function updateSearch() {
  ingredientStore.fetchIngredients({search: searchValue.value});
}
function onIngredientClicked(id) {
  ingredientStore.fetchIngredientById(id);
  ingredientStore.fetchPortions({ ingredient__id: id });
  router.push({
    name: 'ingredientNutrients',
    params: {
      id,
    }
  })
}
function onTabClicked(selectedName) {
  tabs.forEach((tab) => {
    if (selectedName === tab.name) {
      tab.selected = true
      router.push({
        name: tab.route,
      })
    }
  });
}
onMounted(() => {
  ingredientStore.fetchIngredients();
});
</script>