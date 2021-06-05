import { GET_CART, GET_TOTAL } from './types'

export default {
  [GET_CART]: function (state) {
    return state.cart
  },
  [GET_TOTAL]: function (state) {
    return state.total
  }
}
