<script setup>
import { computed } from 'vue'
import { CHECKLIST } from '../data/itinerary.js'
import { useChecklist } from '../composables/useChecklist.js'

const { toggle, isChecked } = useChecklist()

const cats = computed(() => [...new Set(CHECKLIST.map((c) => c.cat))])
const bycat = (cat) => CHECKLIST.filter((c) => c.cat === cat)

const total   = CHECKLIST.length
const done    = computed(() => CHECKLIST.filter((c) => isChecked(c.id)).length)
const pct     = computed(() => Math.round((done.value / total) * 100))
</script>

<template>
  <section id="checklist" class="px-4 py-16 md:py-24">
    <div class="mx-auto max-w-container">

      <!-- Header -->
      <div class="mb-10 reveal text-center">
        <span class="mb-3 inline-block rounded-full bg-fuji-500/10 px-4 py-1.5 font-heading text-sm font-semibold uppercase tracking-widest text-fuji-600">
          出發前準備
        </span>
        <h2 class="font-heading text-3xl font-bold text-ivory-900 md:text-4xl">行前確認清單</h2>
      </div>

      <!-- Progress bar -->
      <div class="reveal mb-8 rounded-card-md border border-ivory-300 bg-ivory-200/60 p-5">
        <div class="mb-2 flex items-center justify-between">
          <span class="font-body text-sm font-semibold text-ivory-700">完成度</span>
          <span class="font-heading text-lg font-bold text-yamabuki-500">{{ done }}/{{ total }}（{{ pct }}%）</span>
        </div>
        <div class="h-3 overflow-hidden rounded-full bg-ivory-300">
          <div
            class="h-full rounded-full bg-gradient-to-r from-yamabuki-400 to-kaki-500 transition-all duration-500"
            :style="{ width: `${pct}%` }"
          />
        </div>
      </div>

      <!-- Checklist groups -->
      <div class="reveal grid grid-cols-1 gap-4 sm:grid-cols-2 md:gap-5">
        <div v-for="cat in cats" :key="cat">
          <h3 class="mb-3 font-heading text-base font-semibold text-ivory-600">{{ cat }}</h3>
          <div class="space-y-2">
            <label
              v-for="item in bycat(cat)" :key="item.id"
              class="flex cursor-pointer items-center gap-3 rounded-card-md border border-ivory-300 bg-ivory-50 px-4 py-3 shadow-card-sm transition-all duration-200 hover:border-yamabuki-300"
              :class="isChecked(item.id) ? 'opacity-60' : ''"
            >
              <div
                class="flex h-6 w-6 flex-shrink-0 items-center justify-center rounded-md border-2 transition-all duration-200"
                :class="isChecked(item.id)
                  ? 'border-yamabuki-500 bg-yamabuki-500 text-white'
                  : 'border-ivory-400 bg-white'"
                @click.prevent="toggle(item.id)"
              >
                <svg v-if="isChecked(item.id)" viewBox="0 0 14 14" fill="none" class="h-3.5 w-3.5">
                  <path d="M2 7l4 4 6-6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </div>
              <span
                class="font-body text-sm text-ivory-800 transition-all duration-200"
                :class="isChecked(item.id) ? 'line-through text-ivory-400' : ''"
                @click="toggle(item.id)"
              >{{ item.text }}</span>
            </label>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
