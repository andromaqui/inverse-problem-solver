<template>
  <div class="image-deblur-container">
    <h1>2D Image Inverse Tool: Deblurring</h1>

    <div class="image-section">
      <div class="image-preview">
        <h3>Blurred Image</h3>
        <img :src="cameramanImage" alt="Blurred cameraman" />
      </div>
    </div>

    <div v-if="deblurredImage" class="image-preview">
        <h3>Deblurred Image</h3>
        <img :src="deblurredImage" alt="Deblurred result" />
    </div>

    <button @click="unblurImage" class="action-button">Unblur</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const cameramanImage = ref(new URL('@/assets/cameraman_blurred.png', import.meta.url).href)
const deblurredImage = ref(null)

async function unblurImage() {
  const res = await fetch(cameramanImage.value)
  const blob = await res.blob()
  const formData = new FormData()
  formData.append('file', blob, 'cameraman.png')

  const response = await fetch('http://localhost:8000/deblur', {
    method: 'POST',
    body: formData
  })

  const resultBlob = await response.blob()
  deblurredImage.value = URL.createObjectURL(resultBlob)
}

</script>

<style scoped>
.image-deblur-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2rem;
  gap: 1.5rem;
  background-color: #f0f0f0;
  min-height: 100vh;
}

.image-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
}

.image-preview img {
  max-width: 400px;
  border: 2px solid #ccc;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

.action-button {
  padding: 0.75rem 1.5rem;
  font-size: 1rem;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.action-button:hover {
  background-color: #0056b3;
}
</style>
