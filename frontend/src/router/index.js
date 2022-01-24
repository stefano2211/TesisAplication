import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import CodeBank from '../views/Bankview.vue'
import CodeIncome from '../views/IncomeView.vue'
import CodeSpend from '../views/SpendView.vue'
import Spend from '../views/GastoView.vue'
import Income from '../views/IngresoView.vue'
import ExpensesDelete from '../views/ExpensesDelete.vue'
import IncomeDelete from '../views/IncomeDelete.vue'

const routes = [
	{
		path: '/',
		name: 'Home',
		component: Home
	},
	{
		path: '/Code/Bank',
		name: 'CodeBank',
		component: CodeBank
	},
	{
		path: '/Code/Income',
		name: 'CodeIncome',
		component: CodeIncome
	},
	{
		path: '/Code/Spend',
		name: 'CodeSpend',
		component: CodeSpend
	},
	{
		path: '/Gastos',
		name: 'Spend',
		component: Spend
	},
	{
		path: '/Ingresos',
		name: 'Income',
		component: Income
	},
	{
		path: '/Gasto/:Id/Eliminar',
		name: 'ExpensesDelete',
		component: ExpensesDelete
	},
	{
		path: '/Ingresos/:Id/Eliminar',
		name: 'IncomeDelete',
		component: IncomeDelete
	},
]

const router = createRouter({
	history: createWebHistory(process.env.BASE_URL),
	routes
})

export default router
