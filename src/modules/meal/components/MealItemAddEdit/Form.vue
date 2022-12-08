<template>
  <div>
    <BaseField
      component="Select"
      label="Rezept"
      techName="recipe"
      v-model="state.recipe"
      :items="recipes"
      :errors="errors.recipe?.$errors"
    />
    <BaseField
      component="Number"
      label="Portion als Faktor"
      techName="factor"
      v-model="state.factor"
      :errors="errors.factor?.$errors"
    />
    <PrimaryButton
      @click="onSaveClicked"
      :label="!isEdit ? 'Rezept hinzufügen' : 'Rezept bearbeiten'"
    />
    <PrimaryButton
      v-if="isEdit"
      class="mx-2 my-2"
      @click="onDeleteClicked()"
      color="red"
      label="Rezept löschen"
    />
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
import { useIngredientStore } from "@/modules/ingredient/store/index";
import { useRecipeStore } from "@/modules/recipe/store/index";
import { useMealStore } from "@/modules/meal/store/index";

import { useVuelidate } from "@vuelidate/core";
import { required, email, minLength, maxLength } from "@vuelidate/validators";

const state = reactive({
  meal: 1,
  recipe: {
    name: '',
    id: 1,
  },
  factor: 0.33,
});


const rules = {
  meal: {
    required,
  },
  recipe: {
    required,
  },
  factor: {
    required,
  },
};

const props = defineProps({
  items: { type: Object, required: true },
});

const v$ = useVuelidate(rules, state);

const ingredient = ref(null);
const errors = ref([]);
const isLoading = ref(false);

const ingredientStore = useIngredientStore();
const recipeStore = useRecipeStore();
const mealStore = useMealStore();

const recipes = computed(() => {
  return recipeStore.recipes;
});

const isEdit = computed(() => {
  return !!props.items?.id
});


function onDeleteClicked() {
  mealStore.deleteMealItem(props.items.id).then((response) => {
    let id = Number(route.params.id);
    goToRoute(id);
  });
}


function onSaveClicked() {
  v$.value.$validate();
  errors.value = v$.value;
  if (errors.value.$error) {
    commonStore.showError("Bitte Felder überprüfen");
    return;
  }

  let id = Number(route.params.id);
  let eventDayId = Number(route.params.eventDayId);
  // new
  if (!isEdit.value) {
    mealStore
      .createMealItem({
        meal: state.meal,
        recipe: state.recipe.id,
        factor: Number(state.factor),
      })
      .then((response3: any) => {
        goToRecipe("EventDay", {
          id,
          eventDayId,
        });
      });
  }
  // edit
  if (isEdit.value) {
    mealStore
      .updateMealItem({
        id: props.items?.id,
        meal: state.meal,
        recipe: state.recipe.id,
        factor: Number(state.factor),
      })
      .then((response2: any) => {
        goToRecipe("EventDay", {
          id,
          eventDayId,
        });
      })
  }
}

function goToRecipe(route: string, params: any) {
  router.push({
    name: route,
    params: params,
  });
  if (router.currentRoute.value.name === route) {
    router.go(router.currentRoute.value);
  }
}

import { useRoute } from "vue-router";
const route = useRoute();

import { useRouter } from "vue-router";
const router = useRouter();



onMounted(() => {
  mealStore.fetchMealTypes()
  recipeStore.fetchRecipes()
  if (isEdit.value) {
    state.meal = props.items?.meal;
    state.recipe = props.items?.recipe;
    state.factor = props.items?.factor;
  } else {
    state.meal = props.items?.meal;
    state.recipe = null;
    state.factor = 1;
  }
});
</script>
