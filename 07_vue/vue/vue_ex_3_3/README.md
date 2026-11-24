목표
학습 주제
Vue를 사용하여 동적 UI 요소를 생성하고 데이터 바인딩을 구현하는 웹 애플리케이션 개발


학습 목표
Vue에서 데이터를 필터링하여 특정 조건에 맞는 항목만 화면에 표시하는 방법 이해
사용자가 선택한 필터링 옵션에 따라 데이터 목록을 동적으로 변경하는 방법 습득
필터링된 데이터 목록을 효과적으로 관리하고 화면에 표시하는 방법을 익힘


학습 개념

computed()
computed는 계산된 속성을 정의하는 함수입니다.미리 계산된 속성을 사용하여 템플릿에서 표현식을 단순하게 하고 불필요한 반복 연산을 줄입니다.
const { createApp, ref, computed } = Vue

const restOfTodos = computed(() => {
  return todos.value.length > 0 ? '아직 남았다' : '퇴근!'
})﻿﻿

반환되는 값은 computed ref이며 refs와 유사하게 계산된 결과를 .value로 참조할 수 있습니다(템플릿에서는 .value 생략 가능).
Computed 속성은 의존된 반응형 데이터를 기반으로 캐시(cached)됩니다.의존하는 데이터가 변경된 경우에만 재평가되며, 따라서 의존하는 데이터가 변경되지 않는 경우에는 이전 계산 결과를 즉시 반환합니다.
watch()
반응형 데이터를 감시하고, 감시하는 데이터가 변경되는 콜백 함수를 호출합니다.
<input v-model="message">
<p>Message length: {{ messageLength }}</p>

const message = ref('')
const messageLength = ref(0)

const messageWatch = watch(message, (newValue, oldValue) => {
  messageLength.value = newValue.length
})

위처럼 감시하는 변수(message)에 변화가 생겼을 때 연관 데이터를 업데이트 해야 할 때 활용할 수 있습니다.

학습 방향
문제
학습 문제

마지막으로 Alice는 각 할 일의 상태에 따라 별도로 필터링하여 출력을 하는 것으로 애플리케이션 개발을 마무리하고자 한다. 요구 사항에 맞춰 애플리케이션을 작성하시오.
"할 일 목록을 필터링하고 완료된 할 일의 개수를 표시하는 Todo 애플리케이션 구현"
완료된 할 일의 개수 (watch)
체크박스를 클릭하면 해당 항목이 완료되었다고 간주되며, 이때 해당 값을 실시간으로 업데이트한다.
`Completed Count: ` 콘텐츠를 가진 HTML p 요소에 출력된다.
Vue의 watch 함수를 참고한다.
할 일 목록 필터링 (computed)
필터 종류
전체 할 일 보기: 모든 할 일을 출력한다.
완료된 할 일 보기: 완료된 할 일만 출력한다.
미완료된 할 일 보기: 완료되지 않은 할 일만 출력한다.
첫 화면에는 미완료된 할 일 보기가 선택되어 있어야 한다.
HTML select와 option 요소를 활용하며, 기존 form 요소의 하위 요소에 작성한다.
Vue의 computed 속성을 참고한다.

참고