<template>
  <div>
    <h1>쇼핑 애플리케이션</h1>
    <ProductList :products="products" @add-to-cart="addToCart" />

    <Cart 
      :cart-items="cartItems"
      :total-price="totalPrice"
      @remove-from-cart="removeFromCart"
    />
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import ProductList from '@/components/ProductList.vue'
import Cart from '@/components/Cart.vue'

let id = 0

const products = ref([
  { id: id++, name: '사과', price: 1000 },
  { id: id++, name: '바나나', price: 1500 },
  { id: id++, name: '딸기', price: 2000 },
  { id: id++, name: '포도', price: 3000 },
  { id: id++, name: '복숭아', price: 2000 },
  { id: id++, name: '수박', price: 5000 }
])

// 장바구니 제품 목록 데이터
const cartItems = ref([])

// 장바구니 제품 목록에 변화가 있을때만 재연산되는 총 가격 변수
const totalPrice = computed(() => {
  return cartItems.value.reduce((sum, item) => sum + item.price, 0)
})

// 장바구니 제품 추가 기능
const addToCart = (product) => {
  cartItems.value.push(product)
}

// 장바구니 제품 삭제 기능
const removeFromCart = (index) => {
  cartItems.value.splice(index, 1)
}
</script>
