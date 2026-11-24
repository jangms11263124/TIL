목표
학습 주제
Vue.js를 사용하여 동적 UI 요소를 생성하고 데이터 바인딩을 구현하는 웹 애플리케이션 개발


학습 목표
Vue에서 사용자 입력을 받아 데이터를 추가하는 방법 이해
사용자가 입력한 데이터를 동적으로 화면에 추가하는 방법
사용자가 선택한 항목을 삭제하여 데이터를 업데이트하는 방법


학습 개념

JavaScript Date 객체
Date는 날짜를 저장할 수 있고, 날짜와 관련된 메서드도 제공해주는 JavaScript 내장 객체입니다.Date를 활용하면 생성 및 수정 시간을 저장하거나 측정할 수 있고, 현재 날짜를 출력하는 용도 등으로도 활용할 수 있습니다. 
현재 시간 가져오기
1. new Date().getTime()2. Date.now() 1에 비해 2의 방식은 객체를 만들지 않아도 된다는 차이점이 있습니다. 
Array 내장 메서드
 findIndex()배열에서 특정 조건을 만족하는 요소를 찾아 첫 번째 요소의 인덱스를 반환하는 메서드입니다.배열의 각 요소에 대해 콜백 함수를 사용하여 원하는 조건의 요소를 찾습니다.
const colors = ["red", "green", "blue"];

function findGreen(color) {
  return color === "green";
};

const green = colors.findIndex(findGreen);
console.log(green); // 출력: 1

splice()배열에서 특정 요소를 삭제, 추가, 교체하는 메서드입니다.
let months = ["January", "February", "Monday", "Tuesday"];
let days = months.splice(2, 1);

console.log(days); // ["Monday"]
console.log(months); // ["Janurary", "February", "Tuesday"]﻿

학습 방향
문제
학습 문제

모든 할 일 출력에 성공한 Alice는 이제 두 번째로 할 일을 직접 입력하는 텍스트 값을 받아 생성하고자 한다.나아가 잘못 입력한 할 일은 삭제할 수 있는 기능도 구현하고자 한다. 요구 사항에 맞춰 애플리케이션을 작성하시오.
"사용자의 입력을 받아 새로운 할 일을 추가하고, 삭제하는 기능 구현"
반응형 변수 todos
사용자가 입력 필드에 새로운 할 일을 입력하고 Add 버튼을 누르면 submit 이벤트가 발생한다.
submit 이벤트가 발생하면 새로운 할 일 객체가 추가되어야 한다.
할 일 객체는 3가지 속성(id, text, isCompleted)을 가지며 역할은 이전 `To-Do 리스트 클래스 바인딩 연습하기` 문제와 동일하다.
함수 addTodo
변수 todos에 새로운 할 일 객체를 추가하는 역할을 가진다.
HTML form 요소에서 submit 이벤트가 발생하면 호출된다.
새로운 할 일 객체의 id 속성 값은 JavaScript Date 객체의 now()를 활용한다.
사용자 입력 값이 없거나 공백을 입력했다면 할 일을 추가하지 않는다.
함수 deleteTodo
변수 todos에서 특정 할 일 객체를 삭제하는 역할을 가진다.
HTML li 요소 안에 Delete button을 클릭하면 호출된다.
id 속성 값을 활용해 어떤 할 일이 선택되었는지 찾는다.
선택된 할 일의 index를 찾아 todos 배열에서 삭제한다.
JavaScript 배열의 findIndex()와 splice()를 활용한다.

참고

Date: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date
findIndex: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/findIndex
splice: https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/splice