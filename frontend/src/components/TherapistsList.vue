<template>
  <ul>
    <li v-for="therapist in therapists" v-bind:key="therapist.id">
      <router-link :to="{ name: 'TherapistDetails', params: { id: therapist.id } }">
        Show details
      </router-link>
    </li>
  </ul>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'therapist-list',
  computed: mapGetters(['therapists']),
  methods: {},
  beforeMount () {
    this.$store.dispatch('getTherapists')
  }
}
</script>
