목표
학습 주제
Vue를 사용한 동적 데이터 바인딩


학습 목표
Vue에서 데이터 바인딩을 사용하여 동적으로 화면을 업데이트하는 방법 이해
이벤트 핸들러를 사용하여 사용자의 동작에 반응하고, 데이터를 업데이트하는 방법을 습득
Vue 컴포넌트 내에서 데이터와 이벤트를 연결하여 상호작용하는 기본적인 웹 애플리케이션을 만들기


학습 개념
v-bind
하나 이상의 속성 또는 컴포넌트 데이터를 표현식에 동적으로 바인딩합니다.
v-bind shorthand(약어)
v-bind는 아래와 같이 ‘:’ (콜론)으로 줄일 수 있습니다.
<<!-- v-bind.html -->
<img v-bind:src="imageSrc">
<a v-bind:href="myUrl">Move to url</a>﻿﻿

<img :src ="imageSrc">
<a :href="myUrl">Move to url</a>﻿

v-bind 사용처
Attribute BindingsHTML의 속성 값을 Vue의 상태 속성 값과 동기화되도록 합니다.아래와 같이 사용되며 대괄호 속의 값은 해당 태그의 속성명이 되므로, 소문자 값이 권장됩니다(브라우저가 속성 이름을 소문자로 강제 변환).
<button :[key]="myValue"></button>

Class and Style Bindings클래스와 스타일 모두 속성이므로 v-bind를 사용하여 다른 속성과 마찬가지로 동적으로 문자열 값을 할당할 수 있습니다. 아래와 같이 객체를 :class에 전달하여 클래스를 동적으로 전환할 수 있습니다.(isActive의 T/F에 의해 active 클래스의 존재가 결정됨)
<!-- binding-html-classes.html -->
const isActive = ref(false)
<div :class="{ active: isActive }">Text</div>﻿

학습 방향
문제
학습 문제
Vue의 동적 데이터 바인딩과 이벤트 핸들링을 활용해 간단한 텍스트 스타일을 변경할 수 있는 기능을 구현하고자 한다. 주어진 코드를 활용하여 요구 사항을 만족하는 코드를 작성하시오.


반응형 변수 colorCrimson
문자열 'text-crimson' 값을 가진다.
HTML h1 요소의 클래스 속성 값에 바인딩하여 폰트 컬러를 변경한다.
반응형 변수 isDecorate
Boolean 타입 'false' 값을 가진다.
HTML p 요소의 클래스 속성 값에 바인딩하여 'text-decorate' 클래스 선택자를 적용한다.
함수 toggleDecorate
템플릿의 'Toggle Text Style' 버튼을 클릭하면 호출된다.
호출하면 반응형 변수 isDecorate 값을 토글 한다. (true <-> false)
toggleDecorate는 setup()에서 반환된 객체의 메서드이다.
