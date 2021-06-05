<template>
  <q-page>
    <h3 class="text-center">Mi Tienda</h3>
    <div class="q-pa-md row items-start q-gutter-md">
      <ProductCard
        v-for="producto in productos"
        :key="producto.id"
        v-bind="producto"
        @productAdded="addedAlert = true"
      />
    </div>

    <q-dialog v-model="addedAlert">
      <q-card>
        <q-card-section>
          <div class="text-h6">Producto agregado al carrito</div>
        </q-card-section>
        <q-card-actions align="right">
          <q-btn flat label="OK" color="primary" v-close-popup></q-btn>
        </q-card-actions>
      </q-card>
    </q-dialog>
  </q-page>
</template>

<script>
import { GET_CATALOG } from '../store/checkout/types'
import ProductCard from '../components/ProductCard.vue'

export default {
  name: 'PageIndex',
  components: { ProductCard },
  data: function () {
    return {
      addedAlert: false
    }
  },
  computed: {
    productos: function () {
      return this.$store.getters[GET_CATALOG]
    }
  },
  mounted: function () {
    this.$store.dispatch(GET_CATALOG)
  }
}
</script>
