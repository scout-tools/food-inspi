<template>
  <PrimaryButton @click="createBlankSimulator">
    Neu
  </PrimaryButton>
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
import PrimaryButton from "@/components/button/Primary.vue";

const router = useRouter();

import { useRecipeStore } from "@/modules/recipe/store/index";
const recipeStore = useRecipeStore();


function createBlankSimulator() {
  recipeStore.createRecipe({}).then((response) => {
    router.push({
      name: "SimulatorMain",
      params: { id: response?.data.id },
    });
  });
}


</script>
