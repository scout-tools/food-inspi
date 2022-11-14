<template>
  <div>
    <List
      :name="'Hinweise'"
      :items="hints"
      :searchValue="searchValue"
      :sortOptions="sortOptions"
      :filters="filters"
      :buttonList="buttonList"
      mainPageLink="HintMain"
      detailPageLink="HintDetail"
    >
      <template #listitem="{ item }">
        <div class="flex min-w-0 flex-1 items-center">
          <div class="min-w-0 flex-1 px-4 md:grid md:grid-cols-2 md:gap-4">
            <div>
              <p class="truncate text-sm font-medium text-blue-600">
                Hinweis: {{ item.name }}
              </p>
              <p class="mt-2 flex items-center text-sm text-gray-500">
                <nav class="flex" aria-label="Breadcrumb">
                  <ol role="list" class="flex items-center space-x-4">
                    <li class="flex">
                      <component
                        class="h-5 w-5 flex-shrink-0"
                        aria-hidden="true"
                        :is="item.minMax === 'min' ? ArrowDownIcon : ArrowUpIcon"
                      />
                    </li>
                    <li class="flex">
                      <p> {{ item.minMax === 'min' ? 'Mindestens' : 'Maximal' }}</p>
                    </li>
                    <li class="flex">
                      <p> {{ item.value }}</p>
                    </li>
                    <li class="flex">
                      <p> {{ item.parameter === 'energy_kj' ? 'kJ' : '' }}</p>
                      <p> {{ item.parameter === 'nutri_class' ? 'Nutri-Klasse' : '' }}</p>
                      <p> {{ item.parameter.endsWith('_g') ? 'g' : '' }}</p>
                    </li>
                  </ol>
                </nav>
              </p>
            </div>
            <div class="hidden md:block">
              <component
                class="h-7 w-7 flex-shrink-0"
                :class="item.hintLevel === 'warn' ? 'text-orange-500' : 'text-red-500'"
                aria-hidden="true"
                :is="item.hintLevel === 'warn' ? LightBulbIcon : ExclamationTriangleIcon"
              />
              <p class="text-sm"> {{ item.hintLevel === 'warn' ? 'Warnung' : 'Fehler' }}</p>
            </div>
          </div>
        </div>
      </template>
    </List>
  </div>
</template>

<script setup lang="ts">
import { ref, watch, onMounted, computed } from "vue";
import { TagIcon, ChevronRightIcon, HomeIcon } from "@heroicons/vue/20/solid";
import {
  ArrowDownIcon,
  LightBulbIcon,
  ExclamationTriangleIcon,
  ArrowUpIcon,
} from "@heroicons/vue/24/outline";
import List from "@/components/base/list/Main.vue";
import { useRoute } from "vue-router";
import { useHintStore } from "@/modules/hint/store/index.ts";

const hintStore = useHintStore();

const searchValue = ref();

const route = useRoute();

const hints = computed(() => {
  return hintStore.hints;
});

onMounted(() => {
  hintStore.fetchHints(route.query);
});

watch(
  () => route.query,
  () => {
    updateSearch(route.query);
  },
  { immediate: true, deep: true }
);

function updateSearch(params) {
  hintStore.fetchHints(params);
}

const sortOptions = [];

const filters = [
  {
    id: "parameter",
    name: "Parameter",
    options: [
      { value: "energy_kj", label: "Energie", checked: false },
      { value: "sugar_g", label: "Zucker", checked: false },
      { value: "fibre_g", label: "Balaststoffe", checked: false },
      { value: "protein_g", label: "Eiweiß", checked: false },
      { value: "sodium_mg", label: "Salz", checked: false },
      { value: "fat_sat_g", label: "Gesät. Fette", checked: false },
      { value: "weight_g", label: "Gewicht", checked: false },
      { value: "nutri_points", label: "Nutri Punkte", checked: false },
    ],
  },
];
const buttonList = [{ name: "Neue Gruppe", linkName: "" }];
</script>
