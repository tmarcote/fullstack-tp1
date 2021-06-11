import { ADD_CART, GET_CATALOG, REMOVE_CART, EDIT_CART, EMPTY_CART } from './types'

const calcularTotal = (cart) => {
  let total = 0
  for (const prod of cart) {
    total += (prod.precio * parseInt(prod.cantidad))
  }
  return total
}

export default {
  [GET_CATALOG]: function (state, data) {
    state.productos = data
  },
  [ADD_CART]: function (state, data) {
    const index = state.cart.findIndex(el => el.id === data.id)

    if (index === -1) {
      state.cart.push(data)
    } else {
      state.cart[index].cantidad += parseInt(data.cantidad)
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
      state.cart[index].cantidad = parseInt(state.cart[index].cantidad)
    }

    state.total = calcularTotal(state.cart)
  },
  [EMPTY_CART]: function (state) {
    state.cart = []
    state.total = 0
  }
}
