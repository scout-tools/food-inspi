<template>
  <li class="bg-gray-50 px-4 py-6 shadow sm:rounded-lg sm:p-6">
    <article :aria-labelledby="'props.meal-title-' + props.meal.id">
      <div>
        <div>
          <h3 class="text-lg font-medium leading-6 text-gray-900">
            {{ props.meal.name }} ({{
              (props.meal.dayPartFactor * 100).toFixed(0)
            }}
            % Tagesanteil)
          </h3>
          <p class="mt-1 max-w-2xl text-sm text-gray-500">
            {{ props.meal?.getMealTypeDisplay }}
            {{ $dayjs(props.meal?.timeStart, "HH:mm:ss").format("LT") }} -
            {{ $dayjs(props.meal?.timeEnd, "HH:mm:ss").format("LT") }}
          </p>
          <button
            v-if="event?.allowEdit"
            @click="onUpdateMealClicked(props.meal)"
            class="text-sm text-blue-600 hover:text-blue-500"
          >
            Menü bearbeiten
          </button>
        </div>
        <div class="mt-5 border-t border-gray-200">
          <dl class="sm:divide-y sm:divide-gray-200">
            <div class="py-4 sm:grid sm:grid-cols-3 sm:gap-4 sm:py-5">
              <dt class="text-sm font-medium text-gray-500">
                Energieanteil des Ziel Tagesanteils
              </dt>
              <dd
                class="mt-1 text-sm text-red-500 sm:col-span-2 sm:mt-0"
                :class="
                  props.meal.dayPartEnergyKj <= 0.9 ||
                  props.meal.dayPartEnergyKj >= 1.1
                    ? 'text-red-500'
                    : 'text-green-500'
                "
              >
                {{ (props.meal.dayPartEnergyKj * 100).toFixed(0) }} %
              </dd>
            </div>
            <div class="py-4 sm:grid sm:grid-cols-3 sm:gap-4 sm:py-5">
              <dt class="text-sm font-medium text-gray-500">Einkaufspreis</dt>
              <dd class="mt-1 text-sm text-gray-900 sm:col-span-2 sm:mt-0">
                {{ props.meal.priceEur.toFixed(2) }} €
              </dd>
            </div>
            <div class="py-4 sm:grid sm:grid-cols-3 sm:gap-4 sm:py-5">
              <dt class="text-sm font-medium text-gray-500">Nutri Punkte</dt>
              <dd class="mt-1 text-sm text-gray-900 sm:col-span-2 sm:mt-0">
                <NutriSlim :nutriClass="props.meal.nutriClass" />
              </dd>
            </div>
            <div class="py-4 sm:grid sm:grid-cols-3 sm:gap-4 sm:py-5">
              <dt class="text-sm font-medium text-gray-500">Menu-Elemente</dt>
              <dd class="mt-1 text-sm text-gray-900 sm:col-span-2 sm:mt-0">
                <ul
                  role="list"
                  class="divide-y divide-gray-200 rounded-md border border-gray-200"
                  v-if="props.meal.mealItems.length"
                >
                  <li
                    class="flex items-center justify-between py-3 pl-3 pr-4 text-sm"
                    v-for="mealItem in props.meal.mealItems"
                    :key="mealItem.id"
                  >
                  <router-link
                        :to="{
                          name: 'RecipeDetail',
                          params: { id: mealItem.recipe.id },
                        }"
                        target="_blank"
                      >
                    <div class="flex w-0 flex-1 items-center">
                      <StarIcon
                        class="h-5 w-5 flex-shrink-0 text-gray-400"
                        aria-hidden="true"
                      />

                      <div>
                        <span class="ml-2 w-0 flex-1 truncate"
                          >{{ mealItem.factor }} x
                          {{ mealItem.recipe.name }} ({{
                            mealItem.energyKj
                          }}
                          kJ, {{ (mealItem.priceEur || 0).toFixed(2) }}
                          €)
                        </span>
                      </div>
                      <LinkIcon
                        class="h-5 w-5 flex-shrink-0 text-gray-400 mx-1"
                        aria-hidden="true"
                      />
                    </div>
                  </router-link>
                    <div class="ml-4 flex-shrink-0">
                      <button
                        v-if="event.allowEdit"
                        class="font-medium text-blue-600 hover:text-blue-500"
                        @click="onMenuItemUpdate(mealItem)"
                      >
                        bearbeiten
                      </button>
                    </div>
                  </li>
                </ul>
                <ul v-else>
                  <li>
                    Bitte füge ein Rezept hinzu.
                  </li>
                </ul>
              </dd>
            </div>
          </dl>
        </div>
        <div class="mt-6 flex justify-between space-x-8">
          <div class="flex text-sm">
            <span class="inline-flex items-center text-sm">
              <button
                v-if="event.allowEdit"
                @click="
                  onAddMealItemClicked({
                    meal: props.meal,
                  })
                "
                type="button"
                class="inline-flex font-medium text-blue-600 hover:text-blue-500"
              >
                <PlusIcon class="h-5 w-5" aria-hidden="true" />
                <span> Rezept zum Menü Hinzufügen</span>
              </button>
            </span>
          </div>
        </div>
      </div>
    </article>
  </li>
</template>

<script lang="ts" setup>
import NutriSlim from "@/components/score/NutriSlim.vue";
import { ref, watch, onMounted, computed } from "vue";

import {
  Menu,
  MenuButton,
  MenuItem,
  MenuItems,
  Popover,
  PopoverButton,
  PopoverPanel,
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
  PencilIcon,
  LinkIcon,
} from "@heroicons/vue/20/solid";
import {
  ArrowTrendingUpIcon,
  Bars3Icon,
  BellIcon,
  FireIcon,
  HomeIcon,
  UserGroupIcon,
  XMarkIcon,
  ShoppingCartIcon,
} from "@heroicons/vue/24/outline";

const props = defineProps({
  meal: { type: Array, required: true },
});

const emit = defineEmits([
  "onItemUpdate",
  "onMenuItemUpdate",
  "onAddMealItemClicked",
]);

const onUpdateMealClicked = (items) => {
  emit("onItemUpdate", items);
};

const onMenuItemUpdate = (items) => {
  emit("onMenuItemUpdate", items);
};

const onAddMealItemClicked = (items) => {
  emit("onAddMealItemClicked", items);
};

import { useMealStore } from "@/modules/meal/store/index";
const mealStore = useMealStore();

const event = computed(() => {
  return mealStore.mealEvent;
});
</script>