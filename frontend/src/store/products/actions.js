import { GET_PRODUCTOS, ADD_PRODUCTO, DELETE_PRODUCTO, EDIT_PRODUCTO } from './types'
import { api } from '../../boot/axios'

export default {
  [GET_PRODUCTOS]: async function ({ commit }) {
    try {
      const response = await api.get('/productos')
      if (response.status === 200) {
        commit(GET_PRODUCTOS, response.data)
      }
    } catch (err) {
      console.log(err)
    }
  },
  [ADD_PRODUCTO]: async function ({ commit }, data) {
    const formData = new FormData()
    formData.append('nombre', data.nombre)
    formData.append('descripcion', data.descripcion)
    formData.append('precio', data.precio)
    formData.append('stock', data.stock)
    formData.append('img_url', data.img_url)

    try {
      const response = await api.post('/productos', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
      if (response.status === 200) {
        commit(ADD_PRODUCTO, response.data)
      }
    } catch (err) {
      console.log(err)
      alert('Error al agregar producto.')
    }
  },
  [DELETE_PRODUCTO]: async function ({ commit }, id) {
    try {
      const response = await api.delete(`/productos/${id}`)
      if (response.status === 200) {
        commit(DELETE_PRODUCTO, id)
      }
    } catch (err) {
      console.log(err)
      alert('Error al eliminar producto.')
    }
  },
  [EDIT_PRODUCTO]: async function ({ commit }, data) {
    const formData = new FormData()
    formData.append('nombre', data.nombre)
    formData.append('descripcion', data.descripcion)
    formData.append('precio', data.precio)
    formData.append('stock', data.stock)
    formData.append('img_url', data.img_url)

    try {
      const response = await api.patch(`/productos/${data.id}`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
      if (response.status === 200) {
        commit(EDIT_PRODUCTO, response.data)
      }
    } catch (err) {
      console.log(err)
      alert('Error al editar producto.')
    }
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
