<template>
  <div
    class="w-full max-w-md p-4 bg-white border border-gray-200 rounded-lg shadow sm:p-8"
  >
    <div class="flex items-center justify-between mb-4">
      <h5 class="text-xl font-bold leading-none text-gray-900">
        {{ item.name }} - {{ item.mealType }} ({{ totalWeigth(item, item.normPersons) }} g)
      </h5>
    </div>
    <div class="flow-root">
      <ul role="list" class="divide-y divide-gray-200" v-if="item?.portions?.length">
        <li class="py-3 sm:py-4" v-for="i in item?.portions" :key="i.id">
          <div class="flex items-center">
            <div class="flex-1 min-w-0 ms-4">
              <p class="text-md text-gray-800 truncate">
                {{ i?.ingredient }}
              </p>
              <!-- <p class="text-sm text-gray-500 truncate">{{ i.ingredient }}</p> -->
            </div>
            <div
              class="inline-flex items-center text-base font-semibold text-gray-900"
            >
            {{ i.weightG.weightG_Sum * item.normPersons }} g
            </div>
          </div>
        </li>
      </ul>
      <ul v-else>
        <li>Keine Zutat hinzugefügt</li>
      </ul>
    </div>
  </div>
</template>

<script setup lang="ts">

function totalWeigth(item: any, normPerson: number = 1) {
  return item?.portions?.reduce((acc, portion) => acc + portion.weightG.weightG_Sum * normPerson, 0);
}

const props = defineProps({
  item: { type: Object, required: true },
});
</script>
