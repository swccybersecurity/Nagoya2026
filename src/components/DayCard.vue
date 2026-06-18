<script setup>
import { ref } from 'vue'

const props = defineProps({ day: { type: Object, required: true } })

// Dual-plan state (persisted per day in localStorage)
const planKey = `nagoya2026-plan-day${props.day.id}`
const activePlan = ref(localStorage.getItem(planKey) || (props.day.plans?.[0]?.id ?? null))

function switchPlan(id) {
  activePlan.value = id
  localStorage.setItem(planKey, id)
}

const currentPlan = () =>
  props.day.isDualPlan
    ? props.day.plans.find((p) => p.id === activePlan.value) ?? props.day.plans[0]
    : null

const highlightVariants = {
  default:   'border-l-yamabuki-400 from-yamabuki-50 to-ivory-50',
  yamabuki:  'border-l-yamabuki-500 from-yamabuki-50 to-ivory-50',
  kaki:      'border-l-kaki-500     from-kaki-50     to-ivory-50',
  fuji:      'border-l-fuji-500     from-fuji-50     to-ivory-50',
  sky:       'border-l-sky-500      from-sky-50      to-ivory-50',
  green:     'border-l-emerald-500  from-emerald-50  to-ivory-50',
  pink:      'border-l-pink-400     from-pink-50     to-ivory-50',
}

function hlClass(variant) {
  return highlightVariants[variant] ?? highlightVariants.default
}
</script>

<template>
  <article
    :id="`day-${day.id}`"
    class="reveal mb-8 overflow-hidden rounded-card-lg border border-ivory-300 bg-ivory-50 shadow-card-sm transition-all duration-300 ease-custom hover:-translate-y-0.5 hover:shadow-card-lg"
  >
    <!-- Cover image -->
    <div class="relative w-full overflow-hidden" style="aspect-ratio: 2/1;">
      <img
        :src="day.isDualPlan ? currentPlan()?.coverImg : day.cover"
        :alt="day.title"
        class="h-full w-full object-cover transform-gpu transition-transform duration-500 hover:scale-[1.03]"
        loading="lazy"
        onerror="this.style.display='none'"
      />
      <div class="absolute inset-0 bg-gradient-to-t from-ivory-900/60 to-transparent" />
      <!-- Day badge overlay -->
      <div
        class="absolute left-5 top-5 grid h-14 w-14 flex-shrink-0 place-items-center rounded-card-md text-center text-white shadow-lg md:h-16 md:w-16"
        :class="day.badgeClass"
      >
        <div>
          <span class="block font-heading text-2xl font-bold leading-none md:text-3xl">{{ day.num }}</span>
          <span class="block text-[0.65rem] tracking-[0.15em] opacity-85">DAY</span>
        </div>
      </div>
      <!-- Tag -->
      <span
        v-if="day.tag"
        class="absolute right-4 top-4 rounded-full border px-3 py-1 font-body text-xs font-semibold backdrop-blur-sm"
        :class="day.tag.cls"
      >{{ day.tag.text }}</span>
    </div>

    <!-- Card body -->
    <div class="p-5 md:p-8">

      <!-- Header -->
      <div class="mb-5 border-b-2 border-dashed border-ivory-300 pb-5">
        <div class="flex flex-wrap items-center gap-3">
          <div>
            <p class="font-body text-sm font-semibold text-yamabuki-500">{{ day.date }}</p>
            <h3 class="font-heading text-xl font-bold text-ivory-900 md:text-2xl">{{ day.title }}</h3>
          </div>
        </div>
      </div>

      <!-- Dual plan tab switcher -->
      <div v-if="day.isDualPlan" class="mb-6">
        <div class="flex gap-2 rounded-card-md border border-ivory-300 bg-ivory-200/60 p-1.5">
          <button
            v-for="plan in day.plans"
            :key="plan.id"
            class="flex flex-1 flex-col items-center gap-0.5 rounded-card-sm px-3 py-2.5 text-center transition-all duration-200 ease-custom"
            :class="activePlan === plan.id
              ? 'bg-gradient-to-br from-yamabuki-400 to-kaki-500 text-white shadow-card-sm'
              : 'text-ivory-600 hover:bg-ivory-300/60'"
            @click="switchPlan(plan.id)"
          >
            <span class="font-heading text-base font-semibold">{{ plan.label }}</span>
            <span class="font-body text-xs opacity-80">{{ plan.sublabel }}</span>
          </button>
        </div>
      </div>

      <!-- Content: timeline + highlights -->
      <Transition name="plan" mode="out-in">
        <div :key="day.isDualPlan ? activePlan : 'single'" class="grid grid-cols-1 gap-6 md:grid-cols-2 md:gap-8">

          <!-- Timeline -->
          <div>
            <div
              v-for="(item, idx) in (day.isDualPlan ? currentPlan()?.timeline : day.timeline)"
              :key="idx"
              class="relative pl-7"
              :class="idx < (day.isDualPlan ? currentPlan()?.timeline : day.timeline).length - 1
                ? 'border-l-2 border-ivory-300 pb-5'
                : 'border-l-2 border-transparent pb-0'"
            >
              <div class="absolute -left-[7px] top-1 h-3 w-3 rounded-full border-[3px] border-ivory-50 bg-yamabuki-500 shadow-[0_0_0_2px] shadow-yamabuki-300 animate-pulse-dot" />
              <p class="mb-1 font-heading text-sm font-semibold tracking-wide text-yamabuki-500">{{ item.time }}</p>
              <div class="font-body text-[0.9375rem] text-ivory-800" v-html="item.html" />
            </div>
          </div>

          <!-- Highlights -->
          <div class="space-y-3">
            <div
              v-for="(hl, idx) in (day.isDualPlan ? currentPlan()?.highlights : day.highlights)"
              :key="idx"
              class="rounded-card-md border-l-4 bg-gradient-to-br p-4 transition-all duration-200 ease-custom hover:translate-x-1"
              :class="hlClass(hl.variant)"
            >
              <h4 class="mb-1.5 font-heading text-base font-semibold text-ivory-900">{{ hl.title }}</h4>
              <p v-if="hl.body" class="font-body text-[0.9rem] leading-relaxed text-ivory-700">{{ hl.body }}</p>
              <ul v-if="hl.list" class="mt-1.5 space-y-1 pl-4 font-body text-[0.875rem] text-ivory-700 list-disc">
                <li v-for="(li, li_idx) in hl.list" :key="li_idx">{{ li }}</li>
              </ul>
            </div>

            <!-- Budget mini bar -->
            <div
              v-if="(day.isDualPlan ? currentPlan()?.budget : day.budget)"
              class="flex items-center justify-between rounded-card-md bg-gradient-to-br from-ivory-900 to-ivory-800 px-5 py-4 text-white"
            >
              <div>
                <p class="font-body text-xs uppercase tracking-[0.1em] opacity-70">
                  {{ (day.isDualPlan ? currentPlan()?.budget : day.budget).label }}
                </p>
                <p class="font-body text-xs opacity-60">
                  {{ (day.isDualPlan ? currentPlan()?.budget : day.budget).note }}
                </p>
              </div>
              <p class="font-heading text-2xl font-bold">
                <span class="mr-0.5 text-sm opacity-70">¥</span>
                {{ (day.isDualPlan ? currentPlan()?.budget : day.budget).amount }}
              </p>
            </div>
          </div>

        </div>
      </Transition>
    </div>
  </article>
</template>
