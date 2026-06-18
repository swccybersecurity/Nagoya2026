<script setup>
import TheNav         from './components/TheNav.vue'
import TheHero        from './components/TheHero.vue'
import InfoBar        from './components/InfoBar.vue'
import DayCard        from './components/DayCard.vue'
import TipsSection    from './components/TipsSection.vue'
import BudgetSection  from './components/BudgetSection.vue'
import ChecklistSection from './components/ChecklistSection.vue'
import TheFooter      from './components/TheFooter.vue'
import { days }       from './data/itinerary.js'
import { useScrollReveal } from './composables/useScrollReveal.js'

useScrollReveal()
</script>

<template>
  <TheNav />
  <TheHero />
  <InfoBar />

  <!-- Itinerary -->
  <section id="itinerary" class="px-4 py-16 md:py-24">
    <div class="mx-auto max-w-container">
      <div class="mb-10 reveal text-center">
        <span class="mb-3 inline-block rounded-full bg-yamabuki-400/12 px-4 py-1.5 font-heading text-sm font-semibold uppercase tracking-widest text-yamabuki-600">
          九天行程
        </span>
        <h2 class="font-heading text-3xl font-bold text-ivory-900 md:text-4xl">每日行程總覽</h2>
      </div>
      <DayCard v-for="day in days" :key="day.id" :day="day" />
    </div>
  </section>

  <TipsSection />
  <BudgetSection />
  <ChecklistSection />
  <TheFooter />
</template>
