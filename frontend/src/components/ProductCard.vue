<template>
  <q-card class="my-card">
    <q-card-section horizontal>
      <q-img
        class="col-6"
        :src= "img_url || 'na.png'"
      ></q-img>

      <q-card-section>
        <div class="text-h5 q-mb-xs">{{ nombre }}</div>
        <div class="text-caption ">
          {{ descripcion }}
        </div>
      </q-card-section>
    </q-card-section>

    <q-separator></q-separator>

    <q-card-section horizontal>
      <div class= "row mis-actions q-pa-sm">
        <div class="col-6 q-mt-sm q-mb-xs">
          <div class="text-h5">$ {{ precio }}</div>
        </div>
        <div class="col-6 q-mt-sm q-mb-xs text-right text-grey">
          <div class="text-h6">Stock: {{ stock }}</div>
        </div>
      </div>
    </q-card-section>

    <q-separator></q-separator>
    <q-card-actions>
      <form class= "row mis-actions" @submit.prevent.stop="addToCart(id)">
        <div class="col-8 q-mt-sm q-mb-xs">
            <q-input ref="cantidad" min=1 :max=stock v-model="cantidad" label="Cantidad" type="number" class="q-mr-sm" lazy-rule :rules="[val => !!val || 'Field is required']"></q-input>
        </div>
        <div class="col-4 text-h5 q-mt-sm q-mb-xs text-right">
          <q-btn v-if="stock>0" flat color="primary" icon="add_shopping_cart" type="submit"></q-btn>
          <q-btn v-if="stock<=0"  disabled flat color="primary" icon="add_shopping_cart"></q-btn>
        </div>
      </form>
    </q-card-actions>
  </q-card>
</template>

<script>
import { ADD_CART } from '../store/checkout/types'

export default {
  name: 'ProductCard',
  props: {
    id: {
      type: Number,
      required: true
    },
    nombre: {
      type: String,
      required: true
    },
    descripcion: {
      type: String,
      required: false
    },
    precio: {
      type: Number,
      required: true
    },
    stock: {
      type: Number,
      required: true
    },
    img_url: {
      type: String,
      required: false
    }
  },
  data: function () {
    return {
      cantidad: 1
    }
  },
  methods: {
    addToCart: function (id) {
      const product = {
        id: this._props.id,
        nombre: this._props.nombre,
        precio: this._props.precio,
        cantidad: parseInt(this.cantidad)
      }

      this.$store.commit(ADD_CART, product)

      this.$emit('productAdded')
    }
  }
}
</script>

<style>
.my-card {
  width: 100%;
  max-width: 250px;
  overflow: auto;
  word-break: break-all;
}
.mis-actions {
  flex: 1;
}
</style>
