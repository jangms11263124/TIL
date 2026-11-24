
<template>
  <header>
    <nav>
      <RouterLink :to="{ name: 'home' }">Home</RouterLink>
      <span> | </span>
      <RouterLink :to="{ name: 'about' }">About</RouterLink>
      <span> | </span>
      <RouterLink :to="{ name: 'user', params: { username: currentUsername } }">User</RouterLink>
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { ref } from 'vue'
import { RouterLink, RouterView } from 'vue-router'

const currentUsername = ref('admin')
</script>

<style scoped>
</style>
