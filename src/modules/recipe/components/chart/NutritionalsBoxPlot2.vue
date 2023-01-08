<template>
  <apexchart
    type="boxPlot"
    :ref="refName"
    :options="options"
    :series="series"
  ></apexchart>
</template>

<script setup lang="ts">
import { ref, watch, onMounted, computed } from "vue";
import { useRecipeStore } from "@/modules/recipe/store/index";

import { useRoute } from "vue-router";

const route = useRoute();

const recipeStore = useRecipeStore();


const recipes = computed(() => {
  return recipeStore.recipesVerified;
});

const recipeDetail = computed(() => {
  return recipeStore.recipeDetail;
});

const hasData = computed(() => {
  return !!recipeStore.recipes.length;
});

const props = defineProps({
  item: { type: Object, required: true },
});

onMounted(() => {
  const id = route.params.id;
  recipeStore.fetchRecipeById(id);

  recipeStore.fetchVerified();
});

const valueList = computed(() => {
  const value = recipes.value.map((object) => object[props.item.value]);
  value.push(recipeDetail.value[props.item.value])
  value.sort(function (a, b) {
    return a - b;
  });
  return value;
})

const refName = computed(() => {
  return `boxPlotRef${props.item.name}`
})
const options = computed(() => {
  return {
    annotations: {
      points: [
        {
          x: recipeDetail.value[props.item.value],
          y: props.item.name,
          marker: {
            size: 10,
            fillColor: "#F4D920",
            strokeColor: "#000000",
            radius: 20,
          },
          label: {
            offsetY: 0,
            text: `aktueller ${props.item.name}`,
          },
        },
      ],
    },
    grid: {
      row: {
        colors: ["#e5e5e5", "transparent"],
        opacity: 0.5,
        max: 20,
      },
      column: {
        colors: ["#f8f8f8", "transparent"],
        max: 20,
      },
      xaxis: {
        lines: {
          tickAmount: 3,
          max: 20,
        },
      },
      axis: {
        lines: {
        },
      },
    },
    chart: {
      width: "100%",
      height: "150px",
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
      text: "Bezug zu anderen Rezepten",
      align: "left",
    },
    xaxis: {
      max: Math.max.apply(Math, valueList.value),
      tickAmount: 4,
    },
  };
});

const series = computed(() => {
  return [
    {
      name: "Zielwert",
      type: "boxPlot",
      data: [
        {
          x: props.item.name,
          y: valueList.value,
        },
      ],
    },
  ];
});
</script>
