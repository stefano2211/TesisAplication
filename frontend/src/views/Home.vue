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
                    {{getTotal(CodeBankUSD, CodeBankBS, ExpensesType, ExpensesTypebs, IncomeUSD, IncomeBs, Dolares).toFixed(2)}}<small>Bs</small>
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
                    {{getTotalUSD(CodeBankUSD, CodeBankBS, ExpensesType, ExpensesTypebs, IncomeUSD, IncomeBs, Dolares).toFixed(2)}}
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
                  Ganancias en Bolivares
                  <div class="card-subtitle">
                    {{getTotalBsIncome(IncomeBs,IncomeUSD, Dolares)}}Bs
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-sm-3 col-md-3 col-lg-3">
            <div class="card won">
              <div class="card-body">
                <div class="card-title">
                    Ganancias en Dolares
                  <div class="card-subtitle">
                    {{getTotalUsdIncome(IncomeBs,IncomeUSD, Dolares).toFixed(2)}}$
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-sm-3 col-md-3 col-lg-3">
            <div class="card loss">
              <div class="card-body">
                <div class="card-title">
                    Gastos en Bolivares
                  <div class="card-subtitle">
                    {{getTotalBs(ExpensesType,ExpensesTypebs, Dolares)}}
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-sm-3 col-md-3 col-lg-3">
            <div class="card loss">
              <div class="card-body">
                <div class="card-title">
                    Gastos en Dolares
                  <div class="card-subtitle">
                    {{getTotalUsd(ExpensesType,ExpensesTypebs, Dolares).toFixed(2)}}
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
			CodeIncome: [],
			CodeBankUSD: [],
			CodeBankBS: [],
			ExpensesType: [],
			ExpensesTypebs: [],
			IncomeUSD: [],
			IncomeBs: [],
			Dolares: [],
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
		axios.get('http://localhost:8000/Expenses/usd')
			.then(response => {
				console.log('Code Expenses api has received data')
				this.ExpensesType = response.data
			})
			.catch(err => {
				console.log(err)
			})
		axios.get('http://localhost:8000/Expenses/bs')
			.then(response => {
				console.log('Code Expenses api has received data')
				this.ExpensesTypebs = response.data
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
		axios.get('https://s3.amazonaws.com/dolartoday/data.json')
			.then(response => {
				console.log('Api has received data')
				this.Dolares = response.data.USD
			})
			.catch(err => {
				console.log(err)
			})

	},
	methods: {
		getTotalBsIncome(IncomeBs,IncomeUSD, Dolares){
			const IncomeTotalUSD = IncomeUSD.map(item => item.price).reduce((prev, curr) => prev + curr * Dolares.promedio_real, 0);
			const IncomeTotalBS = IncomeBs.map(item => item.price).reduce((prev, curr) => prev + curr, 0);
			return IncomeTotalUSD + IncomeTotalBS
		},
		getTotalUsdIncome(IncomeBs,IncomeUSD, Dolares){
			const IncomeTotalUSD = IncomeUSD.map(item => item.price).reduce((prev, curr) => prev + curr, 0);
			const IncomeTotalBS = IncomeBs.map(item => item.price).reduce((prev, curr) => prev + curr / Dolares.promedio_real, 0);
			return IncomeTotalUSD + IncomeTotalBS
		},
		getTotalBs(ExpensesType,ExpensesTypebs, Dolares){
			const ExpensesTotalUSD = ExpensesType.map(item => item.price).reduce((prev, curr) => prev + curr * Dolares.promedio_real, 0);
			const ExpensesTotalBS = ExpensesTypebs.map(item => item.price).reduce((prev, curr) => prev + curr, 0);
			return ExpensesTotalUSD + ExpensesTotalBS
		},
		getTotalUsd(ExpensesType,ExpensesTypebs, Dolares){
			const ExpensesTotalUSD = ExpensesType.map(item => item.price).reduce((prev, curr) => prev + curr, 0);
			const ExpensesTotalBS = ExpensesTypebs.map(item => item.price).reduce((prev, curr) => prev + curr / Dolares.promedio_real, 0);
			return ExpensesTotalUSD + ExpensesTotalBS
		},
		getTotal(CodeBankUSD, CodeBankBS, ExpensesType, ExpensesTypebs, IncomeUSD, IncomeBs, Dolares){
			const IncomeTotalUSD = IncomeUSD.map(item => item.price).reduce((prev, curr) => prev + curr * Dolares.promedio_real, 0);
			const IncomeTotalBS = IncomeBs.map(item => item.price).reduce((prev, curr) => prev + curr, 0);
			const IncomeTotalBs = IncomeTotalUSD + IncomeTotalBS

			const BankTotalUSD = CodeBankUSD.map(item => item.price).reduce((prev, curr) => prev + curr * Dolares.promedio_real, 0);
			const BankTotalBS = CodeBankBS.map(item => item.price).reduce((prev, curr) => prev + curr, 0);
			const BankTotalBs = BankTotalUSD + BankTotalBS

			const ExpensesTotalUSD = ExpensesType.map(item => item.price).reduce((prev, curr) => prev + curr * Dolares.promedio_real, 0);
			const ExpensesTotalBS = ExpensesTypebs.map(item => item.price).reduce((prev, curr) => prev + curr, 0);
			const ExpensesTotalBs = ExpensesTotalUSD + ExpensesTotalBS

			const resta = IncomeTotalBs - ExpensesTotalBs
			const resultado = resta + BankTotalBs
			return resultado
		},
		getTotalUSD(CodeBankUSD, CodeBankBS, ExpensesType, ExpensesTypebs, IncomeUSD, IncomeBs, Dolares){
			const IncomeTotalUSD = IncomeUSD.map(item => item.price).reduce((prev, curr) => prev + curr * Dolares.promedio_real, 0);
			const IncomeTotalBS = IncomeBs.map(item => item.price).reduce((prev, curr) => prev + curr, 0);
			const IncomeTotalBs = IncomeTotalUSD + IncomeTotalBS

			const BankTotalUSD = CodeBankUSD.map(item => item.price).reduce((prev, curr) => prev + curr * Dolares.promedio_real, 0);
			const BankTotalBS = CodeBankBS.map(item => item.price).reduce((prev, curr) => prev + curr, 0);
			const BankTotalBs = BankTotalUSD + BankTotalBS

			const ExpensesTotalUSD = ExpensesType.map(item => item.price).reduce((prev, curr) => prev + curr * Dolares.promedio_real, 0);
			const ExpensesTotalBS = ExpensesTypebs.map(item => item.price).reduce((prev, curr) => prev + curr, 0);
			const ExpensesTotalBs = ExpensesTotalUSD + ExpensesTotalBS

			const resta = IncomeTotalBs - ExpensesTotalBs
			const resultado = resta + BankTotalBs
			return resultado / Dolares.promedio_real
		}
	}
}
</script>
