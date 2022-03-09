<template>
    <Navbar/>
    <section class="Banner">
      <div class="container">
        <div class="row">
        <div class="col-sm-6 col-md-6 col-lg-6 col-xl-6 box">
            <div class="card">
              <div class="card-header">
                <div class="card-title text-center" style="padding-top: 10px">
                    Ingreso Dolares
                </div>
              </div>
                <div class="card-body">
                  <div class="card-subtitle">
                    {{getTotalUsd(IncomeBs,IncomeUSD, Dolares).toFixed(2)}}<small>$</small>
                  </div>
                </div>
              </div>
          </div>
          <div class="col-sm-6 col-md-6 col-lg-6 col-xl-6 box">
            <div class="card">
              <div class="card-header">
                <div class="card-title text-center" style="padding-top: 10px">
                    Ingresos Bolivares
                </div>
              </div>
                <div class="card-body">
                  <div class="card-subtitle">
                    {{getTotalBs(IncomeUSD,IncomeBs, Dolares)}}<small>Bs</small>
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
              <ModalIncome/>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section class="DayBook">
        <div class="col-sm-12 col-md-12 col-lg-12">
          <div class="card">
            <div class="card-header">
              Libro Diario
            </div>
            <div class="card-body div-card">
                <div class="card-search ">
                    <input class="datefield" type="date">
                    <button class="search">Search</button>
                </div>
              <table class="table">
                  <thead>
                    <tr>
                      <th scope="col">Id</th>
                      <th scope="col">Nombre</th>
                      <th scope="col">Tipo Ingreso</th>
                      <th scope="col">Tipo Moneda</th>
                      <th scope="col">Tipo Banco</th>
                      <th scope="col">Monto</th>
                      <th scope="col">Cambio</th>
                      <th scope="col">Fecha</th>
                      <th scope="col">Accion</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="Income in Income" :key="Income.id">
                      <th scope="row">{{Income.id}}</th>
                      <td>{{Income.name}}</td>
                      <td>{{Income.typeIncome}}</td>
                      <td>{{Income.typeMoney}}</td>
                      <td>{{Income.typeBank}}</td>
                      <td>{{Income.price}}</td>
                      <td>{{ getCambioTotal(Dolares, Income).toFixed(2) }}</td>
                      <td>{{Income.date}}</td>
                      <td><router-link class="btn btn-danger" :to="{ name: 'IncomeDelete', params: {Id: Income.id} }">Eliminar</router-link></td>
                    </tr>
                  </tbody>
                </table>
            </div>
          </div>
        </div>
      </section>
    <section class="BodyGraph">
      <div class="container-fluid">
        <div class="row">
          <div class="col-sm-12 col-md-12 col-lg-12">
              <div class="card-body">
                <Chart/>
              </div>
            </div>
          </div>
        </div>
    </section>
    <section class="GraphPart">
        <div class="container-fluid">
            <div class="row">
                <div class="col-sm-6 col-md-6 col-lg-6">
                    <div class="card">
                        <div class="card-header">
                            Porcentaje de Ingresos
                        </div>
                        <div class="card-body">
                            <Chart1/>
                        </div>
                    </div>
                </div>
                <div class="col-sm-6 col-md-6 col-lg-6">
                    <div class="card">
                        <div class="card-header">
                            Ingresos Semanales
                        </div>
                        <div class="card-body">
                            <BarChart/>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <section class="Mayor">
      <div class="container-fluid">
        <div class="row">
          <div class="col-sm-6 col-md-6 col-lg-6">
            <div class="card">
              <div class="card-header">
                Tabla de Ganancias
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
                    <tr v-for="CodeIncome in CodeIncome" :key="CodeIncome.id">
                      <th scope="row">{{CodeIncome.id}}</th>
                      <td>{{CodeIncome.name}}</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
          <div class="col-sm-6 col-md-6 col-lg-6">
            <div class="card">
              <div class="card-header">
                Grafico Ingresos
              </div>
              <div class="card-body">
                <ChartCircle/>
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
import Chart from '../components/Graph/chartline.vue'
import Chart1 from '../components/Graph/chartline1.vue'
import BarChart from '../components/Graph/BarChar.vue'
import ChartCircle from '../components/Graph/PorcentGraph.vue'
import ModalIncome from '../components/IncomePopup/Popup2.vue'
import axios from 'axios'

export default {
	name: 'Home',
	components: {
		Navbar,
		Footer,
		Chart,
		Chart1,
		BarChart,
		ChartCircle,
		ModalIncome

	},
	data () {
		return {
			Income: [],
			Dolares: [],
			IncomeUSD: [],
			IncomeBs: [],
			CodeIncome: [],
		}
	},
	mounted () {
		axios.get('http://127.0.0.1:8000/Income/')
			.then(response => {
				console.log('Code Expenses api has received data')
				this.Income = response.data
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
		axios.get('http://localhost:8000/Income/usd')
			.then(response => {
				console.log('Code Expenses api has received data')
				this.IncomeUSD = response.data
			})
			.catch(err => {
				console.log(err)
			})
		axios.get('http://localhost:8000/Income/bs')
			.then(response => {
				console.log('Code Expenses api has received data')
				this.IncomeBs = response.data
			})
			.catch(err => {
				console.log(err)
			})
		axios.get('http://localhost:8000/CodeIncome/')
			.then(response => {
				console.log('Code Expenses api has received data')
				this.CodeIncome = response.data
			})
			.catch(err => {
				console.log(err)
			})
	},
	methods: {
		getCambioTotal(Dolares, Income) {
			if (Income.typeMoney == "USD"){

				return Income.price * Dolares.promedio_real

			} else if (Income.typeMoney == "BS"){

				return Income.price / Dolares.promedio_real

			}
		},
		getTotalBs(IncomeBs,IncomeUSD, Dolares){
			const IncomeTotalUSD = IncomeUSD.map(item => item.price).reduce((prev, curr) => prev + curr * Dolares.promedio_real, 0);
			const IncomeTotalBS = IncomeBs.map(item => item.price).reduce((prev, curr) => prev + curr, 0);
			return IncomeTotalUSD + IncomeTotalBS
		},
		getTotalUsd(IncomeBs,IncomeUSD, Dolares){
			const IncomeTotalUSD = IncomeUSD.map(item => item.price).reduce((prev, curr) => prev + curr, 0);
			const IncomeTotalBS = IncomeBs.map(item => item.price).reduce((prev, curr) => prev + curr / Dolares.promedio_real, 0);
			return IncomeTotalUSD + IncomeTotalBS
		}
	}
}
</script>
