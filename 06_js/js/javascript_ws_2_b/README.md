목표
학습 주제
JavaScript 배열과 객체 순회

학습 목표
JavaScript의 배열과 객체를 순회하는 방법 이해
배열 순회를 위한 for, for…of 문과 다양한 배열 메서드를 활용하는 방법을 습득
객체 순회를 위한 for...in 문을 활용하는 방법을 익힘

학습 개념
변수 선언
let
블록 스코프(block scope)를 갖는 지역 변수를 선언
재할당 가능
재선언 불가능

const
 블록 스코프를 갖는 지역 변수를 선언
재할당 불가능
재선언 불가능

while
조건문이 참이면 문장을 계속해서 수행
while (조건문) {
  // do something
}

let i = 0

while (i < 6) {
  // console.log(i)
  i += 1
}

for
특정한 조건이 거짓으로 판별될 때까지 반복
for ([초기문]; [조건문]; [증감문]) {
  // do something
}

for (let i = 0; i < 6; i++) {
  // console.log(i)
}

for…in
객체의 열거 가능한 속성(property)에 대해 반복
for (variable in object) {
  statement
}

const fruits = { a: 'apple', b: 'banana' }

for (const property in object) {
  // console.log(property) // a, b
  // console.log(object[property]) // apple, banana
}

for…of
반복 가능한 객체(배열, 문자열 등)에 대해 반복
for (variable of iterable) {
  statement
}

const numbers = [0, 1, 2, 3]

for (const number of numbers) {
  // console.log(number) // 0, 1, 2, 3
}

학습 방향
JavaScript에서 배열과 객체를 순회하는 다양한 방법을 학습하여 데이터를 효율적으로 처리하는 방법을 이해한다.
배열과 객체를 순회하면서 각 요소에 접근하고 조작하는 기술을 연습하여 실제 개발에서의 활용도를 높인다.
다양한 순회 방법을 활용하여 배열과 객체를 처리하는 실습을 통해 개발자의 역량을 향상시킨다.
문제
JavaScript의 반복문을 연습하고자 한다. 주어진 실행 결과 화면을 참고하여 요구 사항을 만족하는 코드를 작성하시오.
요구사항
주어진 배열 studentNames를 순회하여 요소들을 출력하시오.
for ... of 문을 사용한다.
혹은 for ... 문을 사용할 수도 있다.

주어진 객체 studentAges를 순회하여 각 속성의 값들을 출력하시오.
for ... in 문을 사용한다.
