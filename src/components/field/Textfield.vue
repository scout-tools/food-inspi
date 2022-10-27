<template>
  <div class="mt-6 grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-6">
    <div class="sm:col-span-3">
      <label
        for="first-name"
        class="block text-sm font-medium text-gray-700"
        >First name</label
      >
      <div class="mt-1">
        <input
          type="text"
          name="first-name"
          id="first-name"
          autocomplete="given-name"
          class="
            block
            w-full
            rounded-md
            border-gray-300
            shadow-sm
            focus:border-indigo-500 focus:ring-indigo-500
            sm:text-sm
          "
        />
      </div>
    </div>
</template>

<script setup lang="ts">
</script>

<style>
</style>