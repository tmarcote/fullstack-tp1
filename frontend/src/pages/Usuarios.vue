<template>
  <div id="q-usuarios">
    <div class="q-pa-md">
      <q-table
        title="Usuarios"
        :data="usuarios"
        :columns="columns"
        row-key="id"
      >
        <template v-slot:top>
          <q-btn color="primary" label="Agregar Usuario" @click="agregarUsuario"></q-btn>
          <q-dialog v-model="modal_usuario">
            <q-card>
              <q-card-section>
                <div class="text-h6">Agregar usuario</div>
              </q-card-section>

              <q-card-section>
                <div class="row">
                  <q-input v-model="editedItem.username" label="Username" class="q-mr-sm"></q-input>
                  <q-input type="password" v-model="editedItem.password" label="Password" class="q-mr-sm"></q-input>
                  <q-input v-model="editedItem.nombre" label="Nombre" class="q-mr-sm"></q-input>
                  <q-input v-model="editedItem.apellido" label="apellido" class="q-mr-sm"></q-input>
                </div>
              </q-card-section>
              <q-card-actions align="right">
                <q-btn flat label="OK" color="primary" v-close-popup @click="submitUsuario" ></q-btn>
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
            @click="editarUsuario(props.row)"
            />
            <q-btn
            color="negative"
            icon-right="delete"
            no-caps
            flat
            dense
            @click="eliminarUsuario(props.row.id)"
            />
          </q-td>
        </template>
      </q-table>
    </div>
  </div>
</template>

<script>
import { GET_USUARIOS, ADD_USUARIO, DELETE_USUARIO, EDIT_USUARIO } from '../store/user/types'

export default {
  name: 'PageUsuarios',
  data: function () {
    return {
      modal_usuario: false,
      editedItem: {
        id: -1,
        username: '',
        password: '',
        nombre: '',
        apellido: ''
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
        { name: 'username', align: 'center', label: 'Username', field: 'username', sortable: false },
        { name: 'nombre', align: 'center', label: 'Nombre', field: 'nombre', sortable: false },
        { name: 'apellido', align: 'center', label: 'Apellido', field: 'apellido', sortable: false },
        { name: 'acciones', label: 'Acciones', field: 'acciones' }
      ]
    }
  },
  computed: {
    usuarios: function () {
      return this.$store.getters[GET_USUARIOS]
    }
  },
  methods: {
    agregarUsuario: function () {
      this.editedItem = {
        id: -1,
        username: '',
        password: '',
        nombre: '',
        apellido: ''
      }
      this.modal_usuario = true
    },
    editarUsuario: function (item) {
      this.editedItem = Object.assign({}, item)
      this.modal_usuario = true
    },
    submitUsuario: function () {
      if (this.editedItem.id === -1) {
        this.$store.dispatch(ADD_USUARIO, this.editedItem)
      } else {
        this.$store.dispatch(EDIT_USUARIO, this.editedItem)
      }
    },
    eliminarUsuario: function (id) {
      this.$store.dispatch(DELETE_USUARIO, id)
    }
  },
  mounted: function () {
    this.$store.dispatch(GET_USUARIOS)
  }
}
</script>
