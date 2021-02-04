<template>
  <div class="container">
    <div class="row">
      <div class="col-4">
        <img :src="therapist['data']['fields']['Фотография'][0]['thumbnails']['large']['url']" class="img-fluid" alt="" />
      </div>
      <div class="col-8 info">
        <h1 class="name">{{therapist['data']['fields']['Имя']}}</h1>
        <h4>Методы:</h4>
          <span class="method" v-for="method in therapist['data']['fields']['Методы']" v-bind:key="method"><span class="badge badge-secondary">{{ method }}</span></span>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'therapist-details',
  computed: mapGetters(['therapist']),
  methods: {},
  beforeMount () {
    this.$store.dispatch('getDetails', { 'id': this.id })
  },
  props: {
    id: String
  }
}
</script>

<style>
  .container {
    margin: 50px;
  }

  .info {
    float: right;
    padding-left: 50px;
  }

  .name {
    text-align: center;
  }

  .method {
    padding-right: 10px;
  }

</style>
