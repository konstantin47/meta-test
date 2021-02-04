<template>
  <router-view/>
  <!-- <ul>
    <li v-for="therapist in therapists" v-bind:key="therapist.id">
      <router-link :to="{ name: 'TherapistDetails', params: { id: therapist.id } }">
        Show details
      </router-link>
    </li>
  </ul> -->
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'app',
  computed: mapGetters(['therapists']),
  beforeMount () {
    this.$store.dispatch('getTherapists')
  }
}
</script>

<style>
  body {
    font-family: "Work Sans", "Segoe UI", "Helvetica Neue", sans-serif;
  }
  h1, h2, h3, h4, h5, h6 {
    font-family: "Eczar", sans-serif;
  }
</style>
