<template>
  <div v-if="selectedPost">
    <p>번호 : {{ selectedPost.id }}</p>
    <p>제목 : {{ selectedPost.title }}</p>
    <p>내용 : {{ selectedPost.content }}</p>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()

const posts = ref([
  { id: 1, title: 'Post 1', content: 'Content 1' },
  { id: 2, title: 'Post 2', content: 'Content 2' },
  { id: 3, title: 'Post 3', content: 'Content 3' }
])

// 현재 동적 URL 파라미터 :id와 매칭되는 게시글 필터링
const selectedPost = computed(() => {
  return posts.value.find(p => p.id === Number(route.params.id))
})
</script>

<style scoped>

</style>