import { LOGIN, GET_USUARIOS, ADD_USUARIO, DELETE_USUARIO, EDIT_USUARIO } from './types'
import { api } from '../../boot/axios'

export default {
  [LOGIN]: function ({ commit }, data) {
    const formData = new FormData()
    formData.append('username', data.username)
    formData.append('password', data.password)

    return api.post('/usuarios/login', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    })
      .then(response => {
        if (response.status === 200) {
          commit(LOGIN, response.data)
        } else {
          alert('Credenciales incorrectas.')
        }
      })
      .catch(err => {
        console.log(err)
        alert('Credenciales incorrectas.')
      })
  },
  [GET_USUARIOS]: function ({ commit }) {
    return api.get('/usuarios')
      .then(response => {
        if (response.status === 200) {
          commit(GET_USUARIOS, response.data)
        }
      })
      .catch(err => {
        console.log(err)
      })
  },
  [ADD_USUARIO]: function ({ commit }, data) {
    const formData = new FormData()
    formData.append('username', data.username)
    formData.append('password', data.password)
    formData.append('nombre', data.nombre)
    formData.append('apellido', data.apellido)
    formData.append('rol', data.rol)

    return api.post('/usuarios', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    })
      .then(response => {
        if (response.status === 200) {
          commit(ADD_USUARIO, response.data)
        }
      })
      .catch(err => {
        console.log(err)
        alert('Error al agregar usuario.')
      })
  },
  [DELETE_USUARIO]: function ({ commit }, id) {
    return api.delete(`/usuarios/${id}`)
      .then(response => {
        if (response.status === 200) {
          commit(DELETE_USUARIO, id)
        }
      })
      .catch(err => {
        console.log(err)
        alert('Error al eliminar usuario.')
      })
  },
  [EDIT_USUARIO]: function ({ commit }, data) {
    const formData = new FormData()
    formData.append('username', data.username)
    formData.append('password', data.password)
    formData.append('nombre', data.nombre)
    formData.append('apellido', data.apellido)
    formData.append('rol', data.rol)

    return api.patch(`/usuarios/${data.id}`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    })
      .then(response => {
        if (response.status === 200) {
          commit(EDIT_USUARIO, response.data)
        }
      })
      .catch(err => {
        console.log(err)
        alert('Error al editar usuario.')
      })
  }
}
