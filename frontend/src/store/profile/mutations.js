import { LOGIN } from './types'

export default {
  [LOGIN]: function (state, data) {
    state.username = data.username
    state.id = data.id
    state.rol = data.rol

    if (state.rol === 'admin') {
      this.$router.push('/admin')
    } else {
      this.$router.push('/')
    }
  }
}
