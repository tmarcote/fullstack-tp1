<template>
  <div id="q-productos">
    <div class="q-pa-md">
      <q-table
        title="Productos"
        :data="productos"
        :columns="columns"
        row-key="id"
      >
        <template v-slot:top>
          <q-btn color="primary" label="Agregar Usuario" @click="agregarProducto"></q-btn>
          <q-dialog v-model="modal_producto">
            <q-card>
              <q-card-section>
                <div class="text-h6">Agregar producto</div>
              </q-card-section>

              <q-card-section>
                <div class="row">
                  <q-input v-model="editedItem.nombre" label="Nombre" class="q-mr-sm"></q-input>
                  <q-input v-model="editedItem.descripcion" label="Descripcion" class="q-mr-sm"></q-input>
                  <q-input v-model="editedItem.precio" label="Precio" type="number" class="q-mr-sm"></q-input>
                  <q-input v-model="editedItem.stock" label="Stock" type="number" class="q-mr-sm"></q-input>
                </div>
              </q-card-section>
              <q-card-actions align="right">
                <q-btn flat label="OK" color="primary" v-close-popup @click="submitProducto" ></q-btn>
              </q-card-actions>
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
            @click="eliminaProducto(props.row.id)"
            />
          </q-td>
        </template>
      </q-table>
    </div>
  </div>
</template>

<script>
import { GET_PRODUCTOS, ADD_PRODUCTO, DELETE_PRODUCTO, EDIT_PRODUCTO } from '../store/products/types'

export default {
  name: 'PageProductos',
  data: function () {
    return {
      modal_producto: false,
      editedItem: {
        id: -1,
        nombre: '',
        descripcion: '',
        precio: 0.0,
        stock: 0
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
        { name: 'descripcion', align: 'center', label: 'Descripcion', field: 'descripcion', sortable: false },
        { name: 'precio', align: 'center', label: 'Precio', field: 'precio', sortable: false },
        { name: 'stock', align: 'center', label: 'Stock', field: 'stock', sortable: false },
        { name: 'acciones', label: 'Acciones', field: 'acciones' }
      ]
    }
  },
  computed: {
    productos: function () {
      return this.$store.getters[GET_PRODUCTOS]
    }
  },
  methods: {
    agregarProducto: function () {
      this.editedItem = {
        id: -1,
        nombre: '',
        descripcion: '',
        precio: 0.0,
        stock: 0
      }
      this.modal_producto = true
    },
    editarProducto: function (item) {
      this.editedItem = Object.assign({}, item)
      this.modal_usuario = true
    },
    submitProducto: function () {
      if (this.editedItem.id === -1) {
        this.$store.dispatch(ADD_PRODUCTO, this.editedItem)
      } else {
        this.$store.dispatch(EDIT_PRODUCTO, this.editedItem)
      }
    },
    eliminarProducto: function (id) {
      this.$store.dispatch(DELETE_PRODUCTO, id)
    }
  },
  mounted: function () {
    this.$store.dispatch(GET_PRODUCTOS)
    // this.$store.dispatch('testVenta')
  }
}
</script>
