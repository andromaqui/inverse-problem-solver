<template>
  <div v-if="message" :class="['alert', typeClass]">
    <span>{{ message }}</span>
    <button v-if="dismissible" @click="$emit('close')">✕</button>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  message: String,
  type: { type: String, default: 'error' },
  dismissible: { type: Boolean, default: false }
})

const typeClass = computed(() => {
  return {
    error: 'alert-error',
    info: 'alert-info',
    success: 'alert-success'
  }[props.type] || 'alert-error'
})
</script>

<style scoped>
.alert {
  padding: 0.75rem 1rem;
  border-radius: 6px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.95rem;
  margin: 0.5rem 0;
  max-width: 500px;
}

.alert-error {
  background-color: #ffe6e6;
  color: #a11;
  border: 1px solid #a11;
}

.alert-info {
  background-color: #e6f0ff;
  color: #114488;
  border: 1px solid #114488;
}

.alert-success {
  background-color: #e6ffee;
  color: #116633;
  border: 1px solid #116633;
}

button {
  background: none;
  border: none;
  font-size: 1rem;
  cursor: pointer;
}
</style>
