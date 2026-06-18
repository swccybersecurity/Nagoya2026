<script setup>
const links = [
  { href: '#itinerary', label: '行程' },
  { href: '#hotel',     label: '住宿' },
  { href: '#budget',    label: '預算' },
  { href: '#tips',      label: '小提醒' },
  { href: '#checklist', label: '清單' },
]
</script>

<template>
  <nav
    aria-label="主要導覽"
    class="sticky top-3 z-50 mx-3 flex items-center justify-between gap-3 rounded-full border border-yamabuki-200/40 bg-ivory-50/90 px-4 py-2.5 shadow-card-sm backdrop-blur-xl md:mx-6"
  >
    <!-- Brand -->
    <div class="flex items-center gap-2.5 flex-shrink-0">
      <div class="grid h-8 w-8 place-items-center rounded-full bg-gradient-to-br from-yamabuki-400 to-kaki-500 text-white shadow-card-sm">
        <span class="font-heading text-sm font-bold leading-none">名</span>
      </div>
      <span class="hidden font-heading text-base font-semibold text-ivory-900 sm:block">名古屋 2026</span>
    </div>

    <!-- Links -->
    <div class="flex items-center gap-1 overflow-x-auto scrollbar-none">
      <a
        v-for="l in links"
        :key="l.href"
        :href="l.href"
        class="whitespace-nowrap rounded-full px-3 py-1.5 font-body text-sm font-semibold text-ivory-700 transition-colors duration-200 hover:bg-yamabuki-100 hover:text-yamabuki-700"
      >{{ l.label }}</a>
    </div>
  </nav>
</template>
