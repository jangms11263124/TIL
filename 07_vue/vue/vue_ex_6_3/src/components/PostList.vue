<template>
  <div>
    <h2><strong>{{ username }}</strong>이 작성한 게시글</h2>

    <ol>
      <PostListItem 
        v-for="post in posts" 
        :key="post.id" 
        :post="post"
        :username="username"
      />
    </ol>
    <hr>

    <RouterView />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, RouterView } from 'vue-router'
import PostListItem from './PostListItem.vue'

const route = useRoute()
const username = ref(route.params.username)
const posts = ref([
  { id: 1, title: 'Post 1', content: 'Content 1' },
  { id: 2, title: 'Post 2', content: 'Content 2' },
  { id: 3, title: 'Post 3', content: 'Content 3' }
])
</script>

<style scoped>

</style>