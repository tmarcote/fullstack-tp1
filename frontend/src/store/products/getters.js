import { GET_PRODUCTOS } from './types'

export default {
  [GET_PRODUCTOS]: function (state) {
    return state.productos
  }
}
