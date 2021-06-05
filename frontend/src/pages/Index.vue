<template>
  <q-page>
    <h3 class="text-center">Mi Tienda</h3>
    <div class="q-pa-md row items-start q-gutter-md">
      <ProductCard
        v-for="producto in productos"
        :key="producto.id"
        v-bind="producto"
      />
    </div>
  </q-page>
</template>

<script>
import { GET_PRODUCTOS } from '../store/products/types'
import ProductCard from '../components/ProductCard.vue'

export default {
  name: 'PageIndex',
  components: { ProductCard },
  data: function () {
    return {}
  },
  computed: {
    productos: function () {
      return this.$store.getters[GET_PRODUCTOS]
    }
  },
  methods: {
  },
  mounted: function () {
    this.$store.dispatch(GET_PRODUCTOS)
  }
}
</script>
