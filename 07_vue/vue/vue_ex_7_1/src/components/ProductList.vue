<template>
  <div>
    <h2>Product List</h2>
    <ul>
      <li v-for="product in store.products" :key="product.id">
        {{ product.id }} - {{ product.title }} - {{ product.body }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { useProductStore } from '@/stores/product'

const store = useProductStore()
</script>

<style scoped>

</style>