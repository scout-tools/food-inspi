<template>
  <main
    class="relative h-screen z-40 flex-1 focus:outline-none overflow-y-auto"
  >
    <article class="flex-shrink-0 border border-gray-200 ma-12">
      <form class="space-y-8 divide-y px-3 py-4 divide-gray-200 xl:px-64">
        <div class="space-y-8 divide-y divide-gray-200">
          <h2 class="text-h1 font-medium text-gray-900">Zutaten</h2>
          <div class="pt-8">
            <div>
              <h3 class="text-lg font-medium leading-6 text-gray-900">
                Eckdaten
              </h3>
              <p class="mt-1 text-sm text-gray-500">
                Daten die über jede Zutat bekannt sein müssen
              </p>
            </div>
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

              <div class="sm:col-span-3">
                <label
                  for="last-name"
                  class="block text-sm font-medium text-gray-700"
                  >Last name</label
                >
                <div class="mt-1">
                  <input
                    type="text"
                    name="last-name"
                    id="last-name"
                    autocomplete="family-name"
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

              <div class="sm:col-span-4">
                <label
                  for="email"
                  class="block text-sm font-medium text-gray-700"
                  >Email address</label
                >
                <div class="mt-1">
                  <input
                    id="email"
                    name="email"
                    type="email"
                    autocomplete="email"
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

              <div class="sm:col-span-3">
                <label
                  for="country"
                  class="block text-sm font-medium text-gray-700"
                  >Country</label
                >
                <div class="mt-1">
                  <select
                    id="country"
                    name="country"
                    autocomplete="country-name"
                    class="
                      block
                      w-full
                      rounded-md
                      border-gray-300
                      shadow-sm
                      focus:border-indigo-500 focus:ring-indigo-500
                      sm:text-sm
                    "
                  >
                    <option>United States</option>
                    <option>Canada</option>
                    <option>Mexico</option>
                  </select>
                </div>
              </div>

              <div class="sm:col-span-6">
                <label
                  for="street-address"
                  class="block text-sm font-medium text-gray-700"
                  >Street address</label
                >
                <div class="mt-1">
                  <input
                    type="text"
                    name="street-address"
                    id="street-address"
                    autocomplete="street-address"
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

              <div class="sm:col-span-2">
                <label
                  for="city"
                  class="block text-sm font-medium text-gray-700"
                  >City</label
                >
                <div class="mt-1">
                  <input
                    type="text"
                    name="city"
                    id="city"
                    autocomplete="address-level2"
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

              <div class="sm:col-span-2">
                <label
                  for="region"
                  class="block text-sm font-medium text-gray-700"
                  >State / Province</label
                >
                <div class="mt-1">
                  <input
                    type="text"
                    name="region"
                    id="region"
                    autocomplete="address-level1"
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

              <div class="sm:col-span-2">
                <label
                  for="postal-code"
                  class="block text-sm font-medium text-gray-700"
                  >ZIP / Postal code</label
                >
                <div class="mt-1">
                  <input
                    type="text"
                    name="postal-code"
                    id="postal-code"
                    autocomplete="postal-code"
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
            </div>
          </div>

          <div class="pt-8">
            <div>
              <h3 class="text-lg font-medium leading-6 text-gray-900">
                Notifications
              </h3>
              <p class="mt-1 text-sm text-gray-500">
                We'll always let you know about important changes, but you pick
                what else you want to hear about.
              </p>
            </div>
            <div class="mt-6">
              <fieldset>
                <legend class="sr-only">By Email</legend>
                <div
                  class="text-base font-medium text-gray-900"
                  aria-hidden="true"
                >
                  By Email
                </div>
                <div class="mt-4 space-y-4">
                  <div class="relative flex items-start">
                    <div class="flex h-5 items-center">
                      <input
                        id="comments"
                        name="comments"
                        type="checkbox"
                        class="
                          h-4
                          w-4
                          rounded
                          border-gray-300
                          text-indigo-600
                          focus:ring-indigo-500
                        "
                      />
                    </div>
                    <div class="ml-3 text-sm">
                      <label for="comments" class="font-medium text-gray-700"
                        >Comments</label
                      >
                      <p class="text-gray-500">
                        Get notified when someones posts a comment on a posting.
                      </p>
                    </div>
                  </div>
                  <div class="relative flex items-start">
                    <div class="flex h-5 items-center">
                      <input
                        id="candidates"
                        name="candidates"
                        type="checkbox"
                        class="
                          h-4
                          w-4
                          rounded
                          border-gray-300
                          text-indigo-600
                          focus:ring-indigo-500
                        "
                      />
                    </div>
                    <div class="ml-3 text-sm">
                      <label for="candidates" class="font-medium text-gray-700"
                        >Candidates</label
                      >
                      <p class="text-gray-500">
                        Get notified when a candidate applies for a job.
                      </p>
                    </div>
                  </div>
                  <div class="relative flex items-start">
                    <div class="flex h-5 items-center">
                      <input
                        id="offers"
                        name="offers"
                        type="checkbox"
                        class="
                          h-4
                          w-4
                          rounded
                          border-gray-300
                          text-indigo-600
                          focus:ring-indigo-500
                        "
                      />
                    </div>
                    <div class="ml-3 text-sm">
                      <label for="offers" class="font-medium text-gray-700"
                        >Offers</label
                      >
                      <p class="text-gray-500">
                        Get notified when a candidate accepts or rejects an
                        offer.
                      </p>
                    </div>
                  </div>
                </div>
              </fieldset>
              <fieldset class="mt-6">
                <legend class="contents text-base font-medium text-gray-900">
                  Push Notifications
                </legend>
                <p class="text-sm text-gray-500">
                  These are delivered via SMS to your mobile phone.
                </p>
                <div class="mt-4 space-y-4">
                  <div class="flex items-center">
                    <input
                      id="push-everything"
                      name="push-notifications"
                      type="radio"
                      class="
                        h-4
                        w-4
                        border-gray-300
                        text-indigo-600
                        focus:ring-indigo-500
                      "
                    />
                    <label
                      for="push-everything"
                      class="ml-3 block text-sm font-medium text-gray-700"
                      >Everything</label
                    >
                  </div>
                  <div class="flex items-center">
                    <input
                      id="push-email"
                      name="push-notifications"
                      type="radio"
                      class="
                        h-4
                        w-4
                        border-gray-300
                        text-indigo-600
                        focus:ring-indigo-500
                      "
                    />
                    <label
                      for="push-email"
                      class="ml-3 block text-sm font-medium text-gray-700"
                      >Same as email</label
                    >
                  </div>
                  <div class="flex items-center">
                    <input
                      id="push-nothing"
                      name="push-notifications"
                      type="radio"
                      class="
                        h-4
                        w-4
                        border-gray-300
                        text-indigo-600
                        focus:ring-indigo-500
                      "
                    />
                    <label
                      for="push-nothing"
                      class="ml-3 block text-sm font-medium text-gray-700"
                      >No push notifications</label
                    >
                  </div>
                </div>
              </fieldset>
            </div>
          </div>
        </div>

        <div class="pt-5">
          <div class="flex justify-end">
            <button
              type="button"
              class="
                rounded-md
                border border-gray-300
                bg-white
                py-2
                px-4
                text-sm
                font-medium
                text-gray-700
                shadow-sm
                hover:bg-gray-50
                focus:outline-none
                focus:ring-2
                focus:ring-indigo-500
                focus:ring-offset-2
              "
            >
              Cancel
            </button>
            <button
              type="submit"
              class="
                ml-3
                inline-flex
                justify-center
                rounded-md
                border border-transparent
                bg-indigo-600
                py-2
                px-4
                text-sm
                font-medium
                text-white
                shadow-sm
                hover:bg-indigo-700
                focus:outline-none
                focus:ring-2
                focus:ring-indigo-500
                focus:ring-offset-2
              "
            >
              Save
            </button>
          </div>
        </div>
      </form>
    </article>
  </main>
</template>


<script setup lang="ts">
</script>

<style>
</style>