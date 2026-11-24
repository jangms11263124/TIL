<template>
  <li>
    <RouterLink :to="{ name: 'post-detail', params: { username: username, id: post.id } }">
      제목: {{ post.title }}
    </RouterLink>
  </li>
</template>

<script setup>
import { RouterLink } from 'vue-router'

defineProps({
  post: Object,
  username: String
})
</script>
  
<style scoped>

</style>