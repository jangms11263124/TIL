<template>
  <div>
    <h1>회원가입</h1>
    <form @submit.prevent="signUp">
      <div>
        <label for="username">username</label>
        <input type="text" id="username" v-model.trim="username" />
      </div>
      <div>
        <label for="password1">Password</label>
        <input type="password" id="password1" v-model.trim="password1" />
      </div>
      <div>
        <label for="password2">Password Confirm</label>
        <input type="password" id="password2" v-model.trim="password2" />
      </div>
      <button type="submit">Sign Up</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from "axios";
import {useTodoStore} from "@/stores/todoStore.js";

const store = useTodoStore();
const username = ref('');
const password1 = ref('');
const password2 = ref('');

const signUp = () => {
  axios({
    url: `${store.BASE_URL}/accounts/signup/`,
    method: 'POST',
    data: {
      username: username.value,
      password1: password1.value,
      password2: password2.value
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