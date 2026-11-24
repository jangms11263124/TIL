목표
학습 주제
Vue 동적 데이터 렌더링을 활용한 애플리케이션 구현


학습 목표
Vue를 활용하여 HTML 요소에 동적으로 데이터를 렌더링하는 방법 이해
Vue 디렉티브를 사용하여 데이터와 DOM 요소를 연결하고 동적으로 화면을 업데이트하기


학습 개념
v-show
v-show는 표현식 값의 T/F를 기반으로 요소의 가시성(visibility)을 전환합니다. v-show 요소는 항상 렌더링 되어 DOM에 남아있다는 특징을 가집니다.v-show의 표현식 값이 false일 때도 해당 태그가 사라지는 것이 아니라, 아래와 같이 display: none 스타일이 적용됩니다.
const isShow = ref(false)

<div v-show="isShow">v-show</div>

<div style="display: none;">v-show</div>﻿


학습 방향
문제
학습 문제
Vue의 동적 데이터 바인딩과 이벤트 핸들링을 활용해 카드 생성기 애플리케이션을 작성하고자 한다. 주어진 코드를 활용하여 요구 사항을 만족하는 코드를 작성하시오.

사용자 input 관련 반응형 변수 (inputTitle, inputContent, inputColor)
순서대로 카드의 제목, 내용, 배경색을 입력받는 변수를 나타낸다.
적절한 HTML의 각 input의 값과 양방향 바인딩된다.
카드 관련 반응형 변수 (cardTitle, cardContent, cardColor)
순서대로 만들어진 카드의 제목, 내용, 배경색을 나타낸다.
각 변수는 inputTitle, inputContent, inputColor의 값을 활용하여 할당한다.
반응형 변수 isCreatedCard
카드 생성 여부를 나타내는 변수이며, class 속성 card를 가진 div 요소에 적용된다.
초기 값으로 Boolean 타입 'false'를 가진다.
함수 createCard가 호출되면 'true'로 변경된다.
true로 변경되면 카드가 화면에 출력된다.
`v-show` directive를 활용한다.
함수 createCard
HTML form 요소에서 submit 이벤트가 발생하면 호출된다.
반응형 변수 isCreatedCard를 true로 변경한다.
반응형 변수 inputTitle, inputContent, inputColor를 초기화한다.
createCard은 setup()에서 반환된 객체의 메서드이다.
