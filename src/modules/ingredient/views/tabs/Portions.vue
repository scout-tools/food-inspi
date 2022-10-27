<template>
  <TabPanel class="space-y-12 px-4 py-6">
    <div>
      <div class="mt-5 border-t border-gray-200">
        <div class="sm:flex sm:items-center">
          <div class="sm:flex-auto">
            <p class="mt-2 text-sm text-gray-700">
              A list of all the users in your account including their name,
              title, email and role.
            </p>
          </div>
          <div class="mt-4 sm:mt-0 sm:ml-16 sm:flex-none">
            <button
              type="button"
              class="
                inline-flex
                items-center
                justify-center
                rounded-md
                border border-transparent
                bg-blue-600
                px-4
                py-2
                text-sm
                font-medium
                text-white
                shadow-sm
                hover:bg-blue-700
                focus:outline-none
                focus:ring-2
                focus:ring-blue-500
                focus:ring-offset-2
                sm:w-auto
              "
            >
              Portion hinzufügen
            </button>
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
                        Name der Portion
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
                        Gewicht
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
                        Reihenfolge
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
                        Role
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
                    <tr v-for="person in portions" :key="person.email">
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
                        {{ person.name }}
                      </td>
                      <td
                        class="
                          whitespace-nowrap
                          px-3
                          py-4
                          text-sm text-gray-500
                        "
                      >
                        {{ person.weightG }} g
                      </td>
                      <td
                        class="
                          whitespace-nowrap
                          px-3
                          py-4
                          text-sm text-gray-500
                        "
                      >
                        {{ person.rank }}.
                      </td>
                      <td
                        class="
                          whitespace-nowrap
                          px-3
                          py-4
                          text-sm text-gray-500
                        "
                      >
                        {{ person.role }}
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
                        <a
                          href="#"
                          class="text-indigo-600 hover:text-indigo-900"
                          >Edit<span class="sr-only"
                            >, {{ person.name }}</span
                          ></a
                        >
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
  </TabPanel>
</template>


<script setup lang="ts">
import { ref } from "vue";
import { TabPanel } from "@headlessui/vue";
import { useRoute } from "vue-router";
import { onMounted, computed } from "vue";
//import users store
import { useIngredientStore } from "@/modules/ingredient/store/index.ts";

const route = useRoute();
const store = useIngredientStore();

const portions = computed(() => {
  return store.portions;
});
onMounted(() => {
  const id = route.params.id;
  store.fetchPortions({ ingredient__id: id });
});
</script>