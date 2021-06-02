import { GET_REPORTE_VENTAS } from './types'
import { api } from '../../boot/axios'

export default {
  [GET_REPORTE_VENTAS]: function ({ commit }) {
    return api.get('/productos/ventas')
      .then(response => {
        if (response.status === 200) {
          commit(GET_REPORTE_VENTAS, response.data)
        }
      })
      .catch(err => {
        console.log(err)
      })
  }
}
