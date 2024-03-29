<template>
  <TabPanel class="space-y-12 px-4 py-3">
    <div>
      <div class="mt-5">
        <div
          class="px-4 sm:flex sm:items-center sm:justify-between sm:px-6 lg:px-8"
        >
          <div class="min-w-0 flex-1">
            <h3 class="text-lg font-medium text-gray-900">
              Portionen von {{ ingredientDetail.name }}
            </h3>
            <p class="ml-3 max-w-2xl text-sm text-gray-500">
              Mögliche Auswahlen für eine Zutat
            </p>
          </div>
          <div class="mt-4 flex-2 sm:mt-0 sm:ml-4">
            <PrimaryButton
              color="blue"
              label="Portion hinzufügen"
              @click="onNewPortionClicked"
            />
          </div>
        </div>
        <div class="mt-8 flex flex-col">
          <div class="-my-2 -mx-4 overflow-x-auto sm:-mx-6 lg:-mx-8">
            <div class="inline-block min-w-full py-2 align-middle">
              <div
                class="overflow-hidden shadow-sm ring-1 ring-black ring-opacity-5"
              >
                <table class="min-w-full divide-y divide-gray-300">
                  <thead class="bg-gray-50">
                    <tr>
                      <th
                        scope="col"
                        class="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-6 lg:pl-8"
                      >
                        Name der Portion
                      </th>
                      <th
                        scope="col"
                        class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900"
                      >
                        Gewicht
                      </th>
                      <th
                        scope="col"
                        class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900"
                      >
                        Prioität
                      </th>
                      <th
                        scope="col"
                        class="relative py-3.5 pl-3 pr-4 sm:pr-6 lg:pr-8"
                      >
                        <span class="sr-only">Edit</span>
                      </th>
                    </tr>
                  </thead>
                  <tbody
                    v-if="portions && portions.length"
                    class="divide-y divide-gray-200 bg-white"
                  >
                    <tr v-for="portion in portions" :key="portion.id">
                      <td
                        class="whitespace-nowrap py-4 pl-4 pr-3 text-sm font-medium text-gray-900 sm:pl-6 lg:pl-8"
                      >
                        {{ portion.name }}
                      </td>
                      <td
                        class="whitespace-nowrap px-3 py-4 text-sm text-gray-500"
                      >
                        {{ portion.weightG }} g
                      </td>
                      <td
                        class="whitespace-nowrap px-3 py-4 text-sm text-gray-500"
                      >
                        {{ portion.rank }}.
                      </td>
                      <td
                        class="relative whitespace-nowrap py-4 pl-3 pr-4 text-right text-sm font-medium sm:pr-6 lg:pr-8"
                      >
                        <button
                          @click="onEditClicked(portion)"
                          class="text-blue-600 hover:text-blue-900"
                        >
                          bearbeiten
                        </button>
                      </td>
                      <td
                        class="relative whitespace-nowrap py-4 pl-3 pr-4 text-right text-sm font-medium sm:pr-6 lg:pr-8"
                      >
                        <button
                          @click="onDeleteClicked(portion)"
                          class="text-red-600 hover:text-red-900"
                        >
                          löschen
                        </button>
                      </td>
                    </tr>
                  </tbody>
                  <LoadingItem v-else />
                </table>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <DeleteModal
      :open="openDeleteModal"
      :callbackOnConfirm="deletePortion"
      :callbackOnCancel="cancelModal"
    />
    <PortionEditForm
      :open="openPortionEditForm"
      @close="onPortionEditFormClosed"
      :items="selectedItem"
    />
  </TabPanel>
</template>


<script setup lang="ts">
import { ref } from "vue";
import { TabPanel } from "@headlessui/vue";
import { useRoute, useRouter } from "vue-router";
import { onMounted, computed } from "vue";
import { useIngredientStore } from "@/modules/ingredient/store/index.ts";
import PrimaryButton from "@/components/button/Primary.vue";
import DeleteModal from "@/components/modal/Delete.vue";
import PortionEditForm from "@/modules/ingredient/components/portionEdit/PortionEditForm.vue";
import LoadingItem from "@/components/list/LoadingItem.vue";

const route = useRoute();
const router = useRouter();
const store = useIngredientStore();

const portions = computed(() => {
  return store.portions;
});

const ingredientDetail = computed(() => {
  return store.ingredientDetail;
});

function onNewPortionClicked() {
  router.push({ name: "PortionCreate" });
}

const openDeleteModal = ref(false);
const openPortionEditForm = ref(false);

const selectedItem = ref({});

function onDeleteClicked(portion: object) {
  openDeleteModal.value = true;
  selectedItem.value = portion;
}

import { useCommonStore } from "@/modules/common/store/index.ts";
const commonStore = useCommonStore();

function deletePortion() {
  store.deletePortion(selectedItem.value).then(() => {
    router.go(router.currentRoute);
  });
}

function onEditClicked(portion: object) {
  selectedItem.value = portion;
  openPortionEditForm.value = true;
}

function onPortionEditFormClosed() {
  openPortionEditForm.value = false;
}

function cancelModal() {
  openDeleteModal.value = false;
}

onMounted(() => {
  const id = route.params.id;
  store.fetchPortions({ ingredient__id: id });
});
</script>