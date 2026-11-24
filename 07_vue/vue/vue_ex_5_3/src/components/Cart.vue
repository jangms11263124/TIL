<template>
  <div>
    <h2>장바구니</h2>
    <ul>
      <li v-for="(item, index) in cartItems" :key="index">
        {{ item.name }} - {{ item.price }}원
        <button @click="removeFromCart(index)">삭제</button>
      </li>
    </ul>
    <p>총 가격: {{ totalPrice }}원</p>
  </div>
</template>

<script setup>
defineProps({
  cartItems: Array,
  totalPrice: Number
})

const emit = defineEmits(['removeFromCart'])

const removeFromCart = (index) => {
  emit('removeFromCart', index)
}
</script>

<style scoped>

</style>