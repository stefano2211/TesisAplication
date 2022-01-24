<template>
<Navbar/>
	<section class="Banner">
        <div class="container">
        <div class="row">
            <div class="col-sm-12 col-md-12 col-lg-12 col-xl-12 box">
                <h1>Eliminar Ingreso</h1>
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
									<th scope="row">{{Income.id}}</th>
									<td>{{Income.name}}</td>
									<td>{{Income.typeMoney}}</td>
									<td>{{Income.typeBank}}</td>
									<td>{{Income.price}}</td>
									<td>{{Income.date}}</td>
									</tr>
								</tbody>
							</table>
							<button type="button" class="btn btn-danger" v-on:click="deleteIncome">Borrar</button>
							<router-link class="btn btn-primary" :to="{ name: 'Income'}" style="margin:10px;">Volver</router-link>
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
			IncomeId: this.$route.params.Id,
			Income: []
		}
	},
	methods: {
		getIncome() {
			const path = 'http://localhost:8000/Income/' + `${this.IncomeId}/`
			axios.get(path)
				.then((response) => {
					this.Income = response.data
				})
				.catch((error) => {
					console.log(error)
				})
		},
		deleteIncome() {
			const path = 'http://localhost:8000/Income/' + `${this.IncomeId}/`
			axios.delete(path)
				.then((data) => {
					console(data)
					this.$router.push({name: 'Income'})
					swal('Se a borrado la info')
				})
				.catch((error) => {
					console.log(error)
					swal('Se a borrado la info')
				})
		}
	},
	created() {
		this.getIncome()
	}
}
</script>