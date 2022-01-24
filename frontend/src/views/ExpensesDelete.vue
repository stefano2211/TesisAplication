<template>
<Navbar/>
	<section class="Banner">
        <div class="container">
        <div class="row">
            <div class="col-sm-12 col-md-12 col-lg-12 col-xl-12 box">
                <h1>Eliminar Gasto</h1>
            </div>
            </div>
        </div>
    </section>
	<section class="card-information">
		<div class="container">
			<div class="row">
				<div class="col-sm-12 col-md-12 col-lg-12 col-xl-12 box">
					<div class="card">
						<div class="card-header">
							Datos a borrar
						</div>
						<div class="card-body body">
							<table class="table">
								<thead>
									<tr>
									<th scope="col">Id</th>
									<th scope="col">Name</th>
									<th scope="col">Tipo Moneda</th>
									<th scope="col">Tipo Banco</th>
									<th scope="col">Monto</th>
									<th scope="col">Fecha</th>
									</tr>
								</thead>
								<tbody>
									<tr>
									<th scope="row">{{Expenses.id}}</th>
									<td>{{Expenses.name}}</td>
									<td>{{Expenses.typeMoney}}</td>
									<td>{{Expenses.typeBank}}</td>
									<td>{{Expenses.price}}</td>
									<td>{{Expenses.date}}</td>
									</tr>
								</tbody>
							</table>
							<button type="button" class="btn btn-danger" v-on:click="deleteExpenses">Borrar</button>
							<router-link class="btn btn-primary" :to="{ name: 'Spend'}" style="margin:10px;">Volver</router-link>
						</div>
					</div>
				</div>
			</div>
		</div>
	</section>


<Footer/>
</template>

<script>
import axios from 'axios'
import swal from 'sweetalert'
import Navbar from '../components/Navbar.vue'
import Footer from '../components/Footer.vue'

export default {
	components:{
		Navbar,
		Footer,
	},
	data() {
		return {
			ExpensesId: this.$route.params.Id,
			Expenses: []
		}
	},
	methods: {
		getExpenses() {
			const path = 'http://localhost:8000/Expenses/' + `${this.ExpensesId}/`
			axios.get(path)
				.then((response) => {
					this.Expenses = response.data
				})
				.catch((error) => {
					console.log(error)
				})
		},
		deleteExpenses() {
			const path = 'http://localhost:8000/Expenses/' + `${this.ExpensesId}/`
			axios.delete(path)
				.then((data) => {
					console(data)
					this.$router.push({name: 'Spend'})
					swal('Se a borrado la info')
				})
				.catch((error) => {
					console.log(error)
					swal('Se a borrado la info')
				})
		}
	},
	created() {
		this.getExpenses()
	}
}
</script>