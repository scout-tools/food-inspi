
  <template>
  <div class="bg-white">
    <div class="mx-auto max-w-7xl py-16 px-4 sm:px-6 lg:py-20 lg:px-8">
      <div class="lg:grid lg:grid-cols-3 lg:gap-8">
        <div>
          <h2 class="text-3xl font-bold tracking-tight text-gray-900">
            Was du zum Thema "Norm-Portion" im Food-Inspi wissen musst.
          </h2>
          <p class="mt-4 text-lg text-gray-500">
            Such dir die passende Frage aus der Liste her. Wenn dir eine Frage
            fehlt schreibe eine
            <a href="#" class="font-medium text-blue-600 hover:text-blue-500"
              >Nachricht an Inspi</a
            >
          </p>
        </div>
        <div class="mt-12 lg:col-span-2 lg:mt-0">
          <dl class="space-y-12">
            <div v-for="faq in faqs" :key="faq.question">
              <dt class="text-lg font-medium leading-6 text-gray-900">
                {{ faq.question }}
              </dt>
              <dd class="mt-2 text-base text-gray-500">{{ faq.answer }}</dd>
            </div>
          </dl>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const faqs = [
  {
    question: "Wieso braucht es die Definition einer Norm-Person?",
    answer:
      "Um die korrekte Menge für eine große Gruppe genau kalkulieren zu können kommt es nicht nur" +
      "auf das das richtige Verhältnis zwischen den Zutaten an, sondern natürlich auch um gesamt Mnege." +
      "Im Grund hängt die richtige Portionsgröße von drei Fatoren ab. Der Aktivität über den Tag, dem Alter und das Geschlecht." +
      "Jeder Mensche bekommt also seine indivuelle Norm-Portionsgröße. Die Summe aller Portionen kommt dann auf dem Einkaufszettel.",
  },
  {
    question: "Auf welcher Wissenschaftlichen Grundlage erfolgt die Rechnung?",
    answer:
      "Die Basis der Berechnung basiert auf einen unterschiedlichen Grundumsatz von unterschiedlichen Personen mit unterschiedlichen Tagesabläufen." +
      "Dazu wird der Grundumsatz mit der nach Mifflin-St.Jeor-Formel berechnet und zu einer bestimmten willkürlichen Kombination von Parametern." +
      "ins Verhältnis gesetzt. Für das Gewicht und der Größe wurde der Median je nach Alter und Geschlecht verwendet. Die Daten veröffentlicht das RKI.",
  },
  {
    question:
      "Wieso ist eine männliche 15 jährige Person als als Norm-Portion definiert?",
    answer:
      "Die Portion entspricht ungefähr dem Mittel einer durschschnittlichen Person die an einem großem Lager teilnimmt.",
  },
];
</script>
