목표
학습 주제
Vue에서의 이벤트 핸들링


학습 목표
Vue에서의 이벤트 핸들링을 위한 기본 문법을 이해한다.
이벤트 핸들러를 사용하여 사용자 상호작용에 반응하는 방법을 습득한다.


학습 개념
v-on
DOM 요소에 v-on을 통해 Event Listener를 연결 및 수신할 수 있으며, 약어는 아래와 같이 @로 표현됩니다.
v-on:event="handler"
@event="handler"﻿

Handler의 형태에 따라 Inline Handlers, Method Handlers로 나뉩니다.Inline Handlers는 비교적 간단한 명령 수행 시에 사용되며, Method Handlers는 Method를 정의하여 할당할 때 사용됩니다.
<!-- event-listener.html -->
<div id="app">
  <button v-on:click="increment">{{ count }}</div>
</div>

<script>
  const { createApp, ref } = Vue

  const app = createApp({
    setup() {
      const count = ref(0)
      const increment = function () {
        count.value++
      }
      return {
        count,
        increment
      }
  }
})﻿﻿﻿﻿﻿﻿﻿



학습 방향
문제
학습 문제
Vue3의 이벤트 리스너를 활용한 상태 업데이트를 하고자 한다. 요구 사항을 만족하는 코드를 작성하시오.

정수 0 값을 가지는 반응형 변수 count를 선언한다.
HTML h1 요소의 콘텐츠로 렌더링 된다.
함수 increment
템플릿의 '+' 버튼을 클릭하면 호출된다.
호출하면 반응형 변수 count의 값을 1만큼 증가시킨다.
increment는 setup()에서 반환된 객체의 메서드이다.
함수 decrement
템플릿의 '-' 버튼을 클릭하면 호출된다.
호출하면 반응형 변수 count의 값을 1 만큼 감소시킨다.
decrement는 setup()에서 반환된 객체의 메서드이다.
참고
v-on 디렉티브를 사용하여 DOM 이벤트를 수신할 수 있다.

참고

v-on: https://vuejs.org/guide/essentials/event-handling.html