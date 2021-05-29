import { LOGIN } from './types'

export default {
  [LOGIN]: function (state, data) {
    console.log('Logeando')
    state.username = data.username
  }
}
