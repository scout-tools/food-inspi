<template>
  <div>
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
                  Alle Preise die zu dieser Zutat getragen sind.
                </h3>
                <p class="mt-1 text-sm text-gray-500"></p>
              </div>
              <div class="mt-6 grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-4">
                <Base
                  :cols="1"
                  v-if="!packagesEmpty"
                  component="Toggle"
                  techName="newPackage"
                  v-model="newPackage"
                  :label="'Bestehende Packung verwenden?'"
                />
                <Base
                  :cols="6"
                  component="Select"
                  techName="retailer"
                  v-model="priceState['retailer']"
                  label="Supermarkt"
                  :items="retailers"
                  hint="Wähle eine Hauptkategorie für deine Zutat."
                  :errors="errors.retailer && errors.retailer.$errors"
                />
                <Base
                  :cols="6"
                  v-if="newPackage && !packagesEmpty"
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

            <div v-if="!newPackage || packagesEmpty" class="pt-8">
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
                  :cols="6"
                  component="Text"
                  techName="name"
                  v-model="priceState['name']"
                  label="Name"
                  hint="Wähle eine Hauptkategorie für deine Zutat."
                  :errors="errors.name && errors.name.$errors"
                />
                <Base
                  :cols="6"
                  component="Select"
                  techName="portion"
                  v-model="priceState['portion']"
                  label="Portion"
                  :items="portions"
                  hint="Wähle eine Hauptkategorie für deine Zutat."
                  :errors="errors.portion && errors.portion.$errors"
                />
                <Base
                  :cols="6"
                  component="Number"
                  techName="quantity"
                  v-model="priceState['quantity']"
                  label="Anzahl"
                  hint="Wähle eine Hauptkategorie für deine Zutat."
                  :errors="errors.quantity && errors.quantity.$errors"
                />
              </div>
            </div>
            <div class="mt-6 grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-4">
              <Base
                class="mt-6"
                :cols="6"
                component="Currency"
                :label="'Preis'"
                techName="priceEur"
                v-model="priceState['priceEur']"
                :errors="errors.priceEur && errors.priceEur.$errors"
                hint="Preis für die Packung bei Rewe."
              />
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
import { required, maxValue, minValue } from "@vuelidate/validators";

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

const packagesEmpty = computed(() => {
  return !ingredientStore.packages?.length;
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
  priceEur: 1.99,
  retailer: null,
  package: null,
  name: "",
  portion: null,
  quality: "own",
  quantity: 1,
});

const newPackage = ref(false);
const errors = ref([]);
const isLoading = ref(false);

const rules = computed(() => {
  const localRules = {
    retailer: { required },
    priceEur: {
      required,
      minValue: minValue(0.01),
      maxValue: maxValue(10000),
     },
  };
  debugger;
  if (newPackage.value === false) {
    debugger;
    // if billing is not the same as shipping, require it
    localRules.quantity = {
      required,
    };
    localRules.name = {
      required,
    };
  } else {
    debugger;
    localRules.package = {
      required,
    };
  }
  return localRules;
});

const v$ = useVuelidate(rules, priceState);

const ingredientStore = useIngredientStore();

const router = useRouter();

import { useCommonStore } from "@/modules/common/store/index";
const commonStore = useCommonStore();

function onButtonClicked() {
  v$.value.$validate();
  errors.value = v$.value;
  debugger;
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
        commonStore.showSuccess("Preis erfolgreich hinzugefügt");
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

  ingredientStore.fetchPackages({ portion__ingredient__id: id });
  ingredientStore.fetchPortions({ ingredient__id: id });
  ingredientStore.fetchRetailers();
});
</script>
