import { PURCHASE } from './types'
import { api } from '../../boot/axios'

export default {
  [PURCHASE]: async function ({ commit, state }) {
    const data = JSON.stringify(state.cart)

    try {
      const response = await api.post('/productos/venta', data, {
        headers: {
          'Content-Type': 'application/json'
        }
      })
      console.log(response)
    } catch (err) {
      console.log(err)
    }
  }
}
