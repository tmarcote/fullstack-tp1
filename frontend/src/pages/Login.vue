<template>
  <q-page class="flex flex-center">
    <q-input v-model="username" placeholder="username" class="q-mr-sm"/>
    <q-input v-model="password" placeholder="password" type="password" class="q-mr-sm"/>
    <q-btn v-on:click="login">Login</q-btn>
  </q-page>
</template>

<script>
import { LOGIN } from '../store/user/types'

export default {
  name: 'PageLogin',
  data: function () {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    login: function () {
      this.$store.dispatch(LOGIN, {
        username: this.username,
        password: this.password
      })
    }
  }
}
</script>
