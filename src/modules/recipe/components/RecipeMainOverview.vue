<template>
  <div>
    <RecipeItemList
      @openRecipeItemAdd="openRecipeItemAdd"
      @openRecipeItemUpdate="openRecipeItemUpdate"
      :recipeItems="recipeItems"
      :editable="isEditable"
    />
    <dl class="sm:divide-y sm:divide-gray-200 border-t border-gray-200 px-2">
      <div class="py-4 sm:grid sm:grid-cols-3 sm:gap-4 sm:py-5 sm:px-6">
        <dt class="text-sm font-medium text-gray-500">Gesamt Nutri</dt>
        <dd class="mt-1 text-sm text-gray-900 sm:col-span-2 sm:mt-0">
          <NutriBar :nutriClass="recipeDetail.nutriClass" />
        </dd>
      </div>
      <div class="py-4 sm:grid sm:grid-cols-3 sm:gap-4 sm:py-5 sm:px-6">
        <dt class="text-sm font-medium text-gray-500">Hinweise</dt>
        <dd
          v-if="recipeDetail && recipeDetail.hints && recipeDetail.hints.length"
          class="mt-1 text-sm text-gray-900 sm:col-span-2 sm:mt-0"
        >
          <span
            v-for="hint in recipeDetail.hints"
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
            >{{ hint.name }}</span
          >
        </dd>
        <dd v-else class="mt-1 text-sm text-gray-900 sm:col-span-2 sm:mt-0">
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
            >Rezept ist super</span
          >
        </dd>
      </div>
    </dl>
    <div class="overflow-hidden bg-white shadow sm:rounded-lg">
      <div class="px-4 py-5 sm:px-6">
        <h3 class="text-lg font-medium leading-6 text-gray-900">
          Inhaltsstoffe
        </h3>
        <p class="mt-1 max-w-2xl text-sm text-gray-500">pro Person</p>
      </div>
      <div class="px-4 sm:px-6">
        <ListItem
          label="Engergie"
          :value="recipeDetail.energyKj"
          unit="kJ"
          :recipeItems="recipeItems"
        />
        <ListItem label="Ballaststoffe" :value="recipeDetail.fibreG" />
        <ListItem label="gesä. Fettsäuren" :value="recipeDetail.fatSatG" />
        <ListItem
          label="Nutri Punkte"
          :value="recipeDetail.nutriPoints"
          unit="Punkte"
        />
        <ListItem label="Eiweiß" :value="recipeDetail.proteinG" />
        <ListItem label="Gewicht" :value="recipeDetail.weightG" />
        <ListItem label="Zucker" :value="recipeDetail.sugarG" />
        <ListItem label="Salz" :value="recipeDetail.saltG" />
      </div>
        <div class="px-4 py-4"><NutritionalsBoxPlot/></div>
        <PriceList
          label="Engergie"
          :value="recipeDetail.energyKj"
          unit="kJ"
          :recipeItems="recipeItems"/>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, computed } from "vue";
import RecipeItemList from "@/modules/recipe/components/RecipeItemList.vue";
import PriceList from "@/modules/recipe/components/PriceList.vue";
import NutritionalsBoxPlot from "@//modules/recipe/components/chart/NutritionalsBoxPlot.vue";
import ListItem from "@/modules/recipe/components/ListItem.vue";
import { useRoute } from "vue-router";
import { useRecipeStore } from "@/modules/recipe/store/index.ts";

const route = useRoute();
const props = defineProps({
  recipeItems: { type: Array, required: true },
  isEditable: { type: Boolean, required: false, default: false },
});

const emit = defineEmits(["openRecipeItemUpdate", "openRecipeItemAdd"]);

const openRecipeItemUpdate = (reciptItem: Object) => {
  emit("openRecipeItemUpdate", reciptItem);
};
const openRecipeItemAdd = () => {
  emit("openRecipeItemAdd");
};

const recipeStore = useRecipeStore();

const recipeDetail = computed(() => {
  return recipeStore.recipeDetail;
});

onMounted(() => {
  const id = route.params.id;
  recipeStore.fetchRecipeById(id);
});
</script>
