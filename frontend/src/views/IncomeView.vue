<template>
    <Navbar/>
    <section class="Banner">
      <div class="container">
        <div class="row">
            <div class="col-sm-12 col-md-12 col-lg-12 col-xl-12 box">
                <h1>Categoria Ingresos</h1>
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
              <ModalIncome/>
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
                      <th scope="col">Accion</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="Income in Income" :key="Income.id">
                      <th scope="row">{{Income.id}}</th>
                      <td>{{Income.name}}</td>
                      <td><router-link class="btn btn-danger" :to="{ name: 'CodeIncomeDelete', params: {Id: Income.id} }">Eliminar</router-link></td>
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
import ModalIncome from '../components/CodeIncomepopup/Popup.vue'
import axios from 'axios'

export default {
	name: 'CodeIncome',
	components: {
		Navbar,
		Footer,
		ModalIncome
	},
	data () {
		return {
			Income: []
		}
	},
	mounted () {
		axios.get('http://localhost:8000/CodeIncome/')
			.then(response => {
				console.log('Code Inncome api has received data')
				this.Income = response.data
			})
			.catch(err => {
				console.log(err)
			})
	}
}
</script>
