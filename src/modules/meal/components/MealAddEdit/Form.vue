<template>
  <div>
    <BaseField
      component="Text"
      label="Name des Essens"
      techName="name"
      v-model="state.name"
      :errors="errors.name?.$errors"
    />
    <BaseField
      component="Number"
      label="Tagesaktor"
      techName="factor"
      v-model="state.factor"
      :errors="errors.factor?.$errors"
    />
    <BaseField
      component="Select"
      v-model="state.mealType"
      techName="mealType"
      label="Essens Typ"
      :items="mealTypes"
      :errors="errors.mealType?.$errors"
    />
    <PrimaryButton
      @click="onSaveClicked"
      :label="!isEdit ? 'Menu hinzufügen' : 'Menu bearbeiten'"
    />
    <PrimaryButton
      v-if="isEdit"
      class="mx-2 my-2"
      @click="onDeleteClicked()"
      color="red"
      label="Menu löschen"
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
  name: 'Test',
  mealDay: 1,
  mealType: {
    value: 'test',
  },
  factor: 0.33,
});


const rules = {
  name: {
    required,
  },
  factor: {
    required,
  },
  mealType: {
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

const ingredients = computed(() => {
  return ingredientStore.ingredients;
});

const mealTypes = computed(() => {
  return mealStore.mealTypes;
});

const isEdit = computed(() => {
  return !!props.items?.id
});


function onDeleteClicked() {
  let id = Number(route.params.id);
  let eventDayId = Number(route.params.eventDayId);

  mealStore.deleteMeal(props.items.id).then((response) => {
        goToRecipe("EventDay", {
          id,
          eventDayId,
        });
  });
}

watch(ingredientStore, (items) => {
  if (items && items.portions && items.portions.length) {
    if (props.reciptItem?.portion?.id) {
      state.portion = items.portions.filter(
        (item) => item.id === props.reciptItem.portion.id
      )[0];
    } else {
      state.portion = items.portions[0];
    }
  }
});

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
      .createMeal({
        name: state.name,
        mealDay: eventDayId,
        factor: state.factor,
        mealType: state.mealType?.value,
      })
      .then((response3: any) => {
        goToRecipe("EventDay", {
          id,
          eventDayId: response3.data.mealDay
        });
      });
  }
  // edit
  if (isEdit.value) {
    mealStore
      .updateMeal({
        id: props.items?.id,
        name: state.name,
        mealDay: eventDayId,
        factor: state.factor,
        mealType: state.mealType?.value,
      })
      .then((response2: any) => {
        goToRecipe("EventDay", {
          id,
          eventDayId: response2.data.mealDay
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
  setTimeout(function () {
    if (isEdit.value) {
      state.name = props.items?.name;
      state.mealDay = props.items?.mealDay;
      state.factor = props.items?.factor;
      state.mealType = mealTypes.value.filter(item => item.value === props.items?.mealType)[0];
    } else {
      state.name = '';
      state.mealDay = 1;
      state.factor = 0.33;
      state.mealType = mealTypes[0]
    }
  }, 300);
});
</script>
