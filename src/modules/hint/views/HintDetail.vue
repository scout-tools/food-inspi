<template>
  <div class="2xl:px-64 xl:px-30">
    <Breadcrumbs :pages="pages" />
    <main class="relative z-40 flex-1 focus:outline-none">
      <article v-if="hint.name">
        <div class="overflow-hidden bg-white shadow sm:rounded-lg">
          <div class="px-4 py-5 sm:px-6">
            <h3 class="text-lg font-medium leading-6 text-gray-900">
              Inspi Regel
            </h3>
            <p class="mt-1 max-w-2xl text-sm text-gray-500">
              Details für diese Regel.
            </p>
          </div>
          <div class="border-t border-gray-200 px-4 py-5 sm:p-0">
            <dl class="sm:divide-y sm:divide-gray-200">
              <div class="py-4 sm:grid sm:grid-cols-3 sm:gap-4 sm:py-5 sm:px-6">
                <dt class="text-sm font-medium text-gray-500">Name</dt>
                <dd class="mt-1 text-sm text-gray-900 sm:col-span-2 sm:mt-0">
                  {{ hint.name }}
                </dd>
              </div>
              <div class="py-4 sm:grid sm:grid-cols-3 sm:gap-4 sm:py-5 sm:px-6">
                <dt class="text-sm font-medium text-gray-500">Parameter</dt>
                <dd class="mt-1 text-sm text-gray-900 sm:col-span-2 sm:mt-0">
                  {{ hint.parameter }}
                </dd>
              </div>
              <div class="py-4 sm:grid sm:grid-cols-3 sm:gap-4 sm:py-5 sm:px-6">
                <dt class="text-sm font-medium text-gray-500">Stufe</dt>
                <dd class="mt-1 text-sm text-gray-900 sm:col-span-2 sm:mt-0">
                  {{ hint.hintLevel }}
                </dd>
              </div>
              <div class="py-4 sm:grid sm:grid-cols-3 sm:gap-4 sm:py-5 sm:px-6">
                <dt class="text-sm font-medium text-gray-500">minMax</dt>
                <dd class="mt-1 text-sm text-gray-900 sm:col-span-2 sm:mt-0">
                  {{ hint.minMax }}
                </dd>
              </div>
              <div class="py-4 sm:grid sm:grid-cols-3 sm:gap-4 sm:py-5 sm:px-6">
                <dt class="text-sm font-medium text-gray-500">Wert</dt>
                <dd class="mt-1 text-sm text-gray-900 sm:col-span-2 sm:mt-0">
                  {{ hint.value }}
                </dd>
              </div>
            </dl>
          </div>
        </div>
        <apexchart
          v-if="hasData"
          type="boxPlot"
          ref="boxPlotRef"
          :options="options"
          :series="series"
        ></apexchart>
      </article>
      <div class="xl:hidden" v-else>Bitte Wähle eine Zutat</div>
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref, watch, onMounted, computed, getCurrentInstance } from "vue";
import Breadcrumbs from "@/components/breadcrumbs/Header.vue";
import { useHintStore } from "@/modules/hint/store/index";
import { useRecipeStore } from "@/modules/recipe/store/index";

import { useRoute } from "vue-router";

const route = useRoute();

const boxPlotRef = ref(null);
const isReady = ref(false);

const pages = computed(() => {
  return [
    { name: "Zutaten", link: "HintMain" },
    {
      name: `${hint.value.name}`,
      link: `HintDetail`,
    },
  ];
});

const hasData = computed(() => {
  return !!series?.value[0]?.data[0]?.y.length && hint.value.value && isReady.value;
});

const snakeToCamel = (str) =>
  str
    .toLowerCase()
    .replace(/([-_][a-z])/g, (group) =>
      group.toUpperCase().replace("-", "").replace("_", "")
    );

const options = {
  chart: {
    width: "100%",
  },
};

const series = computed(() => {
  const array = recipes.value.map(
    (object) => object[snakeToCamel(hint.value.parameter)]
  );
  array.sort(function (a, b) {
    return a - b;
  });

  return [
    {
      name: "Verteilung",
      type: "boxPlot",
      data: [
        {
          x: "data",
          y: array,
        },
      ],
    },
    {
      name: "Ausreißer",
      type: "scatter",
      data: [
        {
          x: "data",
          y: array,
        },
      ],
    },
    {
      name: "Regel",
      type: "scatter",
      data: [
        {
          x: "data",
          y: [hint.value.value],
        },
      ],
    },
  ];
});

const hintStore = useHintStore();
const recipeStore = useRecipeStore();

const hints = computed(() => {
  return hintStore.hints;
});

const hint = computed(() => {
  return hintStore.hint;
});

const recipes = computed(() => {
  return recipeStore.recipes;
});

onMounted(() => {
  const id = route.params.id;
  hintStore.fetchHintById(id);
  recipeStore.fetchRecipes();
  setTimeout(function () {
    isReady.value = true;
  }, 300);
});
</script>