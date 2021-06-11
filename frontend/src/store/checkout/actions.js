import { GET_CATALOG } from './types'
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
  }
}
