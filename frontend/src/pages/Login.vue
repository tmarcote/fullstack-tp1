<template>
  <q-page class="flex flex-center">
    <form @submit.prevent.stop="login">
      <q-input ref="username" v-model="username" placeholder="username" class="q-mr-sm" lazy-rule :rules="[val => !!val || 'Field is required']"/>
      <q-input ref="password" v-model="password" placeholder="password" type="password" class="q-mr-sm" lazy-rule :rules="[val => !!val || 'Field is required']"/>
      <q-btn type="submit">Login</q-btn>
    </form>
  </q-page>
</template>

<script>
import { LOGIN } from '../store/profile/types'

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
      this.$refs.username.validate()
      this.$refs.password.validate()

      if (this.$refs.username.hasError || this.$refs.password.hasError) {
        return
      }

      this.$store.dispatch(LOGIN, {
        username: this.username,
        password: this.password
      })
    }
  }
}
</script>
