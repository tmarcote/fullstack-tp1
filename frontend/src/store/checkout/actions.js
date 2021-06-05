import { PURCHASE, GET_CATALOG, EMPTY_CART } from './types'
import { api } from '../../boot/axios'

export default {
  [GET_CATALOG]: async function ({ commit }) {
    try {
      const response = await api.get('/productos')
      if (response.status === 200) {
        commit(GET_CATALOG, response.data)
      }
    } catch (err) {
      console.log(err)
    }
  },
  [PURCHASE]: async function ({ commit, state }) {
    const data = JSON.stringify(state.cart)

    try {
      const response = await api.post('/productos/venta', data, {
        headers: {
          'Content-Type': 'application/json'
        }
      })

      if (response.status === 200) {
        commit(EMPTY_CART)
        this.$router.push('/success')
      }
    } catch (err) {
      console.log(err)
      alert('Se produjo un error al procesar la compra.')
    }
  }
}
