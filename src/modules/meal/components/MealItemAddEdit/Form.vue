<template>
  <div>
    <div v-if="!loading">
      <BaseField
        component="Select"
        label="Rezeptfilter"
        techName="mealType"
        v-model="state.mealType"
        :items="mealTypes"
        :errors="errors.mealType?.$errors"
      />
      <BaseField
        component="Select"
        label="Rezept"
        techName="recipe"
        :disabled="!state.mealType && !isEdit"
        v-model="state.recipe"
        :items="recipes"
        :errors="errors.recipe?.$errors"
      />
      <BaseField
        component="Number"
        label="Portion als Faktor"
        techName="factor"
        :disabled="!state.mealType && !isEdit"
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
    <LoadingItem v-else />
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
import LoadingItem from "@/components/list/LoadingItem.vue";

import { useIngredientStore } from "@/modules/ingredient/store/index";
import { useRecipeStore } from "@/modules/recipe/store/index";
import { useMealStore } from "@/modules/meal/store/index";

import { useVuelidate } from "@vuelidate/core";
import { required, email, minLength, maxLength } from "@vuelidate/validators";

const state = reactive({
  recipe: {
    name: "",
    id: 1,
  },
  factor: 1,
});

const rules = {
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

const loading = computed(() => {
  return isLoading.value;
});

const ingredientStore = useIngredientStore();
const recipeStore = useRecipeStore();
const mealStore = useMealStore();

const recipes = computed(() => {
  return recipeStore.recipes;
});

const isEdit = computed(() => {
  return !!props.items?.id;
});

const mealTypes = computed(() => {
  return mealStore.mealTypes;
});

function onDeleteClicked() {
  mealStore.deleteMealItem(props.items.id).then((response) => {
    let id = Number(route.params.id);
    let eventDayId = Number(route.params.eventDayId);
    goToRecipe("EventDay", {
      id,
      eventDayId,
    });
  });
}

watch(
  () => state.mealType,
  () => {
    if (state?.mealType?.value || isEdit.value) {
      updateData(state?.mealType?.value);
    }
  },
  { immediate: true, deep: true }
);

function onSaveClicked() {
  v$.value.$validate();
  errors.value = v$.value;
  if (errors.value.$error) {
    commonStore.showError("Bitte Felder überprüfen");
    return;
  }

  let id = Number(route.params.id);
  let eventDayId = Number(route.params.eventDayId);
  isLoading.value = true;
  // new
  if (!isEdit.value) {
    mealStore
      .createMealItem({
        meal: props.items?.meal.id,
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
        meal: props.items?.meal,
        recipe: state.recipe.id,
        factor: Number(state.factor),
      })
      .then((response2: any) => {
        goToRecipe("EventDay", {
          id,
          eventDayId,
        });
      });
  }
  isLoading.value = false;
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

async function updateData(mealType: any) {
  isLoading.value = true;
  let params = {};
  if (mealType) {
    params = {
      meal_type: mealType,
    };
  } else {
    state.mealType = mealTypes.value.filter(
      (item) => item.value === props.items?.recipe.mealType
    )[0];
    return;
  }
  await recipeStore.fetchRecipes(params);

  if (isEdit.value) {
    state.meal = props.items?.meal?.id;
    state.recipe = props.items?.recipe;
    state.factor = props.items?.factor;
  } else {
    state.meal = props.items?.meal?.id;
    state.recipe = null;
    state.factor = 1;
  }
  isLoading.value = false;
}

onMounted(async () => {
  isLoading.value = true;
  if (mealTypes.value.length === 0) {
    await mealStore.fetchMealTypes();
  }
  updateData(props.items?.meal.mealType);
});
</script>
