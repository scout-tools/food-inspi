<template>
  <div>
    <Breadcrumbs :pages="pages" />
    <main
      class="
        relative
        h-screen
        z-40
        flex-1
        focus:outline-none
        overflow-y-auto
        pb-12
      "
    >
      <article class="flex-shrink-0 border border-gray-200 ma-12">
        <form class="space-y-8 divide-y px-3 py-4 divide-gray-200">
          <div class="space-y-8 divide-y divide-gray-200">
            <h2 class="text-h1 font-medium text-gray-900">Preis anlegen</h2>
            <div class="pt-8">
              <div>
                <h3 class="text-lg font-medium leading-6 text-gray-900">
                  Eckdaten
                </h3>
                <p class="mt-1 text-sm text-gray-500">
                  Daten die über jede Zutat bekannt sein müssen
                </p>
              </div>
              <div class="mt-6 grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-4">
                <Base
                  :cols="6"
                  component="Select"
                  techName="measuringUnit"
                  v-model="state['measuringUnit']"
                  label="Messeinheit"
                  :items="measuringUnits"
                  hint="Wähle die Messeinheit aus."
                  :errors="errors.measuringUnit && errors.measuringUnit.$errors"
                />
                <Base
                  :cols="6"
                  component="Number"
                  techName="quantity"
                  v-model="state['quantity']"
                  :label="'Anzahl'"
                  hint="Wähle die Anzahl der Maßheit aus, die eine Portion sein soll."
                  :errors="errors.quantity && errors.quantity.$errors"
                />
                <Base
                  :cols="6"
                  component="Text"
                  techName="name"
                  v-model="state['name']"
                  :label="'Name (optional)'"
                  hint="Wähle einen Portionsnamen aus. Sonst wird der generiert."
                  :errors="errors.name && errors.name.$errors"
                />
              </div>
            </div>
          </div>

          <div class="pt-5 pb-12">
            <div class="flex justify-end">
              <PrimaryButton
                @click="onButtonClicked"
                label="Speichern"
                :isLoading="isLoading"
              />
            </div>
          </div>
        </form>
      </article>
    </main>
  </div>
</template>


<script setup lang="ts">
import { computed, reactive, onMounted, ref } from "vue";
import Base from "@/components/field/Base.vue";
import Breadcrumbs from "@/components/breadcrumbs/Header.vue";
import PrimaryButton from "@/components/button/Primary.vue";
import Success from "@/modules/common/components/Success.vue";
import { useIngredientStore } from "@/modules/ingredient/store/index.ts";

import { useVuelidate } from "@vuelidate/core";
import { required, email, minLength, maxLength } from "@vuelidate/validators";

import { useRoute, useRouter } from "vue-router";

const route = useRoute();

const pages = computed(() => {
  return [
    { name: "Zutaten", link: "IngredientMain", current: false },
    {
      name: "Neue Zutat",
      link: `IngredientCreate`,
      current: true,
    },
  ];
});

const ingredientStore = useIngredientStore();

const ingredientDetail = computed(() => {
  return ingredientStore.ingredientDetail;
});

const measuringUnits = computed(() => {
  return ingredientStore.measuringUnits;
});

const retailers = computed(() => {
  return ingredientStore.retailers;
});

const state = reactive({
  ingredient: ingredientDetail.value.id,
  measuringUnit: 1,
  quantity: 1,
  name: null,
});

const rules = {
  ingredient: {
    required,
  },
  measuringUnit: {
    required,
  },
  quantity: {
    required,
  },
};

const v$ = useVuelidate(rules, state);

const newPortion = ref(true);
const errors = ref([]);
const isLoading = ref(false);



const router = useRouter();

import { useCommonStore } from "@/modules/common/store/index";
const commonStore = useCommonStore();

function onButtonClicked() {
  v$.value.$validate();
  errors.value = v$.value;
  if (errors.value.$error) {
    commonStore.showError("Bitte Felder überprüfen");
    return;
  }
  isLoading.value = true;
  ingredientStore
    .createPortion(state)
    .then((response) => {
      if (response && response.status === 201) {
        router.push({
          name: "IngredientPortions",
          params: { id: route.params.id },
        });
        commonStore.showSuccess("Zutat erfolgreich angelegt");
      } else if (response && response.status === 400) {
        commonStore.showSuccess(`Die Anfrage ist Fehlerhaft.${response.data}`);
      } else {
        console.log(response);
      }
    })
    .finally(() => {
      isLoading.value = false;
    });
}

onMounted(() => {
  const id = route.params.id;
  ingredientStore.fetchIngredientById(id)
  ingredientStore.fetchMeasuringUnit();
});
</script>
