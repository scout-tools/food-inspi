<template>
  <div>
    <Breadcrumbs :pages="pages" />
    <div
      v-if="!isShoppingRoute"
      class="
        mx-8
        my-4
        border-b border-gray-200
        pb-5
        sm:flex sm:items-center sm:justify-between
      "
    >
      <div class="pb-5">
        <h3 class="text-sm font-medium leading-6 text-gray-900">
          {{ props.event.name }}
        </h3>
        <p class="mt-2 max-w-4xl text-sm text-gray-500">
          Für {{ props.event.normPortions }} Normpersonen
        </p>
      </div>
      <div v-if="!isShoppingRoute" class="mt-3 flex sm:mt-0 sm:ml-4">
          <router-link

            class="text-sm font-medium text-gray-500 hover:text-gray-700"
            :to="{ name: 'EventShoppingCart' }"
          >
        <button
          type="button"
          class="
            inline-flex
            items-center
            rounded-md
            border border-gray-300
            bg-white
            px-4
            py-2
            text-sm
            font-medium
            text-gray-700
            shadow-sm
            hover:bg-gray-50
            focus:outline-none
            focus:ring-2
            focus:ring-blue-500
            focus:ring-offset-2
          "
        >
          Einkaufsliste
        </button>
          </router-link>
        <button
          @click="onEditClicked(props.event)"
          type="button"
          class="
            ml-3
            inline-flex
            items-center
            rounded-md
            border border-transparent
            bg-blue-600
            px-4
            py-2
            text-sm
            font-medium
            text-white
            shadow-sm
            hover:bg-blue-700
            focus:outline-none
            focus:ring-2
            focus:ring-blue-500
            focus:ring-offset-2
          "
        >
          Bearbeiten
        </button>
      </div>
    </div>
    <!-- <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div class="min-w-0 flex-1">
          <div
            class="
              mt-1
              flex flex-col
              sm:mt-0 sm:flex-row sm:flex-wrap sm:space-x-8
            "
          >
            <div class="mt-2 flex items-center text-sm text-gray-500">
              <UsersIcon
                class="mr-1.5 h-5 w-5 flex-shrink-0 text-white"
                aria-hidden="true"
              />
              {{ props.event.normPortions }} Normpersonen
            </div>
          </div>
        </div>
        <div class="mt-5 flex">
          <router-link
            class="text-sm font-medium text-gray-500 hover:text-gray-700"
            :to="{ name: 'EventShoppingCart' }"
          >
            <button
              type="button"
              class="
                mx-2
                flex
                h-10
                w-10
                items-center
                justify-center
                rounded-md
                bg-orange-600
                p-2
                text-white
              "
            >
              <span class="sr-only">Einkaufsliste</span>
              <ShoppingCartIcon class="h-6 w-6" aria-hidden="true" />
            </button>
          </router-link>
          <button
            type="button"
            @click="onEditClicked(props.event)"
            class="
              mx-2
              flex
              h-10
              w-10
              items-center
              justify-center
              rounded-md
              bg-blue-600
              p-2
              text-white
            "
          >
            <span class="sr-only">Ändern</span>
            <PencilIcon class="h-6 w-6" aria-hidden="true" />
          </button>
        </div>
      </div> -->

    <main class="pt-8 pb-16">
      <div class="mx-auto max-w-7xl sm:px-6 lg:px-8">
        <div class="px-0">
          <slot />
        </div>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import {
  Disclosure,
  DisclosureButton,
  DisclosurePanel,
  Listbox,
  ListboxButton,
  ListboxLabel,
  ListboxOption,
  ListboxOptions,
  Menu,
  MenuButton,
  MenuItem,
  MenuItems,
} from "@headlessui/vue";
import {
  ArrowLongLeftIcon,
  ArrowLongRightIcon,
  BriefcaseIcon,
  CalendarIcon,
  CheckCircleIcon,
  CheckIcon,
  ChevronDownIcon,
  ChevronRightIcon,
  CurrencyDollarIcon,
  EnvelopeIcon,
  LinkIcon,
  MagnifyingGlassIcon,
  MapPinIcon,
  PencilIcon,
  UsersIcon,
  ShoppingCartIcon,
  HomeIcon,
} from "@heroicons/vue/20/solid";
import { Bars3Icon, BellIcon, XMarkIcon } from "@heroicons/vue/24/outline";
import { ref, watch, onMounted, computed } from "vue";
import { useRoute } from "vue-router";



import Breadcrumbs from "@/components/breadcrumbs/Header.vue";

const getDailyFactor = computed(() => {
  if (props?.event?.mealDays?.length > 0) {
    return props.event.mealDays[0].energyKj / 13125;
  }
  return 0;
});

const emit = defineEmits(["onDeleteClicked", "onEditClicked"]);

function onDeleteClicked() {
  emit("onDeleteClicked");
}

function onEditClicked(items) {
  emit("onEditClicked", items);
}
const route = useRoute();

const isShoppingRoute = computed(() => {
  return route.name === 'EventShoppingCart';
});

const pages = computed(() => {
  console.log({ id: props.event.id });
  return [
    { name: "Alle Veranstaltungen", link: "MealDayStart", current: false },
    {
      name: props.event.name,
      link: "EventDefault",
      params: props.event.params,
      current: false,
    },
  ];
});

const props = defineProps({
  event: { type: Object, required: true },
});
</script>