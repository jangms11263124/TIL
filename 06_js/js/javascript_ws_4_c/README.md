목표
학습 주제
JavaScript 이벤트 핸들러와 DOM 조작

학습 목표
JavaScript를 사용하여 HTML 요소에 이벤트 핸들러를 등록하는 방법 이해
이벤트 핸들러를 활용하여 사용자 상호작용에 반응하는 기본적인 웹 애플리케이션 제작
DOM을 조작하여 웹 페이지의 구조를 변경하는 기초적인 기술 습득

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

.preventDefault()
해당 이벤트에 대한 기본 동작을 실행하지 않도록 지정


학습 방향
JavaScript 이벤트 핸들러를 등록하고 활용하는 방법을 익힌다.
이벤트 핸들러를 통해 사용자 상호작용에 반응하는 웹 애플리케이션을 구현하는 방법을 습득한다.
DOM을 조작하여 웹 페이지의 구조를 변경하는 기초적인 기술을 학습하고, 실습을 통해 활용한다.

문제
JavaScript의 이벤트 핸들러를 활용한 DOM 조작을 이해하고자 한다. 제시된 코드를 참고하여 요구사항을 만족하는 코드를 작성하시오.
요구사항
'text-input' class인 input 요소
작성하는 텍스트는 실시간으로 p 요소 컨텐츠에 입력된다.
input 요소에 focus가 잡히면 
p 요소의 폰트 크기를 2rem으로 변경한다. (fs-2 클래스 스타일 속성 활용)
p 요소의 배경 컬러를 회색으로 변경한다. (bg-color 클래스 스타일 속성 활용)
input 요소에 focus가 해제되면 
focus가 잡혔을 때 적용한 폰트 크기와 배경 컬러 스타일을 모두 해제한다.
작성하는 텍스트 길이가 5 초과라면 
 'warning' class인 span 요소를 화면에 출력한다. 
p 요소를 화면에 출력하지 않는다.
작성하는 텍스트 길이가 5 이하라면 
'warning' class인 span 요소를 화면에 출력하지 않는다. 
p 요소를 화면에 출력한다.

'color-input' class인 input 요소
작성하는 텍스트가 CSS의 폰트 컬러 값으로 p 요소 컨텐츠에 실시간 반영된다.M:M