<template>
  <ProductListItem 
  v-for="product in products" 
  :key="product.id"
  :product="product"
  />
</template>

<script setup>
import ProductListItem from '@/components/ProductListItem.vue';

defineProps({
  products: Array
})
</script>

<style scoped>

</style>