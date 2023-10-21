<template>
  <PageWrapper>
    <main class="relative z-0 flex-1 overflow-y-auto focus:outline-none">
      <!-- Breadcrumb -->
      <Breadcrumbs :pages="pages" />
      <div v-if="!loading">
        <dl class="mx-5 my-5  grid grid-cols-1 gap-5 sm:grid-cols-3">
          <div
            v-for="item in stats"
            :key="item.name"
            class="overflow-hidden rounded-lg bg-white px-4 py-5 shadow sm:p-6"
          >
            <dt class="truncate text-sm font-medium text-gray-500">
              {{ item.name }}
            </dt>
            <dd
              class="mt-1 text-xl font-semibold tracking-tight text-gray-900"
            >
              {{ item.stat || '-  ' }}
            </dd>
          </div>
        </dl>
        <RecipeOverview
          :recipeItems="recipeDetail.recipeItems"
          @openRecipeItemUpdate="onOpenRecipeItemUpdate"
          @openRecipeItemAdd="openRecipeItemAdd"
          @openRecipeFactor="openRecipeFactor"
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
        <RecipeFactorForm
          :open="openRecipeFactorForm"
          @close="onRecipeFactorFormClose"
          header="Rezeptfaktor"
        />
        <div
          class="px-2 py-2 sm:flex sm:items-center sm:justify-between sm:px-6 lg:px-8"
        >
          <div class="min-w-0 flex-1"></div>
          <div
            v-if="recipeDetail.allowEdit"
            class="mt-4 flex-2 sm:mt-0 sm:ml-4"
          >
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
      </div>
      <LoadingItem v-else />
    </main>
    <CreateRecipe
      :open="openRecipeUpdate"
      @close="onRecipeUpdateClose"
      :items="recipeDetail"
    />
  </PageWrapper>
</template>

<script setup lang="ts">
import Breadcrumbs from "@/components/breadcrumbs/Header.vue";
import PrimaryButton from "@/components/button/Primary.vue";
import RecipeItemList from "@/modules/recipe/components/RecipeItemList.vue";
import RecipeOverview from "@/modules/recipe/components/RecipeMainOverview.vue";
import RecipeOverview2 from "@/modules/recipe/components/RecipeMainOverview2.vue";
import RecipeOverview3 from "@/modules/recipe/components/RecipeMainOverview3.vue";
import RecipeOverviewNutri from "@/modules/recipe/components/RecipeMainOverviewNutri.vue";
import LoadingItem from "@/components/list/LoadingItem.vue";
import PageWrapper from "@/components/base/PageWrapper.vue";

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

const loading = computed(() => {
  return isLoading.value;
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

async function onEditClicked() {
  openRecipeUpdate.value = true;
}

function onRecipeUpdateClose() {
  openRecipeUpdate.value = false;
}

import { ref, watch, onMounted, computed } from "vue";
import EmptyItem from "@/modules/recipe/components/simulator/EmptyItem.vue";
import RecipeItemUpdate from "@/modules/recipe/components/RecipeItem/RecipeItem.vue";
import RecipeFactorForm from "@/modules/recipe/components/recipeFactor/RecipeFactorForm.vue";
import { useRoute } from "vue-router";
import { useRecipeStore } from "@/modules/recipe/store/index";

const openRecipeItemUpdate = ref(false);
const openRecipeFactorForm = ref(false);
const openRecipeItem = ref({});
const isLoading = ref(true);

function openRecipeItemAdd() {
  openRecipeItem.value = {};
  openRecipeItemUpdate.value = true;
}

function openRecipeFactor() {
  openRecipeFactorForm.value = true;
}

function onRecipeFactorFormClose() {
  openRecipeFactorForm.value = false;
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

onMounted(async () => {
  isLoading.value = true;
  const id = route.params.id;
  await Promise.all([
    recipeStore.fetchRecipeById(id),
    recipeStore.fetchVerified(),
  ]);

  isLoading.value = false;
});

const stats = computed(() => [
  { name: "Rezeptname", stat: recipeDetail.value?.name },
  { name: "Beschreibung", stat: recipeDetail.value?.description },
  { name: "Menütyp", stat: recipeDetail.value?.getMealTypeDisplay },
]);
</script>
