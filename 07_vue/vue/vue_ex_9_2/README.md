목표
학습 주제
Django REST framework를 사용한 API 서버
개발 Vue.js와 Pinia를 사용한 애플리케이션 프론트 엔드 개발


학습 목표
Django 프로젝트를 생성하고 관리하는 방법을 익힌다.
Django REST framework를 활용하여 API 서버를 구축하는 방법을 습득한다.
Vue.js와 Pinia를 활용하여 프론트 엔드 프로젝트를 구축하는 방법을 익힌다.
기존 스켈레톤 코드를 기반으로 프로젝트를 생성하고 불필요한 컴포넌트와 코드를 삭제하는 능력을 키운다.


학습 개념
pinia-plugin-persistedstate
 Pinia의 플러그인(plugin) 중 하나웹 애플리케이션의 상태(state)를 브라우저의 local storage나session storage에 영구적으로 저장하고 복원하는 기능을 제공
설치 및 등록
$ npm i pinia-plugin-persistedstate

// main.js
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
const app = createApp(App)
const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)
// app.use(createPinia())
app.use(pinia)
app.mount('#app')

// stores/counter.js
export const useCounterStore = defineStore('counter', () => {…,
  return { todos, addTodo, deleteTodo, updateTodo, doneTodosCount }
}, { persist: true })

학습 방향
Django 프로젝트와 앱을 생성하고 관리하는 경험을 쌓는다.
Django 모델을 사용하여 데이터베이스 모델을 정의하고 관리하는 방법을 이해한다.
Vue.js와 Pinia를 사용하여 프로젝트를 초기화하고 관리하는 경험을 쌓는다.

문제
학습 문제
현재 프로젝트에는 회원 가입과 로그인에 필요한 기능과 화면이 구현되어있다. 해당 기능을 pinia store 를 통해 관리하고 사용할 수 있도록 주어진 요구사항을 만족하는 코드를 작성하시오
제공된 스켈레톤 프로젝트에서 진행한다.
'django-pjt'
가상 환경을 설정하고 gitignore를 생성한다.
프로젝트 실행에 필요한 라이브러리를 설치한다.
'vue-project'에 미리 작성된 프로젝트 구조를 파악한 뒤 아래 요구사항에 따라 진행한다.
'UserStore' store
src/stores 경로에 새로운 pinia store 'UserStore'를 생성한다.
useUserStore에 로그인 요청 성공 시 반환되는 token 값을 담을 'token' state를 정의한다.
'pinia-plugin-persistedstate'를 사용할 수 있도록 적절한 option을 추가한다.
API서버 요청시 사용될 'BASE_URL'을 정의한다.
인증 관련 기본 요청 주소는 'http://127.0.0.1:8000/accounts'이다.
로그인 요청과 회원가입 요청 기능을 수정한다.
LogInView 와 SignUpView에 각각 정의한 로그인 요청과 회원가입 요청 기능을 useUserStore로 옮긴다.
각 요청은 직접 axios 요청을 보내는 대신 새로 작성한 userStore에 있는 함수를 호출한다.
userStore의 signUp과 logIn에 'payload' 파라미터를 추가한다.
함수 호출 시 필요한 값을 'payload'에 담아 넘겨준다.
예시
const payload = {
  username: username.value,
  password: password.value
}
store.login(payload)
로그인 함수 수정
로그인 성공 응답에 담긴 'key'값을 useUserStore 정의한 반응형 변수 token에 담는다.
각 기능의 정상 동작 여부를 확인한다.

