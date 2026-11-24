목표
학습 주제
JavaScript 함수를 활용한 배열과 객체 다루기

학습 목표
JavaScript에서 함수를 활용하여 배열과 객체를 다루는 방법 이해
다양한 배열과 객체 조작 예제를 통해 함수를 활용하여 데이터를 처리하는 방법 연습

학습 개념
function
참조 자료형에 속하며 모든 함수는 Function object
return 값이 없다면 undefined를 반환

함수 선언식
function name ([param[, param,[..., param]]]) { 
  statements
  return value
}

함수 표현식
 함수 이름이 없는 ‘익명 함수’를 사용할 수 있음
호이스팅 되지 않으므로 함수를 정의하기 전에 먼저 사용할 수 없음
let funcName = function () {
  statements
}

Object
키로 구분된 데이터 집합을 저장하는 자료형
중괄호(‘{}’)를 이용=> `hello, ${name}`e}`
중괄호 안에는 key: value 쌍으로 구성된 속성(property)를 여러 개 작성 가능
key는 문자형만 허용
value는 모든 자료형 허용
let user = {
  name: 'Alice',
  'key with space': true,
  greeting: function () {
    return 'hello'
  }
}

Callback function
다른 함수에 인자로 전달되는 함수
외부 함수 내에서 호출되어 일종의 루틴이나 특정 작업을 진행
let numbers2 = [1, 2, 3]
let callBackFunction = function (num) {
  // pass
﻿}
numbers2.forEach(callBackFunction)

Array Helper Method
배열 조작을 보다 쉽게 수행할 수 있는 특별한 메서드 모음

forEach
배열 내의 모든 요소 각각에 대해 함수(콜백함수)를 호출
반환 값 없음

map
배열 내의 모든 요소 각각에 대해 함수(콜백함수)를 호출
함수 호출 결과를 모아 새로운 배열을 반환

filter 
콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열을 반환

find 
콜백 함수의 반환 값이 참이면 해당 요소를 반환

some
배열의 요소 중 적어도 하나라도 콜백 함수를 통과하면 true를 반환하며 즉시 배열 순회 중지
반면에 모두 통과하지 못하면 false를 반환

every
배열의 모든 요소가 콜백 함수를 통과하면 true를 반환
반면에 하나라도 통과하지 못하면 즉시 false를 반환하고 배열 순회 중지

학습 방향
JavaScript에서 함수를 활용하여 배열과 객체를 효율적으로 다루는 방법을 학습하여 데이터 처리와 관리 능력을 향상시킨다.
배열을 다루는 다양한 함수와 객체를 다루는 다양한 함수를 익히고, 이를 조합하여 복잡한 데이터 구조를 다루는 능력을 기른다.
다양한 예제를 통해 함수를 활용하여 배열과 객체를 다루는 방법을 실습하여 프로그래밍의 유연성을 키우고, 코드의 가독성을 높인다.
문제
전교생이 5명인 작은 섬 마을 학교에서 최근 중간고사를 치렀다. 선생님은 각 학생의 이름과 과목 3개에 대한 시험 성적을 가지고 있다. 
선생님은 학생들의 평균 성적을 계산하는 프로그램을 작성해야 한다. 
요구 사항에 맞춰 프로그램을 작성하시오.
요구사항
공통 사항
작성하는 함수는 객체를 반환한다.
반환하는 객체의 각 속성은 학생의 이름, 값은 해당하는 평균 점수를 나타낸다.

함수 makeAvgScores1
Javascript의 'for' statement를 활용하여 작성한다.

함수 makeAvgScores2
Javascript의 'for...of' statement를 활용하여 작성한다.

함수 makeAvgScores3
'Array Helper Methods'를 활용하여 작성한다.
