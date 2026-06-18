import { ref } from 'vue'

const KEY = 'nagoya2026-checklist'
const checked = ref(JSON.parse(localStorage.getItem(KEY) || '[]'))

function toggle(id) {
  const idx = checked.value.indexOf(id)
  if (idx === -1) checked.value.push(id)
  else checked.value.splice(idx, 1)
  localStorage.setItem(KEY, JSON.stringify(checked.value))
}

function isChecked(id) {
  return checked.value.includes(id)
}

export function useChecklist() {
  return { checked, toggle, isChecked }
}
