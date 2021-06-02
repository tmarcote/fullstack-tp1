<template>
  <div id="q-ventas">
    <div class="q-pa-md">
      <q-table
        title="Reporte Ventas"
        :data="productos"
        :columns="columns"
        row-key="id"
      >
      </q-table>
    </div>
  </div>
</template>

<script>
import { GET_REPORTE_VENTAS } from '../store/reportes/types'

export default {
  name: 'PageReporteVentas',
  data: function () {
    return {
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
        { name: 'ventas', align: 'center', label: 'Ventas', field: 'ventas', sortable: false }
      ]
    }
  },
  computed: {
    productos: function () {
      return this.$store.getters[GET_REPORTE_VENTAS]
    }
  },
  mounted: function () {
    this.$store.dispatch(GET_REPORTE_VENTAS)
  }
}
</script>
