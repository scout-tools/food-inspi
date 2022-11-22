<template>
  <TabPanel class="space-y-12 px-4 py-3">
    <div>
      <div class="mt-5">
        <div
          class="
            px-4
            sm:flex sm:items-center sm:justify-between sm:px-6
            lg:px-8
          "
        >
          <div class="min-w-0 flex-1">
            <h3 class="text-lg font-medium text-gray-900">
              Preise von {{ ingredientDetail.name }}
            </h3>
            <p class="ml-3 max-w-2xl text-sm text-gray-500">
              Mögliche Auswahlen für eine Zutat
            </p>
          </div>
          <div class="mt-4 flex-2 sm:mt-0 sm:ml-4">
            <PrimaryButton
              color="blue"
              label="Preis hinzufügen"
              @click="onNewPortionClicked"
            />
          </div>
        </div>
        <div class="mt-8 flex flex-col">
          <div class="-my-2 -mx-4 overflow-x-auto sm:-mx-6 lg:-mx-8">
            <div class="inline-block min-w-full py-2 align-middle">
              <div
                class="
                  overflow-hidden
                  shadow-sm
                  ring-1 ring-black ring-opacity-5
                "
              >
                <table class="min-w-full divide-y divide-gray-300">
                  <thead class="bg-gray-50">
                    <tr>
                      <th
                        scope="col"
                        class="
                          py-3.5
                          pl-4
                          pr-3
                          text-left text-sm
                          font-semibold
                          text-gray-900
                          sm:pl-6
                          lg:pl-8
                        "
                      >
                        Name des Packets
                      </th>
                      <th
                        scope="col"
                        class="
                          px-3
                          py-3.5
                          text-left text-sm
                          font-semibold
                          text-gray-900
                        "
                      >
                        Preis
                      </th>
                      <th
                        scope="col"
                        class="
                          px-3
                          py-3.5
                          text-left text-sm
                          font-semibold
                          text-gray-900
                        "
                      >
                        Supermarkt
                      </th>
                      <th
                        scope="col"
                        class="relative py-3.5 pl-3 pr-4 sm:pr-6 lg:pr-8"
                      >
                        <span class="sr-only">Edit</span>
                      </th>
                    </tr>
                  </thead>
                  <tbody class="divide-y divide-gray-200 bg-white">
                    <tr v-for="item in prices" :key="item.id">
                      <td
                        class="
                          whitespace-nowrap
                          py-4
                          pl-4
                          pr-3
                          text-sm
                          font-medium
                          text-gray-900
                          sm:pl-6
                          lg:pl-8
                        "
                      >
                        {{ item.package.name }} ({{
                          item.package.portion.name
                        }})
                      </td>
                      <td
                        class="
                          whitespace-nowrap
                          px-3
                          py-4
                          text-sm text-gray-900
                        "
                      >
                        {{ item.priceEur }} € ({{ item.pricePerKg }} €/ Kg)
                      </td>
                      <td
                        class="
                          whitespace-nowrap
                          px-3
                          py-4
                          text-sm text-gray-900
                        "
                      >
                        {{ item.retailer.name }}
                      </td>
                      <td
                        class="
                          relative
                          whitespace-nowrap
                          py-4
                          pl-3
                          pr-4
                          text-right text-sm
                          font-medium
                          sm:pr-6
                          lg:pr-8
                        "
                      >
                        <button
                          @click="onDeleteClicked(item)"
                          class="text-red-600 hover:text-red-900"
                        >
                          löschen
                        </button>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <DeleteModal
      :open="openDeleteModal"
      :callbackOnConfirm="onDeletePriceConfirmed"
      :callbackOnCancel="cancelModal"
    />
  </TabPanel>
</template>


<script setup lang="ts">
import { ref } from "vue";
import { TabPanel } from "@headlessui/vue";
import { useRoute } from "vue-router";
import { useRouter } from "vue-router";
import { onMounted, computed } from "vue";
import { useIngredientStore } from "@/modules/ingredient/store/index.ts";
import PrimaryButton from "@/components/button/Primary.vue";
import DeleteModal from "@/components/modal/Delete.vue";
import { useCommonStore } from "@/modules/common/store/index.ts";
const commonStore = useCommonStore();

const route = useRoute();
const router = useRouter();
const store = useIngredientStore();

const prices = computed(() => {
  return store.prices;
});

const ingredientDetail = computed(() => {
  return store.ingredientDetail;
});

function onNewPortionClicked() {
  router.push({ name: "PriceCreate" });
}

const openDeleteModal = ref(false);
const selectedItem = ref();

function onDeleteClicked(item) {
  openDeleteModal.value = true;
  selectedItem.value = item;
}

function onDeletePriceConfirmed() {
  const id = selectedItem.value.id;
  store.deletePrice(id).then(() => {
    router.push({
      name: "IngredientPrices",
      params: {
        id,
      },
    });
    commonStore.showSuccess("Zutat erfolgreich gelöscht");
    openDeleteModal.value = false;
  });
}

function cancelModal() {
  openDeleteModal.value = false;
}

onMounted(() => {
  const id = route.params.id;
  store.fetchPrices({ package__portion__ingredient__id: id });
});
</script>