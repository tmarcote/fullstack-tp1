import { GET_USUARIOS, LOGIN, ADD_USUARIO, DELETE_USUARIO, EDIT_USUARIO } from './types'

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
  },
  [GET_USUARIOS]: function (state, data) {
    state.usuarios = data
  },
  [ADD_USUARIO]: function (state, data) {
    state.usuarios.push(data)
  },
  [DELETE_USUARIO]: function (state, id) {
    state.usuarios = state.usuarios.filter(obj => obj.id !== id)
  },
  [EDIT_USUARIO]: function (state, data) {
    const index = state.usuarios.findIndex(obj => obj.id === data.id)
    if (index !== -1) {
      Object.assign(state.usuarios[index], data)
    }
  }
}
