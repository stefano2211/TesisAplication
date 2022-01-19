<template>
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Codigos Bancos</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <form @submit="onSubmit">
          <div class="mb-3">
            <label for="recipient-name" class="col-form-label">Nombre</label>
            <input type="text" class="form-control" id="recipient-name" v-model.trim="form.name">
          </div>
          <div class="mb-3">
            <label for="recipient-name" class="col-form-label">Monto</label>
            <input type="text" class="form-control" id="recipient-name" v-model.trim="form.price">
          </div>
          <div class="mb-3">
            <label for="recipient-name" class="col-form-label">Tipo</label>
            <select name="select" type="text" class="form-control" id="recipient-name" v-model.trim="form.type">
              <option value="Dolares">USD</option>
              <option value="Bolivares" selected>BS</option>
            </select>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="submit" class="btn btn-success" >Registrar</button>
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
				price: '',
				type: ''
			}
		}
	},
	methods: {
		onSubmit (e) {
			e.preventDefault()

			const path = 'http://127.0.0.1:8000/CodesBank/'
			axios.post(path, this.form).then((response) => {
				this.form.name = response.data.name
				this.form.price = response.data.price
				this.form.type = response.data.type
				swal('Libro actualizado exitosamente', '', 'success')
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
