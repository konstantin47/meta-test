import Vue from 'vue'
import Vuex from 'vuex'
import { Therapist } from '../api/therapists'
import { SET_THERAPISTS, SET_THERAPIST } from './mutation-types.js'

Vue.use(Vuex)

const state = {
  therapists: [],
  therapist: {}
}

const getters = {
  therapists: state => state.therapists,
  therapist: state => state.therapist
}

const mutations = {
  [SET_THERAPISTS] (state, { therapists }) {
    state.therapists = therapists
  },
  [SET_THERAPIST] (state, { therapist }) {
    state.therapist = therapist
  }
}

const actions = {
  getTherapists ({ commit }) {
    Therapist.list().then(therapists => {
      commit(SET_THERAPISTS, { therapists })
    })
  },
  getDetails ({ commit }, payload) {
    Therapist.details(payload.id).then(therapist => {
      commit(SET_THERAPIST, { therapist })
    })
  }
}

export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations
})
