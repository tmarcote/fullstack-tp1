import { GET_CART, GET_TOTAL, GET_CATALOG } from './types'

export default {
  [GET_CATALOG]: function (state) {
    return state.productos
  },
  [GET_CART]: function (state) {
    return state.cart
  },
  [GET_TOTAL]: function (state) {
    return state.total
  }
}
