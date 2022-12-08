<template>
  <apexchart
    v-if="hasData"
    type="boxPlot"
    ref="boxPlotRef"
    :options="options"
    :series="series"
  ></apexchart>
</template>

<script setup lang="ts">
import { ref, watch, onMounted, computed, getCurrentInstance } from "vue";
import Breadcrumbs from "@/components/breadcrumbs/Header.vue";
import { useHintStore } from "@/modules/hint/store/index";
import { useRecipeStore } from "@/modules/recipe/store/index";

import { useRoute } from "vue-router";

const route = useRoute();

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

const recipeDetail = computed(() => {
  return recipeStore.recipeDetail;
});

const hasData = computed(() => {
  return !!recipeStore.recipes.length;
});

onMounted(() => {
  const id = route.params.id;
  recipeStore.fetchRecipeById(id);

  recipeStore.fetchRecipes();
});

const options = computed(() => {
  return {
    annotations: {
      points: [
        {
          x: recipeDetail.value["sugarG"],
          y: "Zucker",
          marker: {
            size: 10,
            fillColor: "#F4D920",
            strokeColor: "#000000",
            radius: 20,
          },
          label: {
            offsetY: 0,
            text: "aktueller Zucker",
          },
        },
        {
          x: recipeDetail.value["fatSatG"],
          y: "Gesät. Fettsäuren",
          marker: {
            size: 10,
            fillColor: "#F4D920",
            strokeColor: "#000000",
            radius: 20,
          },
          label: {
            offsetY: 0,
            text: "aktuelle ges. Fettsäuren",
          },
        },
        {
          x: recipeDetail.value["fibreG"],
          y: "Ballaststoffe",
          marker: {
            size: 10,
            fillColor: "#F4D920",
            strokeColor: "#000000",
            radius: 20,
          },
          label: {
            offsetY: 0,
            text: "Atuelle Ballaststoffe",
          },
        },
        {
          x: recipeDetail.value["proteinG"],
          y: "Eiweiß",
          marker: {
            size: 10,
            fillColor: "#F4D920",
            strokeColor: "#000000",
            radius: 20,
          },
          label: {
            offsetY: 0,
            text: "Aktueller Eiweiße",
          },
        },
        {
          x: recipeDetail.value["carbohydrateG"],
          y: "Kohlenhydrate",
          marker: {
            size: 10,
            fillColor: "#F4D920",
            strokeColor: "#000000",
            radius: 20,
          },
          label: {
            offsetY: 0,
            text: "Aktuelle Kohlenhydrate",
          },
        },
        {
          x: recipeDetail.value["saltG"],
          y: "Salz",
          marker: {
            size: 10,
            fillColor: "#F4D920",
            strokeColor: "#000000",
            radius: 20,
          },
          label: {
            offsetY: 0,
            text: "Aktuelles Salz",
          },
        },
      ],
    },
    grid: {
      row: {
        colors: ["#e5e5e5", "transparent"],
        opacity: 0.5,
        max: 40,
      },
      column: {
        colors: ["#f8f8f8", "transparent"],
        max: 40,
      },
      xaxis: {
        lines: {
          show: true,
          tickAmount: 3,
          max: 40,
        },
      },
      axis: {
        lines: {
          show: true,
        },
      },
    },
    chart: {
      width: "100%",
    },
    plotOptions: {
      bar: {
        horizontal: true,
      },
      boxPlot: {
        colors: {
          upper: "#668855",
          lower: "#5170A5",
        },
      },
    },
    title: {
      text: "Aktuelles Rezept im Vergleich zu Validierten Rezepten.",
      align: "left",
    },
    xaxis: {
      max: 70,
    },
  };
});

const series = computed(() => {
  const sugarG = recipes.value.map((object) => object["sugarG"]);
  sugarG.sort(function (a, b) {
    return a - b;
  });

  const fatSatG = recipes.value.map((object) => object["fatSatG"]);
  fatSatG.sort(function (a, b) {
    return a - b;
  });

  const fibreG = recipes.value.map((object) => object["fibreG"]);
  fibreG.sort(function (a, b) {
    return a - b;
  });
  const proteinG = recipes.value.map((object) => object["proteinG"]);
  proteinG.sort(function (a, b) {
    return a - b;
  });

const carbohydrateG = recipes.value.map((object) => object["carbohydrateG"]);
  carbohydrateG.sort(function (a, b) {
    return a - b;
  });

const saltG = recipes.value.map((object) => object["saltG"]);
  saltG.sort(function (a, b) {
    return a - b;
  });

  return [
    {
      name: "Zielwert",
      type: "boxPlot",
      data: [
        {
          x: "Zucker",
          y: sugarG,
        },
        {
          x: "Gesät. Fettsäuren",
          y: fatSatG,
        },
        {
          x: "Ballaststoffe",
          y: fibreG,
        },
        {
          x: "Eiweiß",
          y: proteinG,
        },
        {
          x: "Kohlenhydrate",
          y: carbohydrateG,
        },
        {
          x: "Salz",
          y: saltG,
        },
      ],
    },
  ];
});
</script>

<style>
</style>