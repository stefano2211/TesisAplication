<template>
  <BarChart
    :chart-data="data"
    css-classes="chart-container"
  />
</template>

<script setup>
import pattern from 'patternomaly'
import { ref, computed } from 'vue'
import { BarChart } from 'vue-chart-3'
import {
	Chart,
	BarController,
	CategoryScale,
	LinearScale,
	BarElement
} from 'chart.js'
Chart.register(BarController, CategoryScale, LinearScale, BarElement)
const dataValues = ref([
	[1, 3, 5, 7, 2, 4, 6],
	[1, 5, 2, 6, 3, 7, 4]
])
const data = computed(() => ({
	labels: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
	datasets: [
		{
			label: 'Foo',
			data: dataValues.value[0],
			backgroundColor: pattern.draw('dash', '#268bd2')
		}

	]
}))

</script>
