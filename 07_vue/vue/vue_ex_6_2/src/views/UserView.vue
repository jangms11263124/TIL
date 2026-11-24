<template>
  <div>
    <h1>User Profile</h1>
    <p>username: {{ route.params.username }}</p>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'

const route = useRoute()
</script>

<style scoped>

</style>