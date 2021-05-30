import { GET_PRODUCTOS, ADD_PRODUCTO, DELETE_PRODUCTO, EDIT_PRODUCTO } from './types'

export default {
  [GET_PRODUCTOS]: function (state, data) {
    state.productos = data
  },
  [ADD_PRODUCTO]: function (state, data) {
    state.productos.push(data)
  },
  [DELETE_PRODUCTO]: function (state, id) {
    state.productos = state.productos.filter(obj => obj.id !== id)
  },
  [EDIT_PRODUCTO]: function (state, data) {
    const index = state.productos.findIndex(obj => obj.id === data.id)
    if (index !== -1) {
      Object.assign(state.productos[index], data)
    }
  }
}
