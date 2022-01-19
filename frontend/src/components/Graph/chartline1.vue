<template>
  <LineChart
    :chart-data="data"
    css-classes="chart-container"
  />
</template>

<script setup>
import { ref, computed } from 'vue'
import { LineChart } from 'vue-chart-3'
import {
	Chart,
	LineController,
	CategoryScale,
	LinearScale,
	PointElement,
	LineElement
} from 'chart.js'
Chart.register(
	LineController,
	CategoryScale,
	LinearScale,
	PointElement,
	LineElement
)

const dataValues = ref([10, 18, 10, 12, 11, 16, 11, 19, 11, 15, 16, 16])
const data = computed(() => ({
	labels: ['Jan', 'Mar', 'May', 'July', 'Sep', 'Dice'],
	datasets: [
		{
			label: 'Gastos',
			data: dataValues.value,
			backgroundColor: '#1cc88a',
			borderColor: '#1cc88a'

		}
	]
}))

</script>
