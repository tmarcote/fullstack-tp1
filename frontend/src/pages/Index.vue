<template>
  <q-page class="flex flex-center">
    <h3>{{ elusuario }}</h3>
    <q-input v-model="usuario" />
    <q-btn v-on:click="login">Push me</q-btn>
  </q-page>
</template>

<script>
import { LOGIN } from '../store/user/types'

export default {
  name: 'PageIndex',
  data: function () {
    return {
      usuario: ''
    }
  },
  computed: {
    elusuario: function () {
      return this.$store.state.user.username
    }
  },
  methods: {
    login: function () {
      this.$store.commit(LOGIN, {
        username: this.usuario
      })
    }
  }
}
</script>
