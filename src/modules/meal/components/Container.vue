<template>
  <div class="h-full">
    <!-- Page heading -->
    <header class="bg-gray-50 py-8">
      <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div class="min-w-0 flex-1">
          <h1
            class="
              mt-2
              text-2xl
              font-bold
              leading-7
              text-gray-900
              sm:truncate sm:text-3xl sm:tracking-tight
            "
          >
            Veranstaltung: {{ props.event.name }}
          </h1>
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
            :to="{ name: 'EventDefault' }"
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
                bg-green-600
                p-2
                text-white
              "
            >
              <span class="sr-only">Home</span>
              <HomeIcon class="h-6 w-6" aria-hidden="true" />
            </button>
          </router-link>
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
      </div>
    </header>

    <main class="pt-8 pb-16">
      <div class="mx-auto max-w-7xl sm:px-6 lg:px-8">
        <div class="px-4 sm:px-0">
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

const props = defineProps({
  event: { type: Object, required: true },
  eventFields: { type: Array, required: true },
});
</script>