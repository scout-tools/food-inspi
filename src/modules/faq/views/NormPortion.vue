<template>
  <div class="2xl:px-64 xl:px-30">
    <article class="flex-shrink-0 border border-gray-200 ma-12">
      <form class="space-y-8 divide-y px-3 py-4 divide-gray-200">
        <div class="space-y-8 divide-y divide-gray-200">
          <FaqNormPortion />
          <SimulatorNormPortion/>
        </div>
      </form>
    </article>
  </div>
</template>


<script setup lang="ts">
import { computed, reactive, onMounted, ref } from "vue";
import Base from "@/components/field/Base.vue";
import Breadcrumbs from "@/components/breadcrumbs/Header.vue";
import PrimaryButton from "@/components/button/Primary.vue";
import Success from "@/modules/common/components/Success.vue";
import FaqNormPortion from "@/modules/faq/components/normPortion/FaqNormPortion.vue";
import SimulatorNormPortion from "@/modules/faq/components/normPortion/Simulator.vue";
import { useIngredientStore } from "@/modules/ingredient/store/index.ts";

import { useVuelidate } from "@vuelidate/core";
import { required, email, minLength, maxLength } from "@vuelidate/validators";

import { useRoute, useRouter } from "vue-router";

const route = useRoute();

const pages = computed(() => {
  return [
    { name: "Zutaten", link: "IngredientMain", current: false },
    {
      name: "Neue Zutat",
      link: `IngredientCreate`,
      current: true,
    },
  ];
});

const ingredientStore = useIngredientStore();

function getHeightByAge(age: number, genderId: number) {
  return getMassByAge(age, genderId) + 100;
}

function getMassByAge(age: number, genderId: number) {
  let mass = 60;
  if (genderId === 1) {
    mass = 80;
    if (age <= 20) {
      mass = 75;
    }
    if (age <= 18) {
      mass = 73;
    }
    if (age <= 17) {
      mass = 70;
    }
    if (age <= 16) {
      mass = 66;
    }
    if (age <= 15) {
      mass = 62;
    }
    if (age <= 14) {
      mass = 55;
    }
    if (age <= 13) {
      mass = 50;
    }
    if (age <= 12) {
      mass = 45;
    }
    if (age <= 11) {
      mass = 40;
    }
    if (age <= 10) {
      mass = 35;
    }
    if (age <= 9) {
      mass = 32;
    }
    if (age <= 8) {
      mass = 27;
    }
    if (age <= 7) {
      mass = 25;
    }
    if (age <= 6) {
      mass = 22;
    }
  } else {
    mass = 60;
    if (age <= 17) {
      mass = 59;
    }
    if (age <= 16) {
      mass = 58;
    }
    if (age <= 15) {
      mass = 57;
    }
    if (age <= 14) {
      mass = 54;
    }
    if (age <= 13) {
      mass = 50;
    }
    if (age <= 12) {
      mass = 45;
    }
    if (age <= 11) {
      mass = 40;
    }
    if (age <= 10) {
      mass = 35;
    }
    if (age <= 9) {
      mass = 32;
    }
    if (age <= 8) {
      mass = 27;
    }
    if (age <= 7) {
      mass = 25;
    }
    if (age <= 6) {
      mass = 22;
    }
  }

  return mass;
}

function getEnergyPerDay(
  age: number,
  genderId: any,
  activityFactor: number,
  norm = false
) {
  let energyKj = 0;
  let output = 0.0;
  // mass
  energyKj += 10 * getMassByAge(age, genderId);
  //height
  energyKj += 6.25 * getHeightByAge(age, genderId);
  // gender
  energyKj += -5 * age;
  // gender factor
  energyKj += genderId === 2 ? -161 : 5;
  // check divers
  // energyKj += genderId === 3 ? 160 : 0;
  // add activityFactor
  energyKj = energyKj * activityFactor;
  // convert to kJ
  energyKj = energyKj * 4.2;

  if (norm) {
    output = Math.round((energyKj / getEnergyPerDay(15, 1, 2)) * 100) / 100;
  } else {
    output = energyKj;
  }

  return output;
}

const normPersonEnergy = computed(() => {
  return getEnergyPerDay(state.age, state.gender?.value, state.activity?.value);
});

const normPersonFactor = computed(() => {
  return getEnergyPerDay(
    state.age,
    state.gender?.value,
    state.activity?.value,
    true
  );
});

const ageArray = [7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35];

function closest(num, arr) {
  var curr = arr[0];
  var diff = Math.abs(num - curr);
  for (var val = 0; val < arr.length; val++) {
    var newdiff = Math.abs(num - arr[val]);
    if (newdiff < diff) {
      diff = newdiff;
      curr = arr[val];
    }
  }
  return curr;
}

const options = computed(() => {
  return {
    chart: {
      id: "vuechart-example",
    },
    xaxis: {
      categories: ageArray,
    },
    markers: {
      size: 6,
    },
    title: {
      text: "Norm-Portion",
    },
    annotations: {
      points: [
        {
          x: closest(state.age, ageArray),
          y: normPersonFactor.value,
          marker: {
            size: 10,
            fillColor: "#F4D920",
            strokeColor: "#000000",
            radius: 20,
          },
          label: {
            offsetY: 0,
            text: "aktuelle Auswahl",
          },
        },
      ],
      yaxis: [
        {
          y: 1,
          strokeDashArray: 15,
          borderColor: "black",
          fillColor: "black",
          opacity: 1,
          offsetX: 0,
          offsetY: 0,
          width: "100%",
          yAxisIndex: 0,

          label: {
            borderColor: "black",
            borderWidth: 10,
            style: {
              color: "#fff",
              background: "black",
            },
            text: "Norm-Portion",
          },
        },
      ],
    },
  };
});

const series = [
  {
    name: "männlich",
    data: ageArray.map((age) => getEnergyPerDay(age, 1, 2, true)),
  },
  {
    name: "weiblich",
    data: ageArray.map((age) => getEnergyPerDay(age, 2, 2, true)),
  },
];

const genders = [
  {
    name: "männlich",
    value: 1,
  },
  {
    name: "weiblich",
    value: 2,
  },
  {
    name: "divers",
    value: 3,
  },
];

const activities = [
  {
    name: "Schulung (x 1.5)",
    value: 1.5,
  },
  {
    name: "Zeltlager (x 2.0)",
    value: 2,
  },
  {
    name: "Wandern (x 2.5)",
    value: 2.5,
  },
];

const state = reactive({
  gender: genders[0],
  age: 15,
  activity: activities[1],
});

const rules = {
  genderId: {
    required,
  },
  age: {
    required,
  },
  activity: {
    required,
  },
};

const v$ = useVuelidate(rules, state);

const errors = ref([]);
const isLoading = ref(false);

const router = useRouter();

import { useCommonStore } from "@/modules/common/store/index";
const commonStore = useCommonStore();

function onButtonClicked() {}

onMounted(() => {});
</script>
