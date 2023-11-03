<template>
  <div
    class="max-w-sm p-6 bg-white border border-gray-200 rounded-lg shadow my-4"
  >
    <h4 class="mb-2 text-xl tracking-tight text-gray-900">
      {{ $dayjs(props.item.day.date).format("dd - DD.MM") }}
    </h4>
    <h4 class="mb-2 text-large tracking-tight text-gray-900">
      {{ props?.item?.start }} Uhr - {{ props?.item?.end }} Uhr
    </h4>
    <h5 class="mb-2 text-xl font-bold tracking-tight text-gray-900">
      {{ props?.item?.name }}
      {{
        props?.item?.getMealTypeDisplay !== props?.item?.name
          ? "/ " + props?.item?.getMealTypeDisplay
          : ""
      }}
    </h5>
    <router-link
      class="underline text-blue-600"
      v-for="item in props?.item?.mealItems"
      :key="item.id"
      :to="{ name: 'RecipeDetail', params: { id: item.recipe?.id } }"
      target="_blank"
    >
      {{ item.recipe.name }}
    </router-link>
    <h4 v-if="props?.item?.mealItems.length == 0">Keine Rezepte vorhanden</h4>
  </div>
</template>
  
  <script setup lang="ts">
const props = defineProps({
  item: { type: Object, required: true },
});
</script>
  