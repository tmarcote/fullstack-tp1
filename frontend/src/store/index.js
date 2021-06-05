import Vuex from 'vuex'
import Vue from 'vue'

import users from './users'
import products from './products'
import reportes from './reportes'
import profile from './profile'
import checkout from './checkout'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    users,
    products,
    reportes,
    profile,
    checkout
  }
})
