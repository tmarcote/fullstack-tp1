import { GET_USER_ID } from './types'

export default {
  [GET_USER_ID]: function (state) {
    return state.id
  }
}
