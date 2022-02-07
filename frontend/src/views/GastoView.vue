<template>
    <Navbar/>
    <section class="Banner">
      <div class="container">
        <div class="row">
        <div class="col-sm-6 col-md-6 col-lg-6 col-xl-6 box">
            <div class="card">
              <div class="card-header">
                <div class="card-title text-center" style="padding-top: 10px">
                    Gastos Dolares
                </div>
              </div>
                <div class="card-body">
                  <div class="card-subtitle">
                    210,38<small>$</small>
                  </div>
                </div>
              </div>
          </div>
          <div class="col-sm-6 col-md-6 col-lg-6 col-xl-6 box">
            <div class="card">
              <div class="card-header">
                <div class="card-title text-center" style="padding-top: 10px">
                    Gastos Bolivares
                </div>
              </div>
                <div class="card-body">
                  <div class="card-subtitle">
                        <small>Bs</small>
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
    <section class="DayBook">
        <div class="col-sm-12 col-md-12 col-lg-12">
          <div class="card">
            <div class="card-header">
              Libro Diario
            </div>
            <div class="card-body div-card">
                <div class="card-search">
                    <input class="datefield" type="date">
                    <button class="search">Search</button>
                </div>
              <table class="table">
                  <thead>
                    <tr>
                      <th scope="col">Id</th>
                      <th scope="col">Name</th>
                      <th scope="col">Tipo de Gasto</th>
                      <th scope="col">Tipo Moneda</th>
                      <th scope="col">Tipo Banco</th>
                      <th scope="col">Monto</th>
                      <th scope="col">Cambio</th>
                      <th scope="col">Fecha</th>
                      <th scope="col">Accion</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="Expenses in Expenses" :key="Expenses.id">
                      <th scope="row">{{Expenses.id}}</th>
                      <td>{{Expenses.name}}</td>
                      <td>{{Expenses.typeExpenses}}</td>
                      <td>{{Expenses.typeMoney}}</td>
                      <td>{{Expenses.typeBank}}</td>
                      <td>{{Expenses.price}}</td>
                      <td>{{ getCambioTotal(Dolares, Expenses).toFixed(2) }}</td>
                      <td>{{Expenses.date}}</td>
                      <td><router-link class="btn btn-danger" :to="{ name: 'ExpensesDelete', params: {Id: Expenses.id} }">Eliminar</router-link></td>
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
                            Porcentaje de Gastos
                        </div>
                        <div class="card-body">
                            <Chart1/>
                        </div>
                    </div>
                </div>
                <div class="col-sm-6 col-md-6 col-lg-6">
                    <div class="card">
                        <div class="card-header">
                            Gastos Semanales
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
                      <th scope="col">#</th>
                      <th scope="col">First</th>
                      <th scope="col">Last</th>
                      <th scope="col">Handle</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <th scope="row">1</th>
                      <td>Mark</td>
                      <td>Otto</td>
                      <td>@mdo</td>
                    </tr>
                    <tr>
                      <th scope="row">2</th>
                      <td>Jacob</td>
                      <td>Thornton</td>
                      <td>@fat</td>
                    </tr>
                    <tr>
                      <th scope="row">3</th>
                      <td>Larry</td>
                      <td>the Bird</td>
                      <td>@twitter</td>
                    </tr>
                    <tr>
                      <th scope="row">3</th>
                      <td>Larry</td>
                      <td>the Bird</td>
                      <td>@twitter</td>
                    </tr>
                    <tr>
                      <th scope="row">3</th>
                      <td>Larry</td>
                      <td>the Bird</td>
                      <td>@twitter</td>
                    </tr>
                    <tr>
                      <th scope="row">3</th>
                      <td>Larry</td>
                      <td>the Bird</td>
                      <td>@twitter</td>
                    </tr>
                    <tr>
                      <th scope="row">3</th>
                      <td>Larry</td>
                      <td>the Bird</td>
                      <td>@twitter</td>
                    </tr>
                    <tr>
                      <th scope="row">3</th>
                      <td>Larry</td>
                      <td>the Bird</td>
                      <td>@twitter</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
          <div class="col-sm-6 col-md-6 col-lg-6">
            <div class="card">
              <div class="card-header">
                Grafico Gastos
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
import Modal from '../components/CodeSpend/Popup2.vue'
import axios from 'axios'


export default {
	name: 'Spend',
	components: {
		Navbar,
		Footer,
		Chart,
		Chart1,
		BarChart,
		ChartCircle,
		Modal
	},
	data () {
		return {
			Expenses: [],
			Dolares: [],
      ExpensesType: [],
		}
	},
	mounted () {


		axios.get('http://localhost:8000/Expenses/')
			.then(response => {
				console.log('Code Expenses api has received data')
				this.Expenses = response.data
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
    axios.get('http://localhost:8000/Expenses/usd')
			.then(response => {
				console.log('Code Expenses api has received data')
				this.ExpensesType = response.data
			})
			.catch(err => {
				console.log(err)
			})
	},
	methods: {
		getCambioTotal(Dolares, Expenses) {
			if (Expenses.typeMoney == "USD"){

				return Expenses.price * Dolares.promedio_real

			} else if (Expenses.typeMoney == "BS"){

				return Expenses.price / Dolares.promedio_real

			}
		},
	}
}
</script>
