<template>
  <LineChart
    :chart-data="data"
    :options="options"
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
const dataValues1 = ref([12, 14, 16, 18, 11, 13, 15, 12, 10, 15, 11, 12])
const dataValues = ref([10, 18, 10, 12, 11, 16, 11, 19, 11, 15, 16, 16])
const data = computed(() => ({
	labels: ['Jan', 'Mar', 'May', 'July', 'Sep', 'Dice'],
	datasets: [
		{
			label: 'Ingresos',
			data: dataValues1.value,
			backgroundColor: '#e44cc4',
			borderColor: '#e44cc4'
		},
		{
			label: 'Gastos',
			data: dataValues.value,
			backgroundColor: '#1cc88a',
			borderColor: '#1cc88a'

		}
	]
}))
const options = ref({
	plugins: {
		title: {
			text: 'Balance Dolares y Bolivares',
			color: 'rgb(228, 76, 196)'

		}
	}
})
</script>
