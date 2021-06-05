import { GET_USUARIOS, ADD_USUARIO, DELETE_USUARIO, EDIT_USUARIO } from './types'
import { api } from '../../boot/axios'

export default {
  [GET_USUARIOS]: async function ({ commit }) {
    try {
      const response = await api.get('/usuarios')
      if (response.status === 200) {
        commit(GET_USUARIOS, response.data)
      }
    } catch (err) {
      console.log(err)
    }
  },
  [ADD_USUARIO]: async function ({ commit }, data) {
    const formData = new FormData()
    formData.append('username', data.username)
    formData.append('password', data.password)
    formData.append('nombre', data.nombre)
    formData.append('apellido', data.apellido)
    formData.append('rol', data.rol)

    try {
      const response = await api.post('/usuarios', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
      if (response.status === 200) {
        commit(ADD_USUARIO, response.data)
      }
    } catch (err) {
      console.log(err)
      alert('Error al agregar usuario.')
    }
  },
  [DELETE_USUARIO]: async function ({ commit }, id) {
    try {
      const response = await api.delete(`/usuarios/${id}`)
      if (response.status === 200) {
        commit(DELETE_USUARIO, id)
      }
    } catch (err) {
      console.log(err)
      alert('Error al eliminar usuario.')
    }
  },
  [EDIT_USUARIO]: async function ({ commit }, data) {
    const formData = new FormData()
    formData.append('username', data.username)
    formData.append('password', data.password)
    formData.append('nombre', data.nombre)
    formData.append('apellido', data.apellido)
    formData.append('rol', data.rol)

    try {
      const response = await api.patch(`/usuarios/${data.id}`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
      if (response.status === 200) {
        commit(EDIT_USUARIO, response.data)
      }
    } catch (err) {
      console.log(err)
      alert('Error al editar usuario.')
    }
  }
}
