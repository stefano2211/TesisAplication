<template>
    <Navbar/>
    <section class="Banner">
      <div class="container">
        <div class="row">
            <div class="col-sm-12 col-md-12 col-lg-12 col-xl-12 box">
                <h1>Categoria Gastos</h1>
            </div>
          </div>
        </div>
    </section>
    <section class="AddButto">
      <div class="container-fluid">
        <div class="row">
          <div class="col-sm-12 col-md-12 col-lg-12">
            <div class="io">
              <button type="button" data-bs-toggle="modal" data-bs-target="#exampleModal" data-bs-whatever="@mdo" class="btn btn-success" placeholder="Añadir"><i class="bi bi-plus"></i></button>
              <ModelSpend/>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section class="BankCategory">
      <div class="container-fluid">
        <div class="row">
          <div class="col-sm-12 col-md-12 col-lg-12">
            <div class="card">
              <div class="card-header">
                Bank Table
              </div>
              <div class="card-body div-card">
                <table class="table">
                  <thead>
                    <tr>
                      <th scope="col">Id</th>
                      <th scope="col">Nombre</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="Expenses in Expenses" :key="Expenses.id">
                      <th scope="row">{{Expenses.id}}</th>
                      <td>{{Expenses.name}}</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <Footer/>
</template>
<script>
import Navbar from '../components/Navbar.vue'
import Footer from '../components/Footer.vue'
import ModelSpend from '../components/CodeSpend/Popup.vue'
import axios from 'axios'

export default {
	name: 'CodeSpend',
	components: {
		Navbar,
		Footer,
		ModelSpend
	},
	data () {
		return {
			Expenses: []
		}
	},
	mounted () {
		axios.get('http://localhost:8000/CodeSpend/')
			.then(response => {
				console.log('Code Expenses api has received data')
				this.Expenses = response.data
			})
			.catch(err => {
				console.log(err)
			})
	}
}
</script>
