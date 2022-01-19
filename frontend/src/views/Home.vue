<template>
  <Navbar/>
    <section class="Banner">
      <div class="container">
        <div class="row">
          <div class="col-sm-4 col-md-4 col-lg-4 col-xl-4 box">
            <div class="card">
              <div class="card-header">
                <div class="card-title text-center" style="padding-top: 10px">
                    Balance Total Bolivares
                </div>
              </div>
                <div class="card-body">
                  <div class="card-subtitle">
                    21,38 <small>Bs</small>
                  </div>
                </div>
              </div>
          </div>
          <div class="col-sm-4 col-md-4 col-lg-4 col-xl-4 box">
            <div class="card">
              <div class="card-header">
                <div class="card-title text-center" style="padding-top: 10px">
                    Profit del Mes
                </div>
              </div>
                <div class="card-body">
                  <div class="card-subtitle">
                    3,14$ - 23Bs
                  </div>
                </div>
            </div>
          </div>
          <div class="col-sm-4 col-md-4 col-lg-4 col-xl-4 box">
            <div class="card">
              <div class="card-header">
                <div class="card-title text-center" style="padding-top: 10px">
                    Balance Total Dolares
                </div>
              </div>
                <div class="card-body">
                  <div class="card-subtitle">
                    21,38$
                  </div>
                </div>
            </div>
          </div>
          </div>
        </div>
    </section>
    <section class="card-section">
      <div class="container-fluid">
        <div class="row">
          <div class="col-sm-3 col-md-3 col-lg-3">
            <div class="card won">
              <div class="card-body">
                <div class="card-title">
                  Ganancias mes en Dolares
                  <div class="card-subtitle">
                    25$
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-sm-3 col-md-3 col-lg-3">
            <div class="card won">
              <div class="card-body">
                <div class="card-title">
                    Gastos mes en Dolares
                  <div class="card-subtitle">
                    25Bs
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-sm-3 col-md-3 col-lg-3">
            <div class="card loss">
              <div class="card-body">
                <div class="card-title">
                    Gastos mes en Bolivares
                  <div class="card-subtitle">
                    25Bs
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-sm-3 col-md-3 col-lg-3">
            <div class="card loss">
              <div class="card-body">
                <div class="card-title">
                    Gastos mes en Dolares
                  <div class="card-subtitle">
                    25$
                  </div>
                </div>
              </div>
            </div>
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
    <section class="Mayor">
      <div class="container-fluid">
        <div class="row">
          <div class="col-sm-6 col-md-6 col-lg-6">
            <div class="card">
              <div class="card-header">
                Bank Table
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
                Grafico Bancos
              </div>
              <div class="card-body">
                <ChartCircle/>
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
      <section class="Mayor">
      <div class="container-fluid">
        <div class="row">
          <div class="col-sm-6 col-md-6 col-lg-6">
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
                      <th scope="col">Monto</th>
                      <th scope="col">Tipo Moneda</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="Bank in Bank" :key="Bank.id">
                      <th scope="row">{{Bank.id}}</th>
                      <td>{{Bank.name}}</td>
                      <td>{{Bank.price}}</td>
                      <td>{{Bank.type}}</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
          <div class="col-sm-6 col-md-6 col-lg-6">
            <div class="card">
              <div class="card-header">
                Grafico Ganacias
              </div>
              <div class="card-body">
                <ChartCircle/>
              </div>
            </div>
          </div>
        </div>
      </div>
      </section>
      <section class="DayBook">
        <div class="col-sm-12 col-md-12 col-lg-12">
          <div class="card">
            <div class="card-header">
              Libro Diario Gastos
            </div>
            <div class="card-body div-card">
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
                    <tr v-for="Expenses in Expenses" :key="Expenses.id">
                      <th scope="row">{{Expenses.id}}</th>
                      <td>{{Expenses.name}}</td>
                      <td>{{Expenses.typeMoney}}</td>
                      <td>{{Expenses.typeBank}}</td>
                      <td>{{Expenses.price}}</td>
                      <td>{{Expenses.date}}</td>
                    </tr>
                  </tbody>
                </table>
            </div>
          </div>
        </div>
      </section>
      <section class="DayBook">
        <div class="col-sm-12 col-md-12 col-lg-12">
          <div class="card">
            <div class="card-header">
              Libro Diario Ingresos
            </div>
            <div class="card-body div-card">
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
                    <tr v-for="Income in Income" :key="Income.id">
                      <th scope="row">{{Income.id}}</th>
                      <td>{{Income.name}}</td>
                      <td>{{Income.typeMoney}}</td>
                      <td>{{Income.typeBank}}</td>
                      <td>{{Income.price}}</td>
                      <td>{{Income.date}}</td>
                    </tr>
                  </tbody>
                </table>
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
import ChartCircle from '../components/Graph/PorcentGraph.vue'
import axios from 'axios'

export default {
	name: 'Home',
	components: {
		Navbar,
		Footer,
		Chart,
		ChartCircle
	},
	data () {
		return {
			Income: [],
			Expenses: [],
			Bank: [],
			CodeIncome: []
		}
	},
	computed: {

	},
	mounted () {
		/* Diary move */
		axios.get('http://localhost:8000/Expenses/')
			.then(response => {
				console.log('Code Expenses api has received data')
				this.Expenses = response.data
			})
			.catch(err => {
				console.log(err)
			})
		axios.get('http://127.0.0.1:8000/Income/')
			.then(response => {
				console.log('Code Expenses api has received data')
				this.Income = response.data
			})
			.catch(err => {
				console.log(err)
			})
		/* Bank Table */
		axios.get('http://localhost:8000/CodesBank/')
			.then(response => {
				console.log('Code Expenses api has received data')
				this.Bank = response.data
			})
			.catch(err => {
				console.log(err)
			})
		/* Code Income */
		axios.get('http://localhost:8000/CodeIncome/')
			.then(response => {
				console.log('Code Expenses api has received data')
				this.CodeIncome = response.data
			})
			.catch(err => {
				console.log(err)
			})
	}
}
</script>
