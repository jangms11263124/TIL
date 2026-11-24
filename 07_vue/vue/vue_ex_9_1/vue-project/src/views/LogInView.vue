<template>
  <div>
    <h1>로그인</h1>
    <form @submit.prevent="logIn">
      <div>
        <label for="id">username</label>
        <input type="text" id="id" v-model.trim="username" />
      </div>
      <div>
        <label for="password">Password</label>
        <input type="password" id="password" v-model.trim="password" />
      </div>
      <button type="submit">Log In</button>
    </form>
  </div>

</template>

<script setup>
import { ref } from 'vue'
import axios from "axios";
import {useTodoStore} from "@/stores/todoStore.js";
const username = ref('');
const password = ref('');
const store = useTodoStore();
const logIn = () => {
  axios({
    url: `${store.BASE_URL}/accounts/login/`,
    method: 'POST',
    data: {
      username: username.value,
      password: password.value
    }
  }).then(response => {
    console.log(response);
  }).catch(error => {
    console.log(error);
  });
}

</script>

<style scoped>

</style>