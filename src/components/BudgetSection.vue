<script setup>
import { computed } from 'vue'
import { BUDGET_DAYS } from '../data/itinerary.js'

const total = computed(() => BUDGET_DAYS.reduce((s, d) => s + d.amount, 0).toLocaleString())
const maxAmt = computed(() => Math.max(...BUDGET_DAYS.map((d) => d.amount)))
</script>

<template>
  <section id="budget" class="bg-ivory-900 px-4 py-16 md:py-24">
    <div class="mx-auto max-w-container">

      <!-- Header -->
      <div class="mb-10 reveal text-center">
        <span class="mb-3 inline-block rounded-full bg-yamabuki-400/20 px-4 py-1.5 font-heading text-sm font-semibold uppercase tracking-widest text-yamabuki-400">
          預算總覽
        </span>
        <h2 class="font-heading text-3xl font-bold text-ivory-100 md:text-4xl">每日花費估算</h2>
        <p class="mt-2 font-body text-sm text-ivory-400">含門票、餐費、交通（不含機票、住宿）</p>
      </div>

      <!-- Day bars -->
      <div class="reveal mb-8 space-y-3">
        <div
          v-for="d in BUDGET_DAYS" :key="d.day"
          class="flex items-center gap-3"
        >
          <span class="w-28 flex-shrink-0 font-body text-xs text-ivory-400 text-right">{{ d.label }}</span>
          <div class="flex-1 rounded-full bg-ivory-800 h-5 overflow-hidden">
            <div
              class="h-full rounded-full bg-gradient-to-r from-yamabuki-400 to-kaki-500 transition-all duration-700"
              :style="{ width: `${(d.amount / maxAmt) * 100}%` }"
            />
          </div>
          <span class="w-20 flex-shrink-0 font-heading text-sm font-semibold text-yamabuki-400">¥{{ d.amount.toLocaleString() }}</span>
        </div>
      </div>

      <!-- Total -->
      <div class="reveal mx-auto max-w-sm rounded-card-lg bg-gradient-to-br from-yamabuki-400 to-kaki-500 px-8 py-6 text-center text-white shadow-card-kaki">
        <p class="font-body text-sm uppercase tracking-[0.12em] opacity-80">9 天預估總花費</p>
        <p class="mt-1 font-heading text-4xl font-bold md:text-5xl">¥{{ total }}</p>
        <p class="mt-1 font-body text-xs opacity-70">以上為日幣，約 3 大 2 小行程花費</p>
      </div>
    </div>
  </section>
</template>
