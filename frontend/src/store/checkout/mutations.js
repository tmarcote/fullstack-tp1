import { PURCHASE, ADD_CART, GET_CATALOG } from './types'

export default {
  [GET_CATALOG]: function (state, data) {
    state.productos = data
  },
  [PURCHASE]: function (state, data) {
    state.cart = []
    this.$router.push('/ventaok')
  },
  [ADD_CART]: function (state, data) {
    const index = state.cart.findIndex(el => el.id === data.id)

    if (index === -1) {
      data.cantidad = 1
      state.cart.push(data)
    } else {
      state.cart[index].cantidad += 1
    }

    const indexCatalog = state.productos.findIndex(el => el.id === data.id)
    state.productos[indexCatalog].stock -= 1

    state.total += data.precio
  }
}
