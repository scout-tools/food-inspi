<template>
  <div class="flex min-w-0 flex-1 items-center">
    <div class="flex min-w-0 flex-1 items-center">
      <div class="min-w-0 flex-1 px-4 md:grid md:grid-cols-2 md:gap-4">
        <div>
          <p class="truncate text-sm font-medium text-blue-600">
            Fahrtenname: {{ props.item?.event?.name }}
          </p>
          <p class="mt-2 flex items-center text-sm text-gray-500">
            <TagIcon
              class="mr-1.5 h-5 w-5 flex-shrink-0 text-gray-400"
              aria-hidden="true"
            />
            <span class="truncate">{{
              props.item?.description || "Keine Beschreibung"
            }}</span>
          </p>
        </div>
        <div class="hidden md:block">
          <div>
            <p class="mt-1 flex items-center text-sm text-gray-500">
              <NutriSlim :nutriClass="props.item.nutriClass" />
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import {
  ClipboardIcon,
  RocketLaunchIcon,
  CheckCircleIcon,
  TagIcon,
} from "@heroicons/vue/24/outline";
import moment from "moment";
const props = defineProps({
  item: Object,
});
</script>
