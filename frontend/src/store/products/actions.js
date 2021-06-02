import { GET_PRODUCTOS, ADD_PRODUCTO, DELETE_PRODUCTO, EDIT_PRODUCTO } from './types'
import { api } from '../../boot/axios'

export default {
  [GET_PRODUCTOS]: function ({ commit }) {
    return api.get('/productos')
      .then(response => {
        if (response.status === 200) {
          commit(GET_PRODUCTOS, response.data)
        }
      })
      .catch(err => {
        console.log(err)
      })
  },
  [ADD_PRODUCTO]: function ({ commit }, data) {
    const formData = new FormData()
    formData.append('nombre', data.nombre)
    formData.append('descripcion', data.descripcion)
    formData.append('precio', data.precio)
    formData.append('stock', data.stock)

    return api.post('/productos', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    })
      .then(response => {
        if (response.status === 200) {
          commit(ADD_PRODUCTO, response.data)
        }
      })
      .catch(err => {
        console.log(err)
        alert('Error al agregar producto.')
      })
  },
  [DELETE_PRODUCTO]: function ({ commit }, id) {
    return api.delete(`/productos/${id}`)
      .then(response => {
        if (response.status === 200) {
          commit(DELETE_PRODUCTO, id)
        }
      })
      .catch(err => {
        console.log(err)
        alert('Error al eliminar producto.')
      })
  },
  [EDIT_PRODUCTO]: function ({ commit }, data) {
    const formData = new FormData()
    formData.append('nombre', data.nombre)
    formData.append('descripcion', data.descripcion)
    formData.append('precio', data.precio)
    formData.append('stock', data.stock)

    return api.patch(`/productos/${data.id}`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    })
      .then(response => {
        if (response.status === 200) {
          commit(EDIT_PRODUCTO, response.data)
        }
      })
      .catch(err => {
        console.log(err)
        alert('Error al editar producto.')
      })
  },
  testVenta: function ({ commit }) {
    let data = [
      {
        id: 1,
        cantidad: 3
      },
      {
        id: 2,
        cantidad: 1
      }
    ]

    data = JSON.stringify(data)

    return api.post('/productos/venta', data, {
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then(response => {
        console.log(response)
      })
      .catch(err => {
        console.log(err)
      })
  }
}
