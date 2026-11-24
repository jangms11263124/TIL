<template>
  <li v-for = "product in products" :key="product.id">
    {{ product.name }} - {{ product.price }}원
  </li>
</template>

<script setup>
  defineProps({
    products: Array
  })
</script>

<style scoped>

</style>