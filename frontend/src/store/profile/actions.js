import { LOGIN } from './types'
import { api } from '../../boot/axios'

export default {
  [LOGIN]: async function ({ commit }, data) {
    const formData = new FormData()
    formData.append('username', data.username)
    formData.append('password', data.password)

    try {
      const response = await api.post('/usuarios/login', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
      if (response.status === 200) {
        commit(LOGIN, response.data)
      } else {
        alert('Credenciales incorrectas.')
      }
    } catch (err) {
      console.log(err)
      alert('Credenciales incorrectas.')
    }
  }
}
