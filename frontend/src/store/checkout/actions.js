import { CHECKOUT, GET_CATALOG, EMPTY_CART } from './types'

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
  [CHECKOUT]: async function ({ commit, state }, userId) {
    const data = {
      total: state.total,
      productos: state.cart,
      user_id: userId
    }

    const payload = JSON.stringify(data)
    console.log(payload)
    try {
      const response = await api.post('/checkout', payload, {
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
