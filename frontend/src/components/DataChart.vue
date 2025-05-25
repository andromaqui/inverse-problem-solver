<template>
  <div class="chart-container">
    <Line :data="chartData" :options="chartOptions" />
  </div>
</template>

<script setup>
import { Line } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title, Tooltip, Legend,
  PointElement, LineElement,
  LinearScale
} from 'chart.js'
import { computed } from 'vue'

ChartJS.register(Title, Tooltip, Legend, PointElement, LineElement, LinearScale)

const props = defineProps({
  x: Array,
  y: Array,
  modelPoints: Array
})

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: { display: false },
  },
  parsing: {
    xAxisKey: 'x',
    yAxisKey: 'y'
  },
  scales: {
    x: {
      type: 'linear',
      title: { display: true, text: 'X values' }
    },
    y: {
      title: { display: true, text: 'Y values' },
      beginAtZero: false
    }
  }
}

const chartData = computed(() => ({
  datasets: [
    {
      label: 'User Data',
      data: props.x.map((x, i) => ({ x, y: props.y[i] })),
      showLine: false,
      pointRadius: 5,
      borderColor: 'blue'
    },
    {
      label: 'Model Fit',
      data: props.modelPoints,
      showLine: true,
      pointRadius: 0,
      borderColor: 'red',
      borderWidth: 2
    }
  ]
}))
</script>

<style scoped>
.chart-container {
  width: 100%;
  max-width: 600px;
  height: 600px;
}
canvas {
  width: 100% !important;
  height: 100% !important;
}

</style>
