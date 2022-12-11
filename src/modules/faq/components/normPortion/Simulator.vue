<template>
  <div>
    <div class="pt-8">
      <h2 class="text-3xl font-bold tracking-tight text-gray-900">
        Simulator
      </h2>
      <p class="mt-4 text-lg text-gray-500">
        Mit diesem Simulator kannst du das System der Normperson besser
        verstehen. Es gibt drei wichtige Parameter, welche die Norm-Portions
        beeinflussen kann. <br />
      </p>
      <div class="mt-6 grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-4">
        <Base
          :cols="6"
          component="Select"
          techName="gender"
          v-model="state['gender']"
          label="Geschlecht"
          :items="genders"
          hint="Wähle ein Geschlecht aus."
          :errors="errors.gender && errors.gender.$errors"
        />
        <Base
          :cols="6"
          component="Number"
          techName="age"
          v-model="state['age']"
          label="Alter"
          hint="Wähle das Alter aus."
          :errors="errors.age && errors.age.$errors"
        />
        <Base
          :cols="6"
          component="Select"
          techName="activity"
          v-model="state['activity']"
          label="Aktivität"
          :items="activities"
          hint="Wähle die Art der Aktivität aus."
          :errors="errors.activity && errors.activity.$errors"
        />
      </div>
      <h1 class="py-2">Tagesbedarf an Engerie</h1>
      <h2 class="py-2">
        {{ normPersonEnergy }} kJ (enspricht das
        <b>{{ normPersonFactor.toFixed(1) }}</b> fache einer Norm-Portion.)
      </h2>
      <h2>
        {{ getMassByAge(state.age, gender?.value).toFixed(1) }} Kg
        {{ getHeightByAge(state.age, gender?.value).toFixed(1) }} cm
      </h2>
      <br />
      <h1 class="py-2"><b>Norm-Person </b>Männlich, 15 Jahre, {{ getHeightByAge(15, 1) }} cm, {{ getMassByAge(15, 1) }} Kg ,  Zeltlager</h1>
      <h2 class="py-2">{{ getEnergyPerDay(15, 1, 1.8) }} kJ</h2>
    </div>
    <apexchart
      type="line"
      ref="linePlotRef"
      :series="series"
      :options="options"
    ></apexchart>
  </div>
</template>

<script setup lang="ts">
import { computed, reactive, onMounted, ref } from "vue";
import Base from "@/components/field/Base.vue";
import Breadcrumbs from "@/components/breadcrumbs/Header.vue";
import PrimaryButton from "@/components/button/Primary.vue";
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
  const mass = getMassByAge(age, genderId)
  const height = Math.sqrt(getMassByAge(age, genderId) / 24) * 100 // 24 ist BMI

  return Math.round(height / 1 * 1);
}

function getMassByAge(age: number, genderId: number) {
  let mass = 80;
  if (genderId === 1) {
    mass = 80;
    if (age <= 20) {
      mass = 75;
    }
    if (age <= 18) {
      mass = 72;
    }
    if (age <= 17) {
      mass = 70;
    }
    if (age <= 16) {
      mass = 66;
    }
    if (age <= 15) {
      mass = 61;
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
    mass = 65;
    if (age <= 17) {
      mass = 63;
    }
    if (age <= 16) {
      mass = 60;
    }
    if (age <= 15) {
      mass = 59;
    }
    if (age <= 14) {
      mass = 57;
    }
    if (age <= 13) {
      mass = 51;
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
    output = Math.round((energyKj / getEnergyPerDay(15, 1, 1.8)) * 100) / 100;
  } else {
    output = energyKj;
  }

  return Math.round(output * 100) / 100;
}

const normPersonEnergy = computed(() => {
  return getEnergyPerDay(
    state.age,
    state.gender?.value,
    state.activity?.value
  );
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
    data: ageArray.map((age) => getEnergyPerDay(age, 1, 1.8, true)),
  },
  {
    name: "weiblich",
    data: ageArray.map((age) => getEnergyPerDay(age, 2, 1.8, true)),
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
    name: "Schulung (x 1.4)",
    value: 1.4,
  },
  {
    name: "Zeltlager (x 1.8)",
    value: 1.8,
  },
  {
    name: "Wandern (x 2.2)",
    value: 2.2,
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

</script>
