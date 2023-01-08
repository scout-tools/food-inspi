<template>
  <div>
    <BaseField
      component="Text"
      label="Name"
      techName="name"
      v-model="state.name"
      :errors="errors.name?.$errors"
    />
    <BaseField
      component="TextArea"
      label="Beschreibung"
      techName="description"
      v-model="state.description"
      :errors="errors.description?.$errors"
    />
    <BaseField
      component="Select"
      v-model="state.mealType"
      techName="mealType"
      label="Essens Typ"
      :items="mealTypes"
      :errors="errors.mealType?.$errors"
    />
    <PrimaryButton @click="onSaveClicked" :label="'Veranst. hinzufügen'" />
    <PrimaryButton
      v-if="isEdit"
      class="mx-2 my-2"
      @click="onDeleteClicked()"
      color="red"
      label="Veranst löschen"
    />
  </div>
</template>

<script setup lang="ts">
import { useCommonStore } from "@/modules/common/store/index.ts";
const commonStore = useCommonStore();

import { reactive, onMounted, ref, watch, computed } from "vue";
import BaseField from "@/components/field/Base.vue";
import Select from "@/components/field/Select.vue";
import PrimaryButton from "@/components/button/Primary.vue";
import { useIngredientStore } from "@/modules/ingredient/store/index";
import { useRecipeStore } from "@/modules/recipe/store/index";
import { useMealStore } from "@/modules/meal/store/index";

import { useVuelidate } from "@vuelidate/core";
import { required, email, minLength, maxLength } from "@vuelidate/validators";

const state = reactive({
  id: null,
  name: "",
  description: "",
  mealType: 1,
});

const rules = {
  name: {
    required,
  },
  description: {
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

const mealStore = useMealStore();
const recipeStore = useRecipeStore();

const isEdit = computed(() => {
  return !!props.items?.id;
});

const mealTypes = computed(() => {
  return mealStore.mealTypes;
});

function onDeleteClicked() {
  mealStore.deleteEvent(props.items).then((response) => {
    router.push({
      name: "MealDayStart",
    });
  });
}

function onSaveClicked() {
  v$.value.$validate();
  errors.value = v$.value;
  if (errors.value.$error) {
    commonStore.showError("Bitte Felder überprüfen");
    return;
  }
  recipeStore
    .updateRecipe({
      id: state.id,
      name: state.name,
      description: state.description,
      mealType: state.mealType?.id,
      status: 'user_public'
    })
    .then((response: any) => {
      goToRecipe(response.data.id);
    });
}

function goToRecipe(id: number) {
  router.push({
    name: "RecipeDetail",
    params: {
      id: id,
    },
  });
}

import { useRoute } from "vue-router";
const route = useRoute();

import { useRouter } from "vue-router";
const router = useRouter();

onMounted(() => {
  mealStore.fetchMealTypes();
  setTimeout(function () {
    if (isEdit.value) {
      state.id = props.items?.id;
      state.name = props.items?.name;
      state.description = props.items?.description;
      state.mealType = mealTypes.value.filter(
        (item) => item.id === props.items?.mealType
      )[0];
    } else {
      state.name = null;
      state.description = null;
      state.mealType = null;
    }
  }, 300);
});
</script>
