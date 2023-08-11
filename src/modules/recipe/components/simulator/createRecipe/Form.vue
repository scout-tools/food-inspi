<template>
  <div>
    <div v-if="!loading">
      <BaseField
        component="Text"
        label="Rezeptname"
        techName="name"
        v-model="state.name"
        :errors="errors.name?.$errors"
      />
      <BaseField
        component="TextArea"
        label="Kurzbeschreibung"
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
      <BaseField
        component="Select"
        v-model="state.status"
        techName="status"
        label="Status"
        :items="recipedStatuses"
        :errors="errors.status?.$errors"
      />
      <PrimaryButton
        @click="onSaveClicked"
        :label="isEdit ? 'speichern' : 'erstellen'"
      />
      <PrimaryButton
        v-if="isEdit"
        class="mx-2 my-2"
        @click="onDeleteClicked()"
        color="red"
        label="löschen"
      />
    </div>
    <LoadingItem v-else/>
  </div>
</template>

<script setup lang="ts">
import { useCommonStore } from "@/modules/common/store/index.ts";
import LoadingItem from "@/components/list/LoadingItem.vue";
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
  status: 1,
});

const rules = {
  name: {
    required,
  },
  mealType: {
    required,
  },
  status: {
    required,
  },
};

const props = defineProps({
  items: { type: Object, required: true },
});

const v$ = useVuelidate(rules, state);

const ingredient = ref(null);
const errors = ref([]);
const isLoading = ref(true);

const mealStore = useMealStore();
const recipeStore = useRecipeStore();

const isEdit = computed(() => {
  return !!props.items?.id;
});

const mealTypes = computed(() => {
  return mealStore.mealTypes;
});

const recipedStatuses = computed(() => {
  return mealStore.recipedStatuses;
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
      mealType: state.mealType?.value,
      status: state.status.value,
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
  if (router.currentRoute.value.name === "RecipeDetail") {
    router.go(router.currentRoute.value);
  }
}

import { useRoute } from "vue-router";
const route = useRoute();

import { useRouter } from "vue-router";
const router = useRouter();

const loading = computed(() => {
  return isLoading.value;
});

onMounted(async () => {
  isLoading.value = true;
  await Promise.all([
    mealStore.fetchMealTypes(),
    mealStore.fetchRecipeStatuses(),
  ]);
  if (isEdit.value) {
    isLoading.value = true;
    state.id = props.items?.id;
    state.name = props.items?.name;
    state.description = props.items?.description;
    state.mealType = mealTypes.value.filter(
      (item) => item.value === props.items?.mealType
    )[0];
    state.status = recipedStatuses.value.filter(
      (item) => item.value === props.items?.status
    )[0];
  } else {
    state.name = null;
    state.description = null;
    state.mealType = null;
    state.status = null;
  }
  isLoading.value = false;
});
</script>
