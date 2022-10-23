<template>
  <div class="flex h-full">
    <LeftNav>
      <router-view />
    </LeftNav>
  </div>
</template>

<script setup lang="ts">
import LeftNav from "@/modules/nav/components/LeftNav.vue";
</script>