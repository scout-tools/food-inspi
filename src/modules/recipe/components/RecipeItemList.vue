<template>
  <div class="xl:px-30 xl:px-30 lg:px-5">
    <div class="py-4 sm:grid sm:grid-cols-3 sm:gap-4 sm:py-5 sm:px-6">
      <dd class="mt-1 text-sm text-gray-900 sm:col-span-3 sm:mt-0">
        <ul
          role="list"
          class="divide-y divide-gray-200 rounded-md border border-gray-200"
        >
          <li
            v-for="item in props.recipeItems"
            :key="item.name"
            class="flex items-center justify-between py-3 pl-3 pr-4 text-sm"
          >
            <div class="flex w-0 flex-1 items-center">
              <NutriSlim :nutriClass="item.nutriClass" />
              <span class="ml-2 w-0 flex-1 truncate"
                >{{ getFormatedText(item) }}</span
              >
              <span
                v-if="item.nutriPoints < -0.5"
                class="ml-2 h-5 w-5 text-green-600"
                ><FaceSmileIcon
              /></span>
              <span
                v-if="item.nutriPoints > 0.5"
                class="ml-2 h-5 w-5 text-red-600"
                ><FaceFrownIcon
              /></span>
              <button v-if="props.editable" @click="openRecipeItemUpdate(item)">
                <ChevronRightIcon
                  class="h-5 w-5 text-gray-400"
                  aria-hidden="true"
                />
              </button>
            </div>
          </li>
        </ul>
        <button v-if="props.editable" @click="openRecipeItemAdd()">
          <PlusCircleIcon
            class="mx-2 my-2 h-10 w-10 text-green-600"
            aria-hidden="true"
          />
        </button>
      </dd>
    </div>
  </div>
</template>

<script setup lang="ts">
import {
  StarIcon,
  ChevronRightIcon,
  PlusCircleIcon,
  FaceSmileIcon,
  FaceFrownIcon,
} from "@heroicons/vue/20/solid";
import PrimaryButton from "@/components/button/Primary.vue";
import NutriSlim from "@/components/score/NutriSlim.vue";

const props = defineProps({
  label: { type: String, required: true },
  recipeItems: { type: Array, required: true },
  editable: { type: Boolean, required: false, default: false },
});

const emit = defineEmits(["openRecipeItemUpdate", "openRecipeItemAdd"]);

const openRecipeItemUpdate = (reciptItem) => {
  emit("openRecipeItemUpdate", reciptItem);
};

const openRecipeItemAdd = () => {
  emit("openRecipeItemAdd");
};

function getFormatedText(item: Object) {
  let text = ''
  text = `${text} ${Math.round(item?.quantity * item?.portion.weightG)} g
                ${item?.portion.ingredient.name } `
  if (item.portion.measuringUnit.name !== 'g') {
      text = `${text} / ${item?.quantity}  ${item?.portion.measuringUnit.name }`
  }
  return text
}
</script>
