<template>
  <div class="text-center my-12">
    <div class="object-center sm:hidden">
      <router-link :to="{ name: 'SimulatorStart' }">
        <img
          class="h-40 mx-auto object-center w-auto"
          src="./../../../../assets/logo.png"
          alt="Food Inspi"
        />
      </router-link>
    </div>
    <svg
      class="mx-auto invisible sm:visible h-12 w-12 text-gray-400"
      fill="none"
      viewBox="0 0 24 24"
      stroke="currentColor"
      aria-hidden="true"
    >
      <path
        vector-effect="non-scaling-stroke"
        stroke-linecap="round"
        stroke-linejoin="round"
        stroke-width="2"
        d="M9 13h6m-3-3v6m-9 1V7a2 2 0 012-2h6l2 2h6a2 2 0 012 2v8a2 2 0 01-2 2H5a2 2 0 01-2-2z"
      />
    </svg>
    <h3 class="mt-2 text-sm font-medium text-gray-900">
      Erstelle dir hier einen Essensplan
    </h3>
    <p class="mt-1 text-sm text-gray-500">
      Füge jetzt deine Zutaten ein. Ich habe sicher einen Tipp für dich.
    </p>
    <div class="mt-6 mb-6">
      <button
        type="button"
        @click="onAddClicked"
        class="
          inline-flex
          items-center
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
        "
      >
        <PlusIcon class="-ml-1 mr-2 h-5 w-5" aria-hidden="true" />
        Neue Veranstaltung hinzufügen
      </button>
    </div>
    <div class="mt-8 flex flex-col">
      <div class="my-2 mx-4 overflow-x-auto sm:-mx-6 lg:-mx-8">
        <div class="inline-block min-w-full py-2 align-middle md:px-6 lg:px-8">
          <div
            class="
              overflow-hidden
              shadow
              ring-1 ring-black ring-opacity-5
              md:rounded-lg
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
                      text-left text-sm text-gray-900
                      sm:pl-6
                    "
                  >
                    Bestehende Veranstaltungen
                  </th>
                  <th scope="col" class="relative py-3.5 pl-3 pr-4 sm:pr-6">
                    <span class="sr-only"></span>
                  </th>
                </tr>
              </thead>
              <tbody
                v-if="events.length"
                class="divide-y divide-gray-200 bg-white"
              >
                <tr v-for="event in events" :key="event.id">
                  <td
                    class="
                      whitespace-nowrap
                      py-4
                      pl-4
                      pr-3
                      text-left text-sm
                      font-medium
                      text-gray-900
                      sm:pl-6
                    "
                  >
                    {{ event.name }}
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
                    "
                  >
                    <button
                      @click="onSimulateClicked(event.id)"
                      class="text-blue-600 hover:text-blue-900"
                    >
                      öffnen
                    </button>
                  </td>
                </tr>
              </tbody>
              <tbody v-else>
                <div role="status" class="px-3 py-3">
                  <svg
                    class="
                      inline
                      mr-2
                      w-8
                      h-8
                      text-gray-200
                      animate-spin
                      fill-blue-600
                    "
                    viewBox="0 0 100 101"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
                      fill="currentColor"
                    />
                    <path
                      d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
                      fill="currentFill"
                    />
                  </svg>
                  <span class="sr-only">Loading...</span>
                </div>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, computed } from "vue";
import { PlusIcon } from "@heroicons/vue/20/solid";
import { useMealStore } from "@/modules/meal/store/index";
import { useRouter } from "vue-router";

const router = useRouter();

const mealStore = useMealStore();

const events = computed(() => {
  return mealStore.events;
});
const emit = defineEmits(["onAddClicked"]);

const onAddClicked = () => {
  emit("onAddClicked");
};

async function onSimulateClicked(id) {
  router.push({
    name: "EventDefault",
    params: { id },
  });
}

onMounted(() => {
  mealStore.fetchEventsSmall();
});
</script>
