<template>
<Navbar/>
	<section class="Banner">
        <div class="container">
        <div class="row">
            <div class="col-sm-12 col-md-12 col-lg-12 col-xl-12 box">
                <h1>Eliminar Codigo Gasto</h1>
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
									</tr>
								</thead>
								<tbody>
									<tr>
									<th scope="row">{{Code.id}}</th>
									<td>{{Code.name}}</td>
									</tr>
								</tbody>
							</table>
							<button type="button" class="btn btn-danger" v-on:click="deleteCodeExpenses">Borrar</button>
							<router-link class="btn btn-primary" :to="{ name: 'CodeSpend'}" style="margin:10px;">Volver</router-link>
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
			CodeExpensesId: this.$route.params.Id,
			Code: []
		}
	},
	methods: {
		getCodeExpenses() {
			const path = 'http://localhost:8000/CodeSpend/' + `${this.CodeExpensesId}/`
			axios.get(path)
				.then((response) => {
					this.Code = response.data
				})
				.catch((error) => {
					console.log(error)
				})
		},
		deleteCodeExpenses() {
			const path = 'http://localhost:8000/CodeSpend/' + `${this.CodeExpensesId}/`
			axios.delete(path)
				.then((data) => {
					console(data)
					this.$router.push({name: 'CodeSpend'})
					swal('Se a borrado la info')
				})
				.catch((error) => {
					console.log(error)
					swal('Se a borrado la info')
				})
		}
	},
	created() {
		this.getCodeExpenses()
	}
}
</script>