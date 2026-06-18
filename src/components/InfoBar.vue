<script setup>
import { HOTEL } from '../data/itinerary.js'

const items = [
  { icon: '✈️', label: '去程', value: 'CX530 · 7/13 抵達 NGO 15:30' },
  { icon: '🏨', label: '住宿', value: HOTEL.name },
  { icon: '🚉', label: '最近站', value: HOTEL.station },
  { icon: '✈️', label: '回程', value: 'CX531 · 7/21 NGO 16:40 起飛' },
]
</script>

<template>
  <section id="hotel" class="border-y border-ivory-300 bg-ivory-200/60 px-4 py-6 md:py-8">
    <div class="mx-auto max-w-container">
      <div class="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-4 md:gap-5">
        <a
          v-for="item in items" :key="item.label"
          :href="item.label === '住宿' ? 'https://www.princehotels.com/nagoya/zh-hant/' : undefined"
          :target="item.label === '住宿' ? '_blank' : undefined"
          class="flex items-start gap-3 rounded-card-md border border-ivory-300 bg-ivory-50 px-4 py-4 shadow-card-sm transition-all duration-200 hover:-translate-y-0.5 hover:shadow-card-md"
          :class="item.label === '住宿' ? 'cursor-pointer' : 'cursor-default'"
        >
          <span class="mt-0.5 text-xl">{{ item.icon }}</span>
          <div class="min-w-0">
            <p class="font-body text-xs font-semibold uppercase tracking-wider text-ivory-500">{{ item.label }}</p>
            <p class="mt-0.5 font-body text-sm font-semibold text-ivory-800 leading-snug">{{ item.value }}</p>
          </div>
        </a>
      </div>
    </div>
  </section>
</template>
