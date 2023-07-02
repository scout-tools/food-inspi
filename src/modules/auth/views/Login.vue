<template>
  <PageWrapper>
    <PrimaryButton @click="onLoginclicked">Mit DPV Account einloggen</PrimaryButton>
  </PageWrapper>
</template>

<script setup>
import PageWrapper from "@/components/base/PageWrapper.vue";
import PrimaryButton from "@/components/button/Primary.vue"

import { useAuthStore } from "@/modules/auth/store/index";
const authStore = useAuthStore();

function onLoginclicked() {
	authStore.login()
}
</script>
