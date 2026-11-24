<template>
  <li>
    {{ product.name }} - {{ product.price }}원
    <button @click="addToCart(product)">장바구니에 추가</button>
  </li>
</template>

<script setup>
const props = defineProps({
  product: Object
})

const emit = defineEmits(['addToCart'])

const addToCart = () => {
  emit('addToCart', props.product)
}
</script>

<style scoped>

</style>
