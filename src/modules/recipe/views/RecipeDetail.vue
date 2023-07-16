<template>
  <div class="2xl:px-64 xl:px-30">
    <main class="relative z-0 flex-1 overflow-y-auto focus:outline-none">
      <!-- Breadcrumb -->
      <Breadcrumbs :pages="pages" />
      <article>
        <RecipeOverview
          :recipeItems="recipeDetail.recipeItems"
          @openRecipeItemUpdate="onOpenRecipeItemUpdate"
          @openRecipeItemAdd="openRecipeItemAdd"
          :isEditable="recipeDetail.allowEdit"
        />

        <RecipeOverviewNutri
          :recipeItems="recipeDetail.recipeItems"
          @openRecipeItemUpdate="onOpenRecipeItemUpdate"
          @openRecipeItemAdd="openRecipeItemAdd"
        />
        <RecipeOverview2
          :recipeItems="recipeDetail.recipeItems"
          @openRecipeItemUpdate="onOpenRecipeItemUpdate"
          @openRecipeItemAdd="openRecipeItemAdd"
        />
        <RecipeOverview3
          :recipeItems="recipeDetail.recipeItems"
          @openRecipeItemUpdate="onOpenRecipeItemUpdate"
          @openRecipeItemAdd="openRecipeItemAdd"
        />
        <RecipeItemUpdate
          :open="openRecipeItemUpdate"
          :reciptItem="openRecipeItem"
          @close="onRecipeItemUpdateClose"
          header="Zutat"
        />
        <div
          class="px-2 py-2 sm:flex sm:items-center sm:justify-between sm:px-6 lg:px-8"
        >
          <div class="min-w-0 flex-1"></div>
          <div v-if="recipeDetail.allowEdit" class="mt-4 flex-2 sm:mt-0 sm:ml-4">
            <PrimaryButton
              color="blue"
              label="Bearbeiten"
              @click="onEditClicked(recipeDetail.id)"
            />
          </div>
          <div class="mt-4 flex-2 sm:mt-0 sm:ml-4">
            <PrimaryButton
              color="blue"
              label="Simulieren"
              @click="onSimulateClicked(recipeDetail.id)"
            />
          </div>
        </div>
      </article>
    </main>
    <CreateRecipe
      :open="openRecipeUpdate"
      @close="onRecipeUpdateClose"
      :items="recipeDetail"
    />
  </div>
</template>

<script setup lang="ts">
import Breadcrumbs from "@/components/breadcrumbs/Header.vue";
import PrimaryButton from "@/components/button/Primary.vue";
import RecipeItemList from "@/modules/recipe/components/RecipeItemList.vue";
import RecipeOverview from "@/modules/recipe/components/RecipeMainOverview.vue";
import RecipeOverview2 from "@/modules/recipe/components/RecipeMainOverview2.vue";
import RecipeOverview3 from "@/modules/recipe/components/RecipeMainOverview3.vue";
import RecipeOverviewNutri from "@/modules/recipe/components/RecipeMainOverviewNutri.vue";

import CreateRecipe from "@/modules/recipe/components/simulator/createRecipe/CreateRecipe.vue";
import { useRouter } from "vue-router";

const router = useRouter();

const route = useRoute();

const pages = computed(() => {
  return [
    { name: "Rezepte", link: "RecipesMain", current: false },
    { name: `${recipeDetail.value.name}`, link: `RecipeDetail`, current: true },
  ];
});

const recipeStore = useRecipeStore();

const recipeDetail = computed(() => {
  return recipeStore.recipeDetail;
});

async function onSimulateClicked(id) {
  const response = await recipeStore.cloneRecipe(id);
  if (response && response.status == 201) {
    router.push({
      name: "SimulatorMain",
      params: { id: response.data.id },
    });
  }
}

async function onEditClicked(id) {
  debugger;
}

import { ref, watch, onMounted, computed } from "vue";
import EmptyItem from "@/modules/recipe/components/simulator/EmptyItem.vue";
import RecipeItemUpdate from "@/modules/recipe/components/RecipeItem/RecipeItem.vue";
import { useRoute } from "vue-router";
import { useRecipeStore } from "@/modules/recipe/store/index";

const openRecipeItemUpdate = ref(false);
const openRecipeItem = ref({});

function openRecipeItemAdd() {
  openRecipeItem.value = {};
  openRecipeItemUpdate.value = true;
}

function onOpenRecipeItemUpdate(reciptItem: Object) {
  openRecipeItemUpdate.value = true;
  openRecipeItem.value = reciptItem;
}

const openRecipeUpdate = ref(false);

function onRecipeItemUpdateClose() {
  openRecipeUpdate.value = false;
  openRecipeItemUpdate.value = false;
}

function onAddRecipe(reciptItem: Object) {
  openRecipeUpdate.value = true;
  openRecipeItem.value = reciptItem;
}

onMounted(() => {
  const id = route.params.id;
  recipeStore.fetchRecipeById(id);
});
</script>
