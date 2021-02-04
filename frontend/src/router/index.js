import Vue from 'vue'
import Router from 'vue-router'
import TherapistsList from '@/components/TherapistsList'
import TherapistDetails from '@/components/TherapistDetails'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/therapists',
      name: 'TherapistsList',
      component: TherapistsList
    },
    {
      path: '/therapists/:id',
      name: 'TherapistDetails',
      props: true,
      component: TherapistDetails
    }
  ]
})
