<template>
  <div>
    <BaseField
      component="Select"
      techName="measuringUnit"
      v-model="state['measuringUnit']"
      label="Messeinheit"
      :items="measuringUnits"
      hint="Wähle die Messeinheit aus."
      :errors="errors.measuringUnit && errors.measuringUnit.$errors"
    />
    <BaseField
      component="Number"
      techName="quantity"
      v-model="state['quantity']"
      :label="'Anzahl'"
      hint="Wähle die Anzahl der Maßheit aus, die eine Portion sein soll."
      :errors="errors.quantity && errors.quantity.$errors"
    />
    <BaseField
      component="Number"
      techName="rank"
      v-model="state['rank']"
      :label="'Rangfolge'"
      hint="Wähle die Rangfolge/Relevanz dieser Prioität in der Liste."
      :errors="errors.rank && errors.rank.$errors"
    />
    <BaseField
      component="Text"
      techName="name"
      v-model="state['name']"
      :label="'Name (optional)'"
      hint="Wähle einen Portionsnamen aus. Sonst wird der generiert."
      :errors="errors.name && errors.name.$errors"
    />
    <PrimaryButton
      class="mx-0 my-2"
      @click="onSaveClicked"
      label="Portion speichern"
      :isLoading="isLoading"
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
import { useRecipeStore } from "@/modules/recipe/store/index.ts";
import { useIngredientStore } from "@/modules/ingredient/store/index.ts";

import { useVuelidate } from "@vuelidate/core";
import { required, email, minLength, maxLength } from "@vuelidate/validators";

const state = reactive({
  measuringUnit: 1,
  quantity: 1,
  name: null,
  rank: 1,
});

const rules = {
  measuringUnit: {
    required,
  },
  quantity: {
    required,
  },
  rank: {
    required,
  },
};

const v$ = useVuelidate(rules, state);

const errors = ref([]);
const isLoading = ref(false);

const recipeStore = useRecipeStore();
const ingredientStore = useIngredientStore();

function onSaveClicked() {
  v$.value.$validate();
  errors.value = v$.value;
  if (errors.value.$error) {
    commonStore.showError("Bitte Felder überprüfen");
    return;
  }
  ingredientStore
    .updatePortion({
      id: props.items.id,
      ingredient: props.items.ingredient.id,
      measuringUnit: state.measuringUnit.id,
      quantity: state.quantity,
      name: state.name,
      rank: state.rank,
    })
    .then((response2: any) => {
      goToRecipe(props.items.ingredient.id);
    });
}

function goToRecipe(id: number) {
  router.push({
    name: "IngredientPortions",
    params: {
      id,
    },
  });
  router.go(router.currentRoute.value);
}

import { useRoute } from "vue-router";
const route = useRoute();

import { useRouter } from "vue-router";
const router = useRouter();

const props = defineProps({
  items: { type: Object, required: true },
});

onMounted(async () => {
  console.log("props", props);
  state.ingredient = props.items.ingredient.id;
  state.measuringUnit = props.items.measuringUnit;
  state.quantity = props.items.quantity;
  state.name = props.items.name;
  state.rank = props.items.rank;
});
</script>
