<template>
  <div>
    <div>
      <BaseField
        component="Number"
        v-model="state.factor"
        techName="factor"
        label="Faktor"
        :errors="errors.factor?.$errors"
      />
      <PrimaryButton
        class="mx-0 my-2"
        @click="onSaveClicked"
        label="Faktor anwenden"
        :isLoading="isLoading"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import { useCommonStore } from "@/modules/common/store/index.ts";
const commonStore = useCommonStore();

import { reactive, onMounted, ref, watch, computed } from "vue";
import BaseField from "@/components/field/Base.vue";
import Select from "@/components/field/Select.vue";
import Breadcrumbs from "@/components/breadcrumbs/Header.vue";
import PrimaryButton from "@/components/button/Primary.vue";
import { useRecipeStore } from "@/modules/recipe/store/index.ts";

import { useVuelidate } from "@vuelidate/core";
import { required, email, minLength, maxLength } from "@vuelidate/validators";

const state = reactive({
  factor: 1.0,
});

const rules = {
  factor: {
    required,
  },
};

const v$ = useVuelidate(rules, state);

const ingredient = ref(null);
const errors = ref([]);
const isLoading = ref(false);

const recipeStore = useRecipeStore();

function onDeleteClicked() {
  recipeStore.deleteRecipeItem(props.reciptItem.id).then((response) => {
    let recipeId = Number(route.params.id);
    goToRecipe(recipeId);
  });
}

function onSaveClicked() {
  v$.value.$validate();
  errors.value = v$.value;
  if (errors.value.$error) {
    commonStore.showError("Bitte Felder überprüfen");
    return;
  }

  let recipeId = Number(route.params.id);

  if (!isNaN(recipeId)) {
    recipeStore
      .multiplyRecipeItems({
        id: recipeId,
        factor: state.factor,
      })
      .then((response2: any) => {
        goToRecipe(recipeId, route.name === "SimulatorMain");
      });
  }
}

function goToRecipe(recipeId: number, isSimulator = true) {
  router.push({
    name: isSimulator ? "SimulatorMain" : "RecipeDetail",
    params: {
      id: recipeId,
    },
  });
  if (
    router.currentRoute.value.name === "SimulatorMain" ||
    router.currentRoute.value.name === "RecipeDetail"
  ) {
    router.go(router.currentRoute.value);
  }
}

import { useRoute } from "vue-router";
const route = useRoute();

import { useRouter } from "vue-router";
const router = useRouter();

onMounted(async () => {});
</script>
