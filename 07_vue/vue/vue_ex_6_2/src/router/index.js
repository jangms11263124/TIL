import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import UserView from '../views/UserView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: AboutView
    },
    {
      // 동적 파라미터 등록
      path: '/user/:username',
      name: 'user',
      component: UserView,
      // 내비게이션 가드 설정
      beforeEnter: (to, from) => {
        const currentUser = to.params.username

        if (currentUser !== 'admin') {
          // 관리자가 아니라면 경고창을 띄우고 home 주소로 이동
          alert('관리자만 접근할 수 있는 페이지입니다.')
          return { name: 'home' }
        }
      }
    }
  ]
})

export default router
