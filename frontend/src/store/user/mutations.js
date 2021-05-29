import { LOGIN } from './types'

export default {
  [LOGIN]: function (state, data) {
    state.username = data.username
    state.id = data.id
    this.$router.push('/')
  }
}
