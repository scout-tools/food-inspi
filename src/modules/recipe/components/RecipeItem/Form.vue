<template>
  <div>
    <div>
      <BaseField
        v-if="!isEdit"
        component="AutoComplete"
        label="Zutat"
        techName="ingredient"
        v-model="ingredient"
        :items="ingredients"
        :errors="errors.ingredient?.$errors"
      />
      <h3 class="my-4" v-else>{{ ingredient?.name }}</h3>
      <BaseField
        v-if="!isLoading && ingredient && ingredient.id"
        component="Select"
        v-model="state.portion"
        techName="portion"
        :disabled="!ingredient"
        label="Portion"
        :items="portions"
        :errors="errors.portion?.$errors"
      />
      <BaseField
      v-if="!isLoading && ingredient && ingredient.id"
        component="Number"
        :label="`Anzahl von ${state.portion?.name}`"
        techName="quantity"
        v-model="state.quantity"
        :errors="errors.quantity?.$errors"
      />
      <div v-if="isLoading">
        <LoadingItem />
      </div>
      <PrimaryButton
        class="mx-0 my-2"
        @click="onSaveClicked"
        :label="!isEdit ? 'Zutat hinzufügen' : 'Zutat bearbeiten'"
        :isLoading="isLoading"
      />
      <PrimaryButton
        v-if="isEdit"
        class="mx-2 my-2"
        @click="onDeleteClicked()"
        color="red"
        label="Zutat löschen"
        :isLoading="isLoading"
      />
    </div>
    <!-- <div v-else>
      <LoadingItem />
    </div> -->
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
import { useIngredientStore } from "@/modules/ingredient/store/index.ts";
import { useRecipeStore } from "@/modules/recipe/store/index.ts";
import { debounce } from "lodash";

import { useVuelidate } from "@vuelidate/core";
import { required, email, minLength, maxLength } from "@vuelidate/validators";

const state = reactive({
  portion: null,
  quantity: 1,
});

const rules = {
  portion: {
    required,
  },
  quantity: {
    required,
  },
};

const props = defineProps({
  reciptItem: { type: Object, required: true },
});

const v$ = useVuelidate(rules, state);

const ingredient = ref(null);
const errors = ref([]);
const isLoading = ref(false);

const ingredientStore = useIngredientStore();
const recipeStore = useRecipeStore();

const ingredients = computed(() => {
  return ingredientStore.ingredients;
});

watch(ingredient, (value) => {
  isLoading.value = true;
  if (value?.id) {
    search(value);
  }

});

const portions = computed(() => {
  return ingredientStore.portions;
});

const isEdit = computed(() => {
  return !!props.reciptItem?.portion?.id;
});

watch(ingredientStore, (items) => {
  isLoading.value = true;
  if (items && items.portions && items.portions.length) {
    if (props.reciptItem?.portion?.id) {
      state.portion = items.portions.filter(
        (item) => item.id === props.reciptItem.portion.id
      )[0];
    } else {
      state.portion = items.portions[0];
    }
  }
  isLoading.value = false;
});

const search = debounce(async (value) => {
  isLoading.value = true;
  ingredientStore.fetchPortions({ ingredient__id: value?.id });
  isLoading.value = false;
}, 1000);

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
  // new
  if (isNaN(recipeId) || route.name === "SimulatorStart") {
    recipeStore.createRecipe({}).then((response: any) => {
      recipeId = response.data.id;
      recipeStore
        .createRecipeItem({
          recipe: recipeId,
          portion: state.portion?.id,
          quantity: state.quantity,
        })
        .then((response2: any) => {
          recipeStore.updateRecipeItem({
            id: response2.data.id,
            recipe: response2.data.recipe,
            portion: response2.data.portion,
            quantity: response2.data.quantity,
          });
        })
        .then((response4: any) => {
          goToRecipe(recipeId);
        });
    });
  }
  // new
  if (
    !isNaN(recipeId) &&
    (route.name === "SimulatorMain" || route.name === "RecipeDetail") &&
    !isEdit.value
  ) {
    recipeStore
      .createRecipeItem({
        recipe: recipeId,
        portion: state.portion?.id,
        quantity: state.quantity,
      })
      .then((response2: any) => {
        recipeStore.updateRecipeItem({
          id: response2.data.id,
          recipe: response2.data.recipe,
          portion: response2.data.portion,
          quantity: response2.data.quantity,
        });
      })
      .then((response3: any) => {
        goToRecipe(recipeId, route.name === "SimulatorMain");
      });
  }
  // edit
  if (
    !isNaN(recipeId) &&
    (route.name === "SimulatorMain" || route.name === "RecipeDetail") &&
    isEdit.value
  ) {
    recipeStore
      .updateRecipeItem({
        id: props.reciptItem?.id,
        recipe: recipeId,
        portion: state.portion?.id,
        quantity: state.quantity,
      })
      .then((response2: any) => {
        recipeStore.updateRecipeItem({
          id: response2.data.id,
          recipe: response2.data.recipe,
          portion: response2.data.portion,
          quantity: response2.data.quantity,
        });
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

onMounted(async () => {
  if (isEdit.value) {
    ingredient.value = props.reciptItem?.portion?.ingredient;
    state.quantity = props.reciptItem?.quantity;
    state.portion = props.reciptItem?.portion.id;
  } else {
    state.portion = null;
    state.quantity = 1;
  }
  await ingredientStore.fetchIngredients();

  isLoading.value = false;
});
</script>
