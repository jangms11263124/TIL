목표
학습 주제
Vue를 사용하여 동적 UI 요소를 생성하고 데이터 바인딩을 구현하는 웹 애플리케이션 개발

학습 목표
Vue에서 반복 렌더링을 위한 디렉티브를 사용하는 방법 이해
반복되는 데이터를 Vue 컴포넌트에서 화면에 렌더링하는 방법
동적으로 생성된 Todo 목록을 화면에 표시하여 사용자에게 제공하는 방법

학습 개념

v-for
소스 데이터를 기반으로 요소 또는 템플릿 블록을 여러 번 렌더링합니다.(Array, Object, number, string, Iterable) v-for는 alias in expression 형식의 특수 구문을 사용하여 반복되는 현재 요소에 대한 별칭(alias)을 제공합니다.
<div v-for="item in items">
  {{ item.text }}
</div>﻿
 인덱스(객체에서는 키)에 대한 별칭을 지정할 수 있습니다.
<div v-for="(item, index)" in items"></div>
<div v-for="value in object"></div>
<div v-for="(value, key) in object"></div>
<div v-for="(value, key, index) in object"></div>﻿ ﻿﻿

 
v-for with key
v-for는 내부 컴포넌트의 상태를 일관되게 유지하고, 데이터의 예측 가능한 행동을 유지하기 위하여 key와 함께 쓰는 것이 권장됩니다.
<div v-for="item in items" :key="item.id">
  <!-- content -->
</div>﻿﻿
 
v-for with v-if
동일 요소에 v-if가 v-for보다 우선순위가 높기 때문에 동일 요소에 v-for와 v-if를 함께 사용하는 것은 바람직하지 않습니다.
학습 방향
문제
학습 문제
Alice는 바쁜 일정 속에서 자신의 할 일을 관리하기 위해 효율적인 방법을 찾고 있다. 종이에 메모하는 것으로는 한계가 있고, 간단한 애플리케이션을 통해 할 일을 더 효율적으로 관리할 수 있을 것으로 예상했다. 그래서 Vue를 사용하여 Todo 애플리케이션을 만들기로 결정했다. 첫 번째로 전체 할 일을 화면에 출력하고자 한다. 요구 사항에 맞춰 애플리케이션을 작성하시오.
"Vue 3의 반응성 시스템을 활용하여 할 일 목록을 표시하고, 체크박스의 선택 여부에 따라 해당 할 일의 완료 여부를 변경"
반응형 변수 todos
배열 todos에는 세 가지 할 일이 객체 형태로 포함되어 있다.
할 일 객체는 3가지 속성을 가진다. (id, text, isCompleted)
id 속성은 todos의 각 할 일을 구분하는 식별자 역할을 지닌다.
text 속성은 각 할 일이 무엇인지 문자열 값을 가진다.
isCompleted 속성은 각 할 일의 완료 여부로 Boolean 타입 값을 가진다.
todos 목록 렌더링
v-for 디렉티브를 사용하여 todos 배열의 각 항목을 순회한다.
각 항목의 text 속성을 출력한다.
각 항목은 HTML li 요소에 콘텐츠로 렌더링 되어야 한다.
사용자가 할 일 항목을 완료할 수 있는지는 체크박스를 제공한다.
체크박스를 클릭함에 따라 isCompleted 속성 값이 토글 된다.
체크박스가 클릭되면 제공된 CSS 클래스 선택자 `is-completed`를 적용한다.