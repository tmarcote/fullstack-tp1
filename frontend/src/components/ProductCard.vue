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

    <q-card-actions>
      <div class= "row mis-actions">
        <div class="col-8 text-h5 q-mt-sm q-mb-xs">$ {{ precio }}</div>
        <div class="col-4 text-h5 q-mt-sm q-mb-xs text-right">
          <q-btn v-if="stock>0" flat color="primary" icon="add_shopping_cart"></q-btn>
          <q-btn v-if="stock<=0"  disabled flat color="primary" icon="add_shopping_cart"></q-btn>

        </div>
      </div>
    </q-card-actions>
  </q-card>
</template>

<script>
export default {
  name: 'ProductCard',
  props: {
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
