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
                  component="Toggle"
                  techName="newPortion"
                  v-model="newPortion"
                  :label="'Bestehende Packung verwenden?'"
                />
                <Base
                  component="Select"
                  techName="retailer"
                  v-model="priceState['retailer']"
                  label="Supermarkt"
                  :items="retailers"
                  hint="Wähle eine Hauptkategorie für deine Zutat."
                  :errors="errors.retailer && errors.retailer.$errors"
                />
                <Base
                  v-if="newPortion"
                  component="Select"
                  techName="Packung"
                  v-model="priceState['package']"
                  :label="'Packung'"
                  :items="packages"
                  hint="Wähle hier eine Packung aus, falls eine existiert."
                  :errors="errors.package && errors.package.$errors"
                />
              </div>
            </div>

            <div v-if="!newPortion" class="pt-8">
              <div>
                <h3 class="text-lg font-medium leading-6 text-gray-900">
                  Neue Verpackung
                </h3>
                <p class="mt-1 text-sm text-gray-500">
                  Wenn nötig kannst du eine neue Verpackung anlegen.
                </p>
              </div>
              <div class="mt-6 grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-4">
                <Base
                  component="Text"
                  techName="name"
                  v-model="priceState['name']"
                  label="Name"
                  hint="Wähle eine Hauptkategorie für deine Zutat."
                  :errors="errors.name && errors.name.$errors"
                />
                <Base
                  component="Select"
                  techName="portion"
                  v-model="priceState['portion']"
                  label="Portion"
                  :items="portions"
                  hint="Wähle eine Hauptkategorie für deine Zutat."
                  :errors="errors.portion && errors.portion.$errors"
                />
                <Base
                  component="Number"
                  techName="quantity"
                  v-model="priceState['quantity']"
                  label="Anzahl"
                  hint="Wähle eine Hauptkategorie für deine Zutat."
                  :errors="errors.quantity && errors.quantity.$errors"
                />
              </div>
            </div>
            <Base
              component="Number"
              :label="'Preis'"
              techName="priceEur"
              v-model="priceState['priceEur']"
              :errors="errors.priceEur && errors.priceEur.$errors"
              hint="Preis für die Packung bei Rewe."
            />
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

const packages = computed(() => {
  return ingredientStore.packages;
});

const portions = computed(() => {
  return ingredientStore.portions;
});

const retailers = computed(() => {
  return ingredientStore.retailers;
});

const priceState = reactive({
  price_eur: 0,
  retailer: null,
  package: null,
  name: "",
  portion: null,
  quality: "own",
  quantity: 1,
});


const rules = {
  price_eur: {
    required,
  },
};

const v$ = useVuelidate(rules, priceState);

const newPortion = ref(true);
const errors = ref([]);
const isLoading = ref(false);

const ingredientStore = useIngredientStore();

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
    .createPrice(priceState)
    .then((response) => {
      if (response && response.status === 201) {
        router.push({
          name: "IngredientPrices",
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

  ingredientStore.fetchPackages({ portion__ingredient__id: id});
  ingredientStore.fetchPortions({ ingredient__id: id });
  ingredientStore.fetchRetailers();
});
</script>
