<template>
  <date-picker v-model="date" type="date" :min="min" :max="max"/>
</template>
<script>
import DatePicker from '@hyjiacan/vue-datepicker'
import '@hyjiacan/vue-datepicker/dist/datepicker.css'

export default {
  components: {DatePicker},
  data() {
    return {
      date: new Date(),
      min: '2012-12-12',
      max: '2020-12-12'
    }
  }
}
</script>
