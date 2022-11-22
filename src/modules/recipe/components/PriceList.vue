<template>
  <div class="px-4 sm:px-6 lg:px-8">
    <div class="sm:flex sm:items-center">
      <div class="sm:flex-auto">
        <h1 class="text-xl font-semibold text-gray-900">Preisliste</h1>
      </div>
    </div>
    <div class="-mx-4 mt-8 flex flex-col sm:-mx-6 md:mx-0">
      <table class="min-w-full divide-y divide-gray-300">
        <thead>
          <tr>
            <th
              scope="col"
              class="
                py-3.5
                pl-4
                pr-3
                text-left text-sm
                font-semibold
                text-gray-900
                sm:pl-6
                md:pl-0
              "
            >
              Zutat
            </th>
            <th
              scope="col"
              class="
                hidden
                py-3.5
                px-3
                text-right text-sm
                font-semibold
                text-gray-900
                sm:table-cell
              "
            >
              Preis pro Kg
            </th>
            <th
              scope="col"
              class="
                hidden
                py-3.5
                px-3
                text-right text-sm
                font-semibold
                text-gray-900
                sm:table-cell
              "
            >
              Gewicht in g
            </th>
            <th
              scope="col"
              class="
                py-3.5
                pl-3
                pr-4
                text-right text-sm
                font-semibold
                text-gray-900
                sm:pr-6
                md:pr-0
              "
            >
              Preis in €
            </th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="project in props.recipeItems"
            :key="project.id"
            class="border-b border-gray-200"
          >
            <td class="py-4 pl-4 pr-3 text-sm sm:pl-6 md:pl-0">
              <div class="font-medium text-gray-900">{{ project.portion.ingredient.name }}</div>
            </td>
            <td
              class="
                hidden
                py-4
                px-3
                text-right text-sm text-gray-500
                sm:table-cell
              "
            >
              {{ project.pricePerKg }} €/Kg
            </td>
            <td
              class="
                hidden
                py-4
                px-3
                text-right text-sm text-gray-500
                sm:table-cell
              "
            >
              {{ project.weightG }} g
            </td>
            <td
              class="
                py-4
                pl-3
                pr-4
                text-right text-sm text-gray-500
                sm:pr-6
                md:pr-0
              "
            >
              {{ project.price }} €
            </td>
          </tr>
        </tbody>
        <tfoot>
          <tr>
            <th
              scope="row"
              colspan="3"
              class="
                hidden
                pl-6
                pr-3
                pt-4
                text-right text-sm
                font-semibold
                text-gray-900
                sm:table-cell
                md:pl-0
              "
            >
              Total
            </th>
            <th
              scope="row"
              class="
                pl-4
                pr-3
                pt-4
                text-left text-sm
                font-semibold
                text-gray-900
                sm:hidden
              "
            >
              Total
            </th>
            <td
              class="
                pl-3
                pr-4
                pt-4
                text-right text-sm
                font-semibold
                text-gray-900
                sm:pr-6
                md:pr-0
              "
            >
              {{ getSumByKey(props.recipeItems, 'price').toFixed(2) }} €
            </td>
          </tr>
        </tfoot>
      </table>
    </div>
  </div>
</template>

<script setup lang="ts">
const projects = [
  {
    id: 1,
    name: "New Advertising Campaign",
    hours: "12.0",
    rate: "$75.00",
    price: "$900.00",
  },
  {
    id: 2,
    name: "New Adsadaign",
    hours: "12.0",
    rate: "$75.00",
    price: "$900.00",
  },
  // More projects...
];

const getSumByKey = (arr, key) => {
  return arr.reduce((accumulator, current) => accumulator + Number(current[key]), 0)
}


const props = defineProps({
  label: { type: String, required: true },
  value: { type: String, required: true},
  unit: { type: String, required: false, default: "g"},
  recipeItems: { type: Array, required: false, default: []}
});
</script>