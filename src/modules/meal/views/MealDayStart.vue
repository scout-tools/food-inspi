<template>
  <PageWrapper>
    <MyTabGroup :tabs="tabs" />
  </PageWrapper>
</template>

<script setup lang="ts">
import { computed } from "vue";
import { useRoute } from "vue-router";

import MyTabGroup from "@/components/menu/TabGroup.vue";
import PageWrapper from "@/components/base/PageWrapper.vue";

const route = useRoute();

const tabs = computed(() => {
  return [
    {
      name: "Meine Events",
      linkName: { name: "MyEvents", query: { meal_type: 'lunch_warm'} },
      current: route.name === "MyEvents",
    },
    {
      name: "Öffentliche Events",
      linkName: { name: "PublicEvents", query: { meal_type: 'lunch_warm'}  },
      current:
        route.name === "PublicEvents"
    },
    {
      name: "Referenz Events",
      linkName: { name: "ApprovedEvents", query: { meal_type: 'lunch_warm'}},
      current: route.name === "ApprovedEvents",
    },
  ];
});
</script>
