<template>
  <div>
    <section aria-labelledby="recent-heading" class="mt-16">
      <div class="mx-auto max-w-7xl sm:px-2 lg:px-8">
        <div class="mx-auto max-w-2xl space-y-8 sm:px-4 lg:max-w-4xl lg:px-0">
          <div
            :key="item.number"
            class="
              border-t border-b border-gray-200
              bg-gray-50
              px-4
              py-6
              shadow
              sm:rounded-lg sm:border
            "
          >
            <h2 class="text-lg font-medium leading-6 text-gray-900">
              {{ item.name }} - {{ recipeDetail[item.value] }} {{ item.unit }}
            </h2>
            <div class="mt-5 border-t border-gray-200">
              <Menu as="div" class="relative flex justify-end lg:hidden">
                <div class="flex items-center">
                  <MenuButton
                    class="
                      -m-2
                      flex
                      items-center
                      p-2
                      text-gray-400
                      hover:text-gray-500
                    "
                  >
                    <span class="sr-only"
                      >Options for order {{ item.number }}</span
                    >
                    <EllipsisVerticalIcon class="h-6 w-6" aria-hidden="true" />
                  </MenuButton>
                </div>

                <transition
                  enter-active-class="transition ease-out duration-100"
                  enter-from-class="transform opacity-0 scale-95"
                  enter-to-class="transform opacity-100 scale-100"
                  leave-active-class="transition ease-in duration-75"
                  leave-from-class="transform opacity-100 scale-100"
                  leave-to-class="transform opacity-0 scale-95"
                >
                  <MenuItems
                    class="
                      absolute
                      right-0
                      z-10
                      mt-2
                      w-40
                      origin-bottom-right
                      rounded-md
                      bg-white
                      shadow-lg
                      ring-1 ring-black ring-opacity-5
                      focus:outline-none
                    "
                  >
                    <div class="py-1">
                      <MenuItem v-slot="{ active }">
                        <a
                          :href="item.href"
                          :class="[
                            active
                              ? 'bg-gray-100 text-gray-900'
                              : 'text-gray-700',
                            'block px-4 py-2 text-sm',
                          ]"
                          >View</a
                        >
                      </MenuItem>
                      <MenuItem v-slot="{ active }">
                        <a
                          :href="item.invoiceHref"
                          :class="[
                            active
                              ? 'bg-gray-100 text-gray-900'
                              : 'text-gray-700',
                            'block px-4 py-2 text-sm',
                          ]"
                          >Invoice</a
                        >
                      </MenuItem>
                    </div>
                  </MenuItems>
                </transition>
              </Menu>
            </div>
            <ul role="list" class="divide-y divide-gray-200">
              <li class="p-2">
                <div class="items-center sm:items-start">
                  <div class="overflow-hidden rounded-lg">
                    <div
                      class="
                        py-4
                        sm:grid sm:grid-cols-3 sm:gap-4 sm:py-5 sm:px-6
                      "
                    >
                      <dt class="text-sm font-medium text-gray-500">
                        Hinweise
                      </dt>
                      <dd
                        v-if="
                          filterRecipeDetail(recipeDetail.hints, item.value) &&
                          filterRecipeDetail(recipeDetail.hints, item.value)
                            .length
                        "
                        class="mt-1 text-sm text-gray-900 sm:col-span-2 sm:mt-0"
                      >
                        <span
                          v-for="hint in filterRecipeDetail(
                            recipeDetail.hints,
                            item.value
                          )"
                          :key="hint.name"
                          class="
                            inline-flex
                            rounded-full
                            px-2
                            text-xs
                            font-semibold
                            leading-5
                          "
                          :class="
                            hint.hintLevel === 'warn'
                              ? 'bg-orange-100 text-orange-800'
                              : 'bg-red-100 text-red-800'
                          "
                        >
                          {{ hint.name }} ({{ hint.minMax }}. {{ hint.value }}
                          {{ item.unit }})
                        </span>
                      </dd>
                      <dd
                        v-else
                        class="mt-1 text-sm text-gray-900 sm:col-span-2 sm:mt-0"
                      >
                        <span
                          class="
                            inline-flex
                            rounded-full
                            bg-green-100
                            px-2
                            text-xs
                            font-semibold
                            leading-5
                            text-green-800
                          "
                          >Alles bestens</span
                        >
                      </dd>
                    </div>
                    <div class="py-5 border-t border-gray-200">
                      <NutritionalsBoxPlot2 :item="item" />
                    </div>
                    <div class="py-5 border-t border-gray-200">
                      <h4 class="my-2">Top Produkte für {{ item.name }}:</h4>
                        <span
                          v-for="hint in sortItems(
                            recipeDetail,
                            item.value
                          )"
                          :key="hint.name"
                          class="
                            mx-1
                            inline-flex
                            rounded-full
                            px-2
                            text-sm
                            font-semibold
                            leading-5
                            bg-blue-100
                            text-blue-800
                          "
                        >
                          {{ hint.name }} {{ (hint.value).toFixed(1) }}
                          {{ item.unit }})
                        </span>
                    </div>
                  </div>
                </div>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import NutritionalsBoxPlot2 from "@/modules/recipe/components/chart/NutritionalsBoxPlot2.vue";

import {
  Disclosure,
  DisclosureButton,
  DisclosurePanel,
  Menu,
  MenuButton,
  MenuItem,
  MenuItems,
} from "@headlessui/vue";

import {
  ChatBubbleLeftEllipsisIcon,
  CodeBracketIcon,
  EllipsisVerticalIcon,
  EyeIcon,
  FlagIcon,
  HandThumbUpIcon,
  MagnifyingGlassIcon,
  PlusIcon,
  ShareIcon,
  StarIcon,
} from "@heroicons/vue/20/solid";

const props = defineProps({
  item: Object,
  recipeDetail: Object,
});

const snakeToCamel = (str) =>
  str
    .toLowerCase()
    .replace(/([-_][a-z])/g, (group) =>
      group.toUpperCase().replace("-", "").replace("_", "")
    );

function filterRecipeDetail(items, value) {
  let returnItems = [];
  if (items && items.length > 0) {
    returnItems = items.filter(
      (item) => snakeToCamel(item.parameter) === value
    );
    if (returnItems.length > 1) {
      returnItems = returnItems.filter((item) => item.hintLevel === "error");
    }
  }
  return returnItems;
}

function sortItems(items, value) {
  const returnArray =  []
  items?.recipeItems?.forEach(element => {
    if (element[value] > 0) {
      returnArray.push({
        name: element.portion.ingredient.name,
        value: element[value]
      });
    }
  });
  const sortedReturnArray = returnArray.sort(
      (p1, p2) => (p1.value < p2.value) ? 1 : (p1.value > p2.value) ? -1 : 0);
return sortedReturnArray.slice(0, 3);

}
</script>
