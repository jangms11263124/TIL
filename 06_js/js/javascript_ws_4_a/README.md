목표
학습 주제
JavaScript 이벤트의 버블링과 캡처링

학습 목표
JavaScript 이벤트의 버블링과 캡처링에 대한 개념 이해
이벤트 버블링과 캡처링이 발생하는 과정을 이해하고 구분하는 방법 습득
이벤트 버블링과 캡처링을 활용하여 이벤트 핸들링을 보다 효율적으로 제어하는 방법을 익힘

학습 개념
Document.querySelector(selector)
제공한 선택자 또는 선택자 뭉치와 일치하는 문서 내 첫 번째 Element 를 반환
일치하는 요소가 없으면 null을 반환

Element.classList
엘리먼트의 클래스 속성 DOMTokenList 를 반환

element.classList.add()
지정한 클래스 값을 추가

element.classList.remove()
지정한 클래스 값을 제거

element.classList.toggle()
클래스가 존재한다면 제거하고 false를 반환
존재하지 않으면 클래스를 추가하고 true를 반환

Callback function
다른 함수에 인자로 전달되는 함수
외부 함수 내에서 호출되어 일종의 루틴이나 특정 작업을 진행
let numbers2 = [1, 2, 3]
let callBackFunction = function (num) {
  // pass
﻿}
numbers2.forEach(callBackFunction)

event
 DOM에서 이벤트가 발생했을 때 생성되는 객체
모든 DOM 요소는 이러한 event를 만들어 냄

event handler
이벤트가 발생했을 때 실행되는 함수
사용자의 행동에 어떻게 반응할지를 JavaScript 코드로 표현한 것

.addEventListener()
대표적인 이벤트 핸들러 중 하나
특정 이벤트를 DOM 요소가 수신할 때마다 콜백 함수를 호출

type
수신할 이벤트 이름
문자열로 작성 (ex. ‘click’)

 handler
발생한 이벤트 객체를 수신하는 콜백 함수
콜백 함수는 발생한 event object를 유일한 매개변수로 받음
EventTarget.addEventListener(type, handler)

// 1. 버튼 선택
const btn = document.querySelector('#btn')
// 2. 콜백 함수
const detectClick = function (event) {
  // console.log(event) // PointerEvent
  // console.log(event.currentTarget) // <button id="btn">버튼</button>
  // console.log(this) // <button id="btn">버튼</button>
}
// 3. 버튼에 이벤트 핸들러를 부착
btn.addEventListener('click', detectClick)


학습 방향
JavaScript 이벤트의 버블링과 캡처링에 대한 개념을 학습하여 이벤트 처리 메커니즘을 이해한다.
실제로 발생하는 이벤트 버블링과 캡처링의 과정을 이해하여 웹 애플리케이션의 동작을 예측하고 제어할 수 있는 능력을 키운다.
버블링과 캡처링을 활용하여 이벤트를 효율적으로 제어하고 중첩된 요소에서의 이벤트 처리를 보다 효율적으로 구현하는 연습을 한다.
문제
JavaScript의 버블링과 캡처링의 동작 원리를 이해하고자 한다. 제시된 코드를 참고하여 요구사항을 만족하는 코드를 작성하시오.
요구사항
테이블의 각 셀 요소를 클릭하면 class 속성 theme-color가 추가된다.
만약 클릭 한 셀 요소에 이미 class 속성 theme-color가 있다면 제거한다.

단, 각 셀 요소에 직접 addEventListener를 적용하지 않는다.
table 요소에 addEventListener를 적용하고, 각 셀에서 발생한 이벤트가 버블링되어 table에 전달되면 적절한 callBack Function이 작동되어야 한다.

HTML table 요소 참고
https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table
