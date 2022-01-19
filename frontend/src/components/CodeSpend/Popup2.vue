<template>
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Gastos</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <form @submit="onSubmit">
          <div class="mb-3">
            <label for="recipient-name" class="col-form-label">Nombre</label>
            <input type="text" class="form-control" id="recipient-name" v-model.trim="form.name">
          </div>
          <div class="mb-3">
            <label for="message-text" class="col-form-label">Descripcion</label>
            <textarea class="form-control" id="message-text" v-model.trim="form.description"></textarea>
          </div>
          <div class="mb-3">
            <label for="recipient-name" class="col-form-label">Monto Ingresado</label>
            <input type="text" class="form-control" id="recipient-name" v-model.trim="form.price">
          </div>
          <div class="mb-3">
            <label for="recipient-name" class="col-form-label">Tipo de Cuenta</label>
            <select name="select" type="text" class="form-control" id="recipient-name" v-model.trim="form.typeBank">
              <option v-for="Bank in Bank" :key="Bank.id">{{Bank.name}}</option>
            </select>
          </div>
          <div class="mb-3">
            <label for="recipient-name" class="col-form-label">Tipo de Ingreso</label>
            <select name="select" type="text" class="form-control" id="recipient-name" v-model.trim="form.typeExpenses">
              <option v-for="Expenses in Expenses" :key="Expenses.id">{{Expenses.name}}</option>
            </select>
          </div>
          <div class="mb-3">
            <label for="recipient-name" class="col-form-label">Tipo de Moneda</label>
            <select name="select" type="text" class="form-control" id="recipient-name" v-model.trim="form.typeMoney">
              <option>USD</option>
              <option>BS</option>
            </select>
          </div>
          <div class="mb-3">
            <label for="recipient-name" class="col-form-label">Fecha</label>
            <input type="date" class="form-control" id="recipient-name" v-model.trim="form.date">
          </div>
          <div class="mb-3">
            <label for="recipient-name" class="col-form-label">Cambio</label>
            <select name="select" type="text" class="form-control" id="recipient-name" v-model.trim="form.dolar">
              <option>{{Dolares.promedio_real}}</option>
            </select>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="submit" class="btn btn-success">Send message</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</div>
</template>
<script>
import axios from 'axios'
import swal from 'sweetalert'

export default {
	data () {
		return {
			form: {
				name: '',
				description: '',
				price: '',
				typeBank: '',
				typeExpenses: '',
				typeMoney: '',
				date: '',
				dolar: ''
			},
			Bank: [],
			Expenses: [],
			Dolares: []
		}
	},
	methods: {
		onSubmit (e) {
			e.preventDefault()

			const path = 'http://127.0.0.1:8000/Expenses/'
			axios.post(path, this.form).then((response) => {
				this.form.name = response.data.name
				this.form.description = response.data.description
				this.form.price = response.data.price
				this.form.typeBank = response.data.typeBank
				this.form.typeExpenses = response.data.typeExpenses
				this.form.typeMoney = response.data.typeMoney
				this.form.date = response.data.date
				this.form.dolar = response.data.dolar
				swal('Libro creado exitosamente', '', 'success')
			})
				.catch((error) => {
					console.log(error)
				})
		}
	},
	mounted () {
		axios.get('http://127.0.0.1:8000/CodesBank/')
			.then(response => {
				console.log('Code bank api has received data')
				this.Bank = response.data
			})
			.catch(err => {
				console.log(err)
			})

		axios.get('http://127.0.0.1:8000/CodeSpend/')
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
	}
}

</script>
