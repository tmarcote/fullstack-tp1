import { GET_REPORTE_VENTAS } from './types'

export default {
  [GET_REPORTE_VENTAS]: function (state) {
    return state.productos_ventas
  }
}
