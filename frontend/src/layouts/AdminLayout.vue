<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="leftDrawerOpen = !leftDrawerOpen"
        />

        <q-toolbar-title>
          Admin Page
        </q-toolbar-title>

        <div class="text-h6 q-pr-md">
          {{ username }}
        </div>
         <q-btn color="negative" label="Logout" @click="logout"></q-btn>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
      content-class="bg-grey-1"
    >
      <q-list>
        <q-item-label
          header
          class="text-grey-8"
        >
          Menu
        </q-item-label>
        <EssentialLink
          v-for="link in essentialLinks"
          :key="link.title"
          v-bind="link"
        />
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import EssentialLink from 'components/EssentialLink.vue'
import { LOGOUT } from '../store/profile/types'
import { EMPTY_CART } from '../store/checkout/types'

const linksData = [
  {
    title: 'Usuarios',
    caption: 'Administrar usuarios',
    icon: 'supervisor_account',
    link: '/#/admin/usuarios'
  },
  {
    title: 'Productos',
    caption: 'Administrar productos',
    icon: 'add_shopping_cart',
    link: '/#/admin/productos'
  },
  {
    title: 'Reporte de Ventas',
    caption: 'Reporte de Ventas',
    icon: 'analytics',
    link: '/#/admin/reportes/ventas'
  }
]

export default {
  name: 'AdminLayout',
  components: { EssentialLink },
  data () {
    return {
      leftDrawerOpen: false,
      essentialLinks: linksData
    }
  },
  computed: {
    username: function () {
      return this.$store.state.profile.username
    }
  },
  methods: {
    logout: function () {
      this.$store.commit(LOGOUT)
      this.$store.commit(EMPTY_CART)
    }
  }
}
</script>
