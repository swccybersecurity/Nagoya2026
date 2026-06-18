<script setup>
import { TIPS } from '../data/itinerary.js'

const variantCls = {
  yamabuki: 'from-yamabuki-50 to-ivory-50 border-yamabuki-200',
  kaki:     'from-kaki-50     to-ivory-50 border-kaki-200',
  fuji:     'from-fuji-50     to-ivory-50 border-fuji-200',
  green:    'from-emerald-50  to-ivory-50 border-emerald-200',
}

const iconBgCls = {
  yamabuki: 'bg-yamabuki-100',
  kaki:     'bg-kaki-100',
  fuji:     'bg-fuji-100',
  green:    'bg-emerald-100',
}
</script>

<template>
  <section id="tips" class="px-4 py-16 md:py-24">
    <div class="mx-auto max-w-container">

      <!-- Section header -->
      <div class="mb-10 text-center reveal">
        <span class="mb-3 inline-block rounded-full bg-kaki-500/10 px-4 py-1.5 font-heading text-sm font-semibold uppercase tracking-widest text-kaki-500">
          旅遊提醒
        </span>
        <h2 class="font-heading text-3xl font-bold text-ivory-900 md:text-4xl">帶兩個小孩出門的眉角</h2>
      </div>

      <div class="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-3 md:gap-6">
        <div
          v-for="tip in TIPS" :key="tip.title"
          class="reveal rounded-card-lg border bg-gradient-to-br p-6 shadow-card-sm transition-all duration-300 ease-custom hover:-translate-y-1.5 hover:shadow-card-md md:p-7"
          :class="variantCls[tip.variant] ?? variantCls.yamabuki"
        >
          <div
            class="mb-4 flex h-12 w-12 items-center justify-center rounded-card-sm text-2xl shadow-card-sm"
            :class="iconBgCls[tip.variant] ?? iconBgCls.yamabuki"
          >
            {{ tip.icon }}
          </div>
          <h3 class="mb-2 font-heading text-lg font-semibold text-ivory-900">{{ tip.title }}</h3>
          <p class="font-body text-sm leading-relaxed text-ivory-700">{{ tip.body }}</p>
        </div>
      </div>
    </div>
  </section>
</template>
