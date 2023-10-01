<template>
  <TabWrapper>
    <!-- Tabs -->
    <div class="sm:hidden" v-if="isAuth">
      <label for="tabs" class="sr-only">Select a tab</label>
      <select
        id="tabs"
        name="tabs"
        @change="onChange($event)"
        v-model="selectedValue"
        class="mt-4 block w-full rounded-md border-gray-300 py-2 pl-3 pr-10 text-base focus:border-blue-500 focus:outline-none focus:ring-blue-500 sm:text-sm"
      >
        <option
          :value="tab.name"
          v-for="tab in tabs"
          :key="tab.name"
          :selected="selectedValue"
        >
          {{ tab.name }} ({{ tab.count }})
        </option>
      </select>
    </div>
    <div class="hidden sm:block" v-if="isAuth">
      <div class="border-b border-gray-200">
        <nav class="mt-2 -mb-px flex space-x-8" aria-label="Tabs">
          <router-link
            v-for="tab in tabs"
            :key="tab.name"
            :to="tab.linkName"
            :class="[
              tab.current
                ? 'border-blue-500 text-blue-600'
                : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-200',
              'whitespace-nowrap py-4 px-1 border-b-2 font-medium text-sm',
            ]"
          >
            {{ tab.name }}
            <span
              v-if="tab.count"
              :class="[
                tab.current
                  ? 'bg-blue-100 text-blue-600'
                  : 'bg-gray-100 text-gray-900',
                'hidden ml-2 py-0.5 px-2.5 rounded-full text-xs font-medium md:inline-block',
              ]"
              >{{ tab.count }}</span
            >
          </router-link>
        </nav>
      </div>
    </div>
    <SimpleList
      v-if="isAuth"
      :items="recipesFiltered"
      :isLoading="isLoading"
      detailPageLink="RecipeDetail"
    >
      <template v-slot:notEmpty="slotProps">
        <RecipeListItem :item="slotProps.item" />
      </template>
      <template v-slot:empty>
        <h1>Leer</h1>
      </template>
    </SimpleList>
    <div v-else>
      <h1>Du bist nicht eingeloggt.</h1>
      <PrimaryButton class="mx-3 my-3" @click="onLoginclicked">Einloggen</PrimaryButton>
    </div>
  </TabWrapper>
</template>

<script setup lang="ts">
import { ref, watch, onMounted, computed } from "vue";
import { useRoute, useRouter } from "vue-router";
import {
  ScaleIcon,
  UserGroupIcon,
  UserIcon,
  BellIcon,
} from "@heroicons/vue/24/outline";
import { useTaskStore } from "@/modules/task/store/index";
import { useDashboardStore } from "@/modules/dashboard/store/index";
import SimpleList from "@/components/list/SimpleList.vue";
import TabWrapper from "@/components/base/TabWrapper.vue";
import RecipeListItem from "@/modules/recipe/components/RecipeListItem.vue";
import { useEventStore } from "@/modules/event/store";
import PrimaryButton from "@/components/button/Primary.vue"

function onLoginclicked() {
	authStore.login()
}

const router = useRouter();

import { useRecipeStore } from "@/modules/recipe/store/index";
const recipeStore = useRecipeStore();

const isLoading = computed(() => {
  return recipeStore.isLoading;
});

const recipesFiltered = computed(() => {
  const query = { ...router.currentRoute.value.query };
  return recipes.value.filter((q) => q.mealType === query.meal_type);
});

const selectedValue = ref("Aktive Anmeldephase");

function onChange(event) {
  const linkName = tabs.value.find((item) => item.name === selectedValue.value)[
    "linkName"
  ];
  router.push(linkName);
}

watch(() => router.currentRoute.value.query, refresh);

const tabs = computed(() => {
  const query = { ...router.currentRoute.value.query };

  return [
    {
      name: "Warm",
      linkName: { name: "RecipeMyRecipes", query: {  meal_type: "lunch_warm" } },
      count: recipes.value.filter((q) => q.mealType === "lunch_warm").length,
      current: query.meal_type === "lunch_warm",
    },
    {
      name: "Kalt",
      linkName: { name: "RecipeMyRecipes", query: { meal_type: "lunch_cold" } },
      count: recipes.value.filter((q) => q.mealType === "lunch_cold").length,
      current: query.meal_type === "lunch_cold",
    },
    {
      name: "Nachtisch",
      linkName: { name: "RecipeMyRecipes", query: { meal_type: "snack" } },
      count: recipes.value.filter((q) => q.mealType === "snack").length,
      current: query.meal_type === "snack",
    },
    {
      name: "Frühstück",
      linkName: { name: "RecipeMyRecipes", query: { meal_type: "breakfast" } },
      count: recipes.value.filter((q) => q.mealType === "breakfast").length,
      current: query.meal_type === "breakfast",
    },
    {
      name: "Getränk",
      linkName: { name: "RecipeMyRecipes", query: { meal_type: "drink" } },
      count: recipes.value.filter((q) => q.mealType === "drink").length,
      current: query.mealType === "drink",
    },
  ];
});

import { useAuthStore } from "@/modules/auth/store/index.ts";
const authStore = useAuthStore();

const isAuth = computed(() => {
  return authStore.isAuth;
});



const recipes = computed(() => {
  return recipeStore.myRecipies;
});

function refresh() {
  recipeStore.fetchMyRecipies();
}


onMounted(() => {
  refresh();
});

</script>
