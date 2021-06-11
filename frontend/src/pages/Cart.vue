<template>
  <div id="q-cart">
    <div class="q-pa-md">
      <q-table
        title="Cart"
        :data="cart"
        :columns="columns"
        row-key="id"
      >
        <template v-slot:top>
          <div class="text-h6 q-mr-md">Total: $ {{total}}</div>
          <q-btn color="primary" label="Comprar" @click="comprar"></q-btn>
          <q-dialog ref="modalProducto" v-model="modal_producto">
            <q-card>
              <q-card-section>
                <div class="text-h6">Editar producto</div>
              </q-card-section>
              <form @submit.prevent.stop="submitProducto">
                <q-card-section>
                  <div class="row">
                    <q-input ref="cantidad" min=1 v-model="editedItem.cantidad" label="Cantidad" type="number" class="q-mr-sm" lazy-rule :rules="[val => !!val || 'Field is required']"></q-input>
                  </div>
                </q-card-section>
                <q-card-actions align="right">
                  <q-btn flat label="OK" color="primary" type="submit"></q-btn>
                </q-card-actions>
              </form>
            </q-card>
          </q-dialog>
        </template>

        <template v-slot:body-cell-acciones="props">
          <q-td :props="props">
            <q-btn
            color="secondary"
            icon-right="edit"
            no-caps
            flat
            dense
            @click="editarProducto(props.row)"
            />
            <q-btn
            color="negative"
            icon-right="delete"
            no-caps
            flat
            dense
            @click="eliminarProducto(props.row.id)"
            />
          </q-td>
        </template>
      </q-table>
    </div>
  </div>
</template>

<script>
import { GET_CART, GET_TOTAL, REMOVE_CART, EDIT_CART, CHECKOUT } from '../store/checkout/types'

export default {
  name: 'PageCart',
  data: function () {
    return {
      modal_producto: false,
      editedItem: {
        id: -1,
        nombre: '',
        precio: 0.0,
        cantidad: 0
      },
      columns: [
        {
          name: 'id',
          required: true,
          label: 'ID',
          align: 'left',
          field: row => row.id,
          format: val => `${val}`,
          sortable: false
        },
        { name: 'nombre', align: 'center', label: 'Nombre', field: 'nombre', sortable: false },
        { name: 'precio', align: 'center', label: 'Precio', field: 'precio', sortable: false },
        { name: 'cantidad', align: 'center', label: 'Cantidad', field: 'cantidad', sortable: false },
        { name: 'acciones', label: 'Acciones', field: 'acciones' }
      ]
    }
  },
  computed: {
    cart: function () {
      return this.$store.getters[GET_CART]
    },
    total: function () {
      return this.$store.getters[GET_TOTAL]
    }
  },
  methods: {
    editarProducto: function (item) {
      this.editedItem = Object.assign({}, item)
      this.modal_producto = true
    },
    submitProducto: function () {
      this.$refs.cantidad.validate()

      if (this.$refs.cantidad.hasError) {
        return
      }

      this.$refs.modalProducto.hide()
      this.$store.commit(EDIT_CART, this.editedItem)
    },
    eliminarProducto: function (id) {
      this.$store.commit(REMOVE_CART, id)
    },
    comprar: function () {
      if (this.cart.length === 0) {
        alert('No tiene ningún producto en el carro de compras.')
        return
      }
      this.$store.dispatch(CHECKOUT)
    }
  }
}
</script>
