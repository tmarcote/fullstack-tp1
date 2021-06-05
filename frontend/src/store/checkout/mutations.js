import { PURCHASE, ADD_CART, GET_CATALOG, REMOVE_CART, EDIT_CART } from './types'

const calcularTotal = (cart) => {
  let total = 0
  for (const prod of cart) {
    total += (prod.precio * prod.cantidad)
  }
  return total
}

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

    state.total = calcularTotal(state.cart)
  },
  [REMOVE_CART]: function (state, id) {
    console.log(id)
    const index = state.cart.findIndex(el => el.id === id)
    console.log(index)
    if (index > -1) {
      state.cart.splice(index, 1)
    }

    state.total = calcularTotal(state.cart)
  },
  [EDIT_CART]: function (state, data) {
    const index = state.cart.findIndex(el => el.id === data.id)

    if (index > -1) {
      Object.assign(state.cart[index], data)
    }

    state.total = calcularTotal(state.cart)
  }
}
