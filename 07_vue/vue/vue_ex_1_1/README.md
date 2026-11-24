목표
학습 주제
Vue3 선언적 렌더링


학습 목표
Vue.js의 선언적 렌더링이란 무엇인지 이해한다.
Vue3에서의 선언적 렌더링 문법을 습득한다.
데이터와 UI 간의 반응형 관계를 설정하고 업데이트하는 방법을 익힌다.


학습 개념
Vue3 CDN 사용법
다음의 태그를 추가하면 별도의 설치 없이 Vue3를 CDN 방식으로 이용할 수 있습니다.
<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>

app.mount()
Vue 속성 중 createApp을 사용하여 App.Instance를 생성할 수 있습니다.
<!-- vue-instance.html -->

<div id="app"></div>

<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
<script>
  const { createApp } = Vue
  
  const app = createApp({})

  app.mount('#app')
</script>﻿﻿﻿﻿﻿

Vue 선언적 렌더링
HTML을 확장하는 템플릿 구문을 사용하여 HTML이 Javascript 데이터를 기반으로 어떻게 보이는지 설명할 수 있습니다.Vue 속성 중 ref를 사용하여 반응형을 가지는 참조 변수를 만들 수 있습니다.
script 내 ref 값에 접근하려면 "변수.value"와 같이 작성해야 합니다.
템플릿 내 ref 값을 사용하려면 "변수"만 작성해도 자동으로 렌더링됩니다.

<div id="app">
  ﻿<h1>{{ message }}</div>
</div>

const app = createApp({
  setup() {
    const message = ref('Hello Vue!')
    return {
      message 
    }
})

학습 방향﻿﻿﻿﻿﻿﻿
문제
학습 문제
Vue의 선언적 렌더링을 알아보기 위해 기본 동작 원리를 연습하고자 한다. 요구 사항을 만족하는 코드를 작성하시오.

Vue3 CDN을 사용한다.
createApp 함수로 이름이 app인 Vue Application instance를 생성한다.
HTML id 속성 값이 app인 div 요소에 Vue Application instance를 연결한다.
템플릿 참조에 관련된 코드를 작성하기 위해 setup 함수를 선언한다.
반응형 변수 message에 'Hello, Vue 3!' 문자열을 할당한다.
브라우저 console에 변수 message의 값인 'Hello, Vue 3!'를 출력한다.
setup 함수에서 반응형 변수 message를 반환한다.
반환된 변수 message 값을 템플릿에 동적 텍스트로 렌더링한다.
HTML h1 요소의 콘텐츠로 사용한다.
반응형 변수 message의 값을 'Bye, Vue 3!'로 변경한다.