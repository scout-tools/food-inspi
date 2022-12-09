<template>
  <li
    class="bg-gray-50 px-4 py-6 shadow sm:rounded-lg sm:p-6"
  >
    <article :aria-labelledby="'props.meal-title-' + props.meal.id">
      <div>
        <div class="flex space-x-3">
          <div class="min-w-0 flex-1">
        <span
            class="
              inline-block
              flex-shrink-0
              rounded-full
              bg-green-100
              px-2
              py-0.5
              text-xs
              font-medium
              text-green-800
            "
            >{{ props.meal.getMealTypeDisplay }}</span
          >
            <p class="text-sm text-gray-500">
              <!-- <a :href="props.meal.href" class="hover:underline">
                <time :datetime="props.meal.datetime">{{ props.meal.date }}</time>
              </a> -->
            </p>
          </div>
          <div class="flex flex-shrink-0 self-center">
            <Menu as="div" class="relative inline-block text-left">
              <div>
                <MenuButton
                  class="
                    -m-2
                    flex
                    items-center
                    rounded-full
                    p-2
                    text-gray-400
                    hover:text-gray-600
                  "
                >
                  <span class="sr-only">Open options</span>
                  <EllipsisVerticalIcon class="h-5 w-5" aria-hidden="true" />
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
                    w-56
                    origin-top-right
                    rounded-md
                    bg-white
                    shadow-lg
                    ring-1 ring-black ring-opacity-5
                    focus:outline-none
                  "
                >
                  <div class="py-1">
                    <MenuItem @click="onUpdateMealClicked(props.meal)" v-slot="{ active }">
                      <a
                        :class="[
                          active
                            ? 'bg-gray-100 text-gray-900'
                            : 'text-gray-700',
                          'flex px-4 py-2 text-sm',
                        ]"
                      >
                        <StarIcon
                          class="mr-3 h-5 w-5 text-gray-400"
                          aria-hidden="true"
                        />
                        <span>Ändern</span>
                      </a>
                    </MenuItem>
                  </div>
                </MenuItems>
              </transition>
            </Menu>
          </div>
        </div>
        <h2
          :id="'props.meal-title-' + props.meal.id"
          class="mt-4 text-base font-medium text-gray-900"
        >
          {{ props.meal.name }} ({{ props.meal.energyKj }} kJ)
        </h2>
      </div>
        <p
          v-for="mealItem in props.meal.mealItems"
          :key="mealItem.id"
          class="mt-1 truncate text-sm text-gray-500"
        >
          {{ mealItem.factor }} x {{ mealItem.recipe.name }} ({{ mealItem.energyKj }} kJ)
          <button class="font-medium text-blue-600 hover:text-blue-500" @click="onMenuItemUpdate(mealItem)">
            bearbeiten
          </button>
        </p>
      <div class="mt-6 flex justify-between space-x-8">
        <div class="flex text-sm">
          <span class="inline-flex items-center text-sm">
            <button
              @click="onAddMealItemClicked({
                meal: props.meal.id
              })"
              type="button"
              class="inline-flex font-medium text-blue-600 hover:text-blue-500"
            >
              <PlusIcon class="h-5 w-5" aria-hidden="true" />
              <span> Rezept zum Menü Hinzufügen</span>
            </button>
          </span>
        </div>
      </div>
    </article>
  </li>
</template>

<script lang="ts" setup>
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
  PencilIcon
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

const emit = defineEmits(["onItemUpdate", "onMenuItemUpdate", "onAddMealItemClicked"]);

const onUpdateMealClicked = (items) => {
  emit("onItemUpdate", items);
};

const onMenuItemUpdate = (items) => {
  emit("onMenuItemUpdate", items);
};

const onAddMealItemClicked = (items) => {
  emit("onAddMealItemClicked", items);
};
</script>