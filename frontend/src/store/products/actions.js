import { LOAD_PRODUCTS } from './types'

export default {
  [LOAD_PRODUCTS] ({ commit }) {
    fetch('https://api.mockaroo.com/api/82662230?count=1000&key=4585d760')
      .then((response) => {
        if (response.ok) {
          return response.json()
        }
      })
      .then((result) => {
        commit('agregarProductos', result)
      })
  }
}
