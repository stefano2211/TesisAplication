<template>
  <Navbar/>
  <section class="Banner">
      <div class="container">
        <div class="row">
          <div class="col-sm-6 col-md-6 col-lg-6 col-xl-6 box">
            <div class="card">
              <div class="card-header">
                <div class="card-title text-center" style="padding-top: 10px">
                    Balance Total Bolivares
                </div>
              </div>
                <div class="card-body">
                  <div class="card-subtitle">
                    {{getTotalBs(CodeBankBS,CodeBankUSD, Dolares)}}<small>Bs</small>
                  </div>
                </div>
              </div>
          </div>
          <div class="col-sm-6 col-md-6 col-lg-6 col-xl-6 box">
            <div class="card">
              <div class="card-header">
                <div class="card-title text-center" style="padding-top: 10px">
                    Balance Total Dolares
                </div>
              </div>
                <div class="card-body">
                  <div class="card-subtitle">
                    {{getTotalUsd(CodeBankBS,CodeBankUSD, Dolares).toFixed(2)}}
                  </div>
                </div>
            </div>
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
              <Modal/>
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
                      <th scope="col">Name</th>
                      <th scope="col">Price</th>
                      <th scope="col">Cambio</th>
                      <th scope="col">Tipo Moneda</th>
                      <th scope="col">Accion</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="Bank in Bank" :key="Bank.id">
                      <th scope="row">{{Bank.id}}</th>
                      <td>{{Bank.name}}</td>
                      <td>{{Bank.price}}</td>
                      <td>{{ getCambioTotal(Dolares, Bank).toFixed(2) }}</td>
                      <td>{{Bank.type}}</td>
                      <td><router-link class="btn btn-danger" :to="{ name: 'BankDelete', params: {Id: Bank.id} }">Eliminar</router-link></td>
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
import Modal from '../components/Bankpoup/Popup.vue'
import axios from 'axios'

export default {
	name: 'CodeBank',
	components: {
		Navbar,
		Footer,
		Modal
	},
	data () {
		return {
			Bank: [],
			Dolares: [],
			CodeBankUSD: [],
			CodeBankBS: []
		}
	},
	mounted () {
		axios.get('http://localhost:8000/CodesBank/')
			.then(response => {
				console.log('Code Expenses api has received data')
				this.Bank = response.data
			})
			.catch(err => {
				console.log(err)
			})
		axios.get('https://s3.amazonaws.com/dolartoday/data.json')
			.then(response => {
				console.log('Api has received data')
				this.Dolares = response.data.USD
			})
			.catch(err => {
				console.log(err)
			})
		axios.get('http://localhost:8000/Bank/usd')
			.then(response => {
				console.log('Code Expenses api has received data')
				this.CodeBankUSD = response.data
			})
			.catch(err => {
				console.log(err)
			})
		axios.get('http://localhost:8000/Bank/bs')
			.then(response => {
				console.log('Code Expenses api has received data')
				this.CodeBankBS = response.data
			})
			.catch(err => {
				console.log(err)
			})

	},
	methods: {
		getCambioTotal(Dolares, Bank) {
			if (Bank.type == "Dolares"){

				return Bank.price * Dolares.promedio_real

			} else if (Bank.type == "Bolivares"){

				return Bank.price / Dolares.promedio_real

			}
		},
		getTotalBs(CodeBankBS,CodeBankUSD, Dolares){
			const BankTotalUSD = CodeBankUSD.map(item => item.price).reduce((prev, curr) => prev + curr * Dolares.promedio_real, 0);
			const BankTotalBS = CodeBankBS.map(item => item.price).reduce((prev, curr) => prev + curr, 0);
			const total = BankTotalUSD + BankTotalBS
			return total
		},
		getTotalUsd(CodeBankBS,CodeBankUSD, Dolares){
			const BankTotalUSD = CodeBankUSD.map(item => item.price).reduce((prev, curr) => prev + curr, 0);
			const BankTotalBS = CodeBankBS.map(item => item.price).reduce((prev, curr) => prev + curr / Dolares.promedio_real, 0);
			const total = BankTotalUSD + BankTotalBS
			return total
		}
	}

}
</script>

}
