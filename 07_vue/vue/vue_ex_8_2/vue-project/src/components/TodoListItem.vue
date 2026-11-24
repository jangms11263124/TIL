<template>
  <div>
    <p>{{ todo.work}}</p>
    <p>{{ todo.content}}</p>
    <p>{{ todo.is_completed}}</p>
    <p>{{ todo.created_at}}</p>
  </div>
  <hr/>
</template>

<script setup>
import { defineProps } from 'vue'
defineProps({
  todo: Object
})
</script>
