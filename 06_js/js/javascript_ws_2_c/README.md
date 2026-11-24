목표
학습 주제
JavaScript 반복문과 제어문

학습 목표
JavaScript에서 제공하는 반복문과 제어문의 종류와 사용법 이해
다양한 반복문과 제어문을 활용하여 프로그램의 흐름을 제어하는 방법을 습득

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

if
조건 표현식의 결과값을 boolean 타입으로 변환 후 참/거짓을 판단
if (name === 'admin') {
  // code
} else if (name === 'customer') {
  // code
} else {
  // code
}


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
JavaScript에서 제공하는 반복문과 제어문의 기본 개념과 사용법을 학습하여 프로그램의 흐름을 제어하는 방법을 이해한다.
실습을 통해 반복문과 제어문을 사용하여 다양한 문제를 해결하고, 프로그램을 구현하는 능력을 기른다.
반복문과 제어문을 적절히 활용하여 복잡한 로직을 구현하는 연습을 통해 개발자의 역량을 향상시킨다.
문제
JavaScript의 반복문과 제어문을 연습하고자 한다. 요구 사항을 만족하는 코드를 작성하시오.
요구사항
주어진 배열 studentNames만을 순회하여 실행결과 이미지와 일치하도록 출력하시오.
객체 studentAges에서 속성의 값이 50 이상인 경우만 출력하시오.
객체 studentAges를 순회하지 않도록 주의하시오.
for ... of 문을 사용한다.
혹은 for ... 문을 사용할 수도 있다.