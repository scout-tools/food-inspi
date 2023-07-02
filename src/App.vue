<template>
  <div class="flex h-full">
    <Banner />
    <LeftNav v-if="isKeycloakInit">
      <router-view />
    </LeftNav>
    <div v-else class="flex justify-center items-center w-full h-screen">
      <LoadingItem />
    </div>
    <Success />
    <Error />
  </div>
</template>

<script setup lang="ts">
import { useAuthStore } from "@/modules/auth/store/index";
import { computed, onUpdated, ref } from "vue";

import LeftNav from "@/modules/app/components/LeftNav.vue";
import Success from "@/modules/common/components/Success.vue";
import Error from "@/modules/common/components/Error.vue";
import LoadingItem from "@/components/list/LoadingItem.vue";

const authStore = useAuthStore();

const isKeycloakInit = computed(() => {
  return authStore.isKeycloakInit;
});

const isAuth = computed(() => {
  return authStore.isAuth;
});

import { usePersonalDataStore } from "@/modules/settings/store/personal-data";
const personalDataStore = usePersonalDataStore();

function getNotifications() {
  if (isAuth.value & isKeycloakInit.value) {
    personalDataStore.fetchPersonalData();
  }
}

onUpdated(() => {});
</script>
