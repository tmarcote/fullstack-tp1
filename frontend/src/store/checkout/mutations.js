import { PURCHASE } from './types'

export default {
  [PURCHASE]: function (state, data) {
    state.cart = []
    this.$router.push('/ventaok')
  }
}
