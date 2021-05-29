import Vuex from 'vuex'
import Vue from 'vue'

import moduloUser from './user'
import moduloCheckout from './checkout'
import products from './products'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    user: moduloUser,
    checkout: moduloCheckout,
    products
  }
})
