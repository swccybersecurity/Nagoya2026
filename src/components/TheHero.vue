<script setup>
import { computed } from 'vue'
import { TRIP } from '../data/itinerary.js'

const today = new Date()
const daysLeft = computed(() => Math.ceil((TRIP.start - today) / 86400000))
const tripDay  = computed(() => Math.floor((today - TRIP.start) / 86400000))

const status = computed(() => {
  if (daysLeft.value > 0)  return { type: 'pre',  msg: `距離出發還有 ${daysLeft.value} 天！` }
  if (tripDay.value <= 8)  return { type: 'live', msg: `旅程第 ${tripDay.value + 1} 天，正在進行中！` }
  return { type: 'post', msg: '旅程已圓滿結束，感謝這段美好回憶 🌸' }
})

const stats = [
  { num: '9', label: '天旅程' },
  { num: '2', label: '個小孩' },
  { num: '9', label: '大景點' },
  { num: '1', label: '王子飯店' },
]
</script>

<template>
  <header class="relative overflow-hidden bg-hero px-4 pb-20 pt-12 md:pb-28 md:pt-20">

    <!-- Floating decorative blobs -->
    <div aria-hidden="true"
      class="pointer-events-none absolute -right-20 -top-20 h-72 w-72 rounded-full bg-yamabuki-200/30 blur-3xl animate-float"
    />
    <div aria-hidden="true"
      class="pointer-events-none absolute -bottom-10 -left-16 h-56 w-56 rounded-full bg-kaki-200/25 blur-3xl animate-float-d"
    />
    <div aria-hidden="true"
      class="pointer-events-none absolute bottom-20 right-1/4 h-40 w-40 rounded-full bg-fuji-200/20 blur-2xl animate-float"
    />

    <div class="relative mx-auto max-w-container">

      <!-- Kicker -->
      <div class="mb-5 animate-fade-in-up">
        <span class="inline-flex items-center gap-2 rounded-full bg-yamabuki-400/12 px-4 py-1.5 font-heading text-sm font-semibold uppercase tracking-widest text-yamabuki-600">
          <span class="h-2 w-2 rounded-full bg-yamabuki-500 animate-pulse-dot" />
          2026 家族旅行
        </span>
      </div>

      <!-- Title -->
      <h1 class="mb-3 animate-fade-in-up-1 font-heading text-5xl font-bold leading-tight tracking-tight text-ivory-900 md:text-7xl">
        名古屋<br>
        <span class="text-gradient-accent">親子遊</span>
      </h1>

      <!-- Subtitle -->
      <p class="mb-6 animate-fade-in-up-2 font-body text-lg text-ivory-700 md:text-xl">
        {{ TRIP.subtitle }} ✈️ {{ TRIP.flightOut }} / {{ TRIP.flightRtn }}<br>
        <span class="text-base text-ivory-600">7 月 13 日 – 7 月 21 日 · 名古屋王子大飯店</span>
      </p>

      <!-- Status banner -->
      <div class="mb-8 animate-fade-in-up-3 inline-flex items-center gap-2 rounded-card-md px-5 py-3 text-sm font-semibold shadow-card-sm"
        :class="{
          'bg-yamabuki-400 text-white': status.type === 'pre',
          'bg-kaki-500 text-white':     status.type === 'live',
          'bg-ivory-300 text-ivory-700': status.type === 'post',
        }"
      >
        <span>{{ status.msg }}</span>
      </div>

      <!-- Stats -->
      <div class="grid grid-cols-2 gap-3 sm:grid-cols-4 md:gap-4 animate-fade-in-up-3">
        <div
          v-for="s in stats" :key="s.label"
          class="rounded-card-md border border-ivory-300 bg-ivory-50/80 px-4 py-4 text-center shadow-card-sm transition-all duration-300 ease-custom hover:-translate-y-1 hover:shadow-card-md"
        >
          <p class="font-heading text-3xl font-bold text-yamabuki-500 md:text-4xl">{{ s.num }}</p>
          <p class="mt-0.5 font-body text-sm text-ivory-600">{{ s.label }}</p>
        </div>
      </div>
    </div>
  </header>
</template>
