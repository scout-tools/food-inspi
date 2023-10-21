<template>
  <div
    class="max-w-sm p-6 bg-white border border-gray-200 rounded-lg shadow my-4"
  >
    <a href="#">
      <h4
        class="mb-2 text-xl tracking-tight text-gray-900"
      >
       {{ props.item.day.date }} / {{ props?.item?.start }} Uhr - {{ props?.item?.end }} Uhr
      </h4>
      <h5
        class="mb-2 text-xl font-bold tracking-tight text-gray-900"
      >
       {{ props?.item?.name }} / {{ props?.item?.getMealTypeDisplay }}
      </h5>
    </a>
    <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">
      {{ props?.item?.mealItems.map(item => item.recipe.name).join(", ")  }}
    </p>
    <!-- <a
      href="#"
      class="inline-flex items-center px-3 py-2 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300"
    >
      Read more
      <svg
        class="w-3.5 h-3.5 ml-2"
        aria-hidden="true"
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 14 10"
      >
        <path
          stroke="currentColor"
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M1 5h12m0 0L9 1m4 4L9 9"
        />
      </svg>
    </a> -->
  </div>
</template>
  
  <script setup lang="ts">

const props = defineProps({
  item: { type: Object, required: true },
});
</script>
  