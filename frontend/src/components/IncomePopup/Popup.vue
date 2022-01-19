<template>
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Ingresos Template</h5>
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
				description: ''
			}
		}
	},
	methods: {
		onSubmit (e) {
			e.preventDefault()

			const path = 'http://127.0.0.1:8000/CodeIncome/'
			axios.post(path, this.form).then((response) => {
				this.form.name = response.data.name
				this.form.description = response.data.description
				swal('Libro creado exitosamente', '', 'success')
			})
				.catch((error) => {
					console.log(error)
				})
		}
	},
	created () {
	}

}

</script>
