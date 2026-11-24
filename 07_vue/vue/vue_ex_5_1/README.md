목표
학습 주제
Props와 emit event를 활용한 컴포넌트 간 데이터 흐름 관리


학습 목표
Props를 사용하여 데이터를 하위 컴포넌트로 전달하는 방법 이해
컴포넌트 이벤트를 발생시켜 부모 컴포넌트로 이벤트를 전달하는 방법 이해
Props 및 이벤트를 활용하여 Vue 애플리케이션에서 유연한 데이터 흐름을 구축하는 방법 습득


학습 개념
•	Passing PropsProps란?부모 컴포넌트에서 자식 컴포넌트로 데이터를 전달하는데 사용되는 속성
One-Way Data Flow모든 props는 자식 속성과 부모 속성 사이에 하향식 단방향 바인딩을 형성합니다.양방향 바인딩을 하지 않는 이유는 하위 컴포넌트가 상위 컴포넌트의 상태를 변경하여 앱에서의 데이터 흐름을 이해하기 어렵게 만드는 것을 방지하기 위함입니다.

•	Props 사용하기부모 컴포넌트에서 props 정의 및 전달하기(템플릿에서는 kebab case로 전달하기)
import { ref } from 'vue'

const message = ref('Message')

<!-- Parent.vue -->

<template>
  <div>
    <ParentChild my-msg="message" />﻿﻿﻿
  </div>
</template>﻿

자식 컴포넌트에서 props 선언 및 출력하기(스크립트에서는 camel case로 받아오기) 
<!-- ParentChild.vue -->
<div>
  <p>{{ myMsg }}</p>
</div>﻿﻿﻿


 학습 방향
문제
학습 문제

Maria는 새로운 쇼핑 애플리케이션을 만들려고 한다. 그녀는 본인이 가지고 싶은 상품 목록을 장바구니에 담아 기록하고 공유하고 싶어한다. 첫 번째 단계로 상품 목록을 표시하는 화면을 만들기로 했다. 요구 사항에 맞게 애플리케이션을 작성하시오.
제공된 스켈레톤 프로젝트에서 진행한다.
ProductList 컴포넌트
 App 컴포넌트의 하위 컴포넌트이다.
 App 컴포넌트로부터 반응형 변수 products를 props로 전달받는다.
 전달받은 products를 순회하며 각 객체의 name 속성과 price 속성을 출력한다.
