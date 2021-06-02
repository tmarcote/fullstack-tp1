import { GET_REPORTE_VENTAS } from './types'

export default {
  [GET_REPORTE_VENTAS]: function (state, data) {
    state.productos_ventas = data
  }
}
