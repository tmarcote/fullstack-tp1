<template>
  <div class="fullscreen bg-blue text-white text-center q-pa-md flex flex-center">
    <div>
      <div class="text-h1 q-mb-md">
        Compra Exitosa!!!
      </div>

      <div class="text-h4" style="opacity:.8">
        Nos contactaremos a la brevedad para organizar el envío.
      </div>

      <q-btn
        class="q-mt-xl"
        color="white"
        text-color="blue"
        unelevated
        to="/"
        label="Volver a la tienda"
        no-caps
      />
    </div>
  </div>
</template>

<script>
export default {
  name: 'Success'
}
</script>
