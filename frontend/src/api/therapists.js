import { HTTP } from './common'

export const Therapist = {
  list () {
    return HTTP.get('/psychotherapists/').then(response => {
      return response.data
    })
  },
  details (id) {
    return HTTP.get(`/psychotherapists/${id}`).then(response => {
      return response.data
    })
  }
}
