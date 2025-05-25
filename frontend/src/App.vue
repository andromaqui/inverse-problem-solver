<template>
  <div class="container">
    <h1>Inverse Solver</h1>

    <div class="input-row">
      <div class="input-group">
        <input v-model="xInput" placeholder="X values" class="fancy-input" />
      </div>
      <div class="input-group">
        <input v-model="yInput" placeholder="Y values" class="fancy-input" />
      </div>
    </div>

    <AppAlert
      v-if="csvError"
      :message="csvError"
      type="error"
      @close="csvError = ''"
    />

    <label class="upload-label">
      Upload CSV
      <input type="file" @change="handleCSV" accept=".csv" hidden />
    </label>

    <label>Model type:</label>
    <select v-model="modelType">
      <option value="linear">Linear</option>
      <option value="exponential">Exponential</option>
      <option value="polynomial">Polynomial</option>
      <option value="logistic">Logistic</option>
      <option value="sigmoid">Sigmoid</option>
      <option value="powerlaw">Powerlaw</option>
    </select>

    <button @click="submitData">Solve</button>

    <div v-if="result">
      <h3>Estimated Parameters:</h3>
      <pre>{{ result }}</pre>
    </div>

    <DataChart
      v-if="parsedX.length === parsedY.length"
      :x="parsedX"
      :y="parsedY"
      :modelPoints="fittedCurve"
    />
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import DataChart from './components/DataChart.vue'
import AppAlert from './components/AppAlert.vue'

const xInput = ref('')
const yInput = ref('')
const modelType = ref('linear')
const result = ref(null)
const fittedCurve = ref([])
const csvError = ref('')

const parsedX = computed(() => xInput.value.split(',').map(Number).filter(n => !isNaN(n)))
const parsedY = computed(() => yInput.value.split(',').map(Number).filter(n => !isNaN(n)))

async function submitData() {

  const x = parsedX.value
  const y = parsedY.value

  const res = await fetch('http://localhost:8000/fit', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      x,
      y,
      model_type: modelType.value
    })
  })

  const data = await res.json()
  result.value = data.params

  const modelFn = getModelFunction(modelType.value, data.params)
  const minX = Math.min(...x)
  const maxX = Math.max(...x)
  const smoothX = Array.from({ length: 100 }, (_, i) =>
    minX + (i * (maxX - minX)) / 99
  )

  console.log("Params:", data.params)
  console.log("Smooth x range:", smoothX)
  console.log("Sample model output:", modelFn(smoothX[0]))


  fittedCurve.value = smoothX.map(xi => ({
    x: xi,
    y: modelFn(xi)
  }))

}

function safeExp(x) {
  if (x > 100) return Math.exp(100)
  if (x < -100) return Math.exp(-100)
  return Math.exp(x)
}


function getModelFunction(type, params) {
  if (type === 'linear') {
    const [a, b] = params
    return x => a * x + b
  } else if (type === 'exponential') {
    const [a, b] = params
    return x => a * Math.exp(-b * x)
  } else if (type === 'logistic') {

    const [L, k, x0] = params
    return (x) => L / (1 + safeExp(-k * (x - x0)))
  } else if (type === 'polynomial') {
    const [a, b, c] = params
    return x => a * x ** 2 + b * x + c
  } else if (type === 'sigmoid') {
    const [a, b] = params
    return x => 1 / (1 + safeExp(-a * (x - b)))
  } else if (type === 'powerlaw') {
    const [a, b] = params
    return x => a + x**b
  }
  return () => 0
}

function handleCSV(event) {
  const file = event.target.files[0]
  if (!file) return

  const reader = new FileReader()
  reader.onload = () => {
    const text = reader.result
    const rows = text.trim().split('\n')

    const [firstA, firstB] = rows[0].split(',')
    const hasHeader = isNaN(firstA) || isNaN(firstB)
    const dataRows = hasHeader ? rows.slice(1) : rows

    const x = []
    const y = []
    let valid = true

    for (const row of dataRows) {
      const values = row.split(',')
      if (values.length !== 2) {
        csvError.value = "Invalid Format: CSV must have exactly 2 columns."
        valid = false
        break
      }

      const [a, b] = values.map(Number)
      if (isNaN(a) || isNaN(b)) {
        csvError.value = "Invalid CSV: All values must be numbers."
        valid = false
        break
      }

      x.push(a)
      y.push(b)
    }

    if (!valid) return

    if (x.length !== y.length || x.length === 0) {
      csvError.value = "Invalid CSV: X and Y must have the same number of values and not be empty."
      return
    }

    csvError.value = ''
    xInput.value = x.join(',')
    yInput.value = y.join(',')

    console.log("CSV parsed. First values:", x[0], y[0])
  }

  reader.readAsText(file)
}

</script>

<style>
body {
  margin: 0;
  font-family: Arial, sans-serif;
}

html, body {
  margin: 0;
  padding: 0;
  height: 100%;
  overflow: hidden;
}

.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2rem;
  gap: 1rem;
  min-height: 100vh;
  background-color: #f5f5f5;
  justify-content: flex-start;
  padding-top: 3rem;
}

input,
select,
button {
  padding: 0.5rem;
  font-size: 1rem;
  width: 100%;
  max-width: 400px;
  box-sizing: border-box;
}

.input-row {
  display: flex;
  gap: 1rem;
  width: 100%;
  max-width: 500px;
}

.input-group {
  flex: 1;
  display: flex;
  flex-direction: column;
}

input[type="file"] {
  margin-top: 1rem;
}

.upload-label {
  display: inline-block;
  padding: 0.5rem 1rem;
  background-color: #007bff;
  color: white;
  font-size: 1rem;
  text-align: center;
  border-radius: 4px;
  cursor: pointer;
  margin-top: 1rem;
  max-width: 400px;
  width: 100%;
  box-sizing: border-box;
}

.fancy-input {
  border: 1px solid #ccc;
  padding: 0.5rem 0.75rem;
  border-radius: 6px;
  font-size: 1rem;
  background-color: white;
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.05);
  transition: border-color 0.2s, box-shadow 0.2s;
  width: 100%;
}

.fancy-input:focus {
  border-color: #007bff;
  box-shadow: 0 0 0 2px rgba(0, 123, 255, 0.2);
  outline: none;
}
</style>
