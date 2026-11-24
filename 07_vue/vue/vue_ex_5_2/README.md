목표
학습 주제
Props와 emit event를 활용한 컴포넌트 간 데이터 흐름 관리


학습 목표
Props를 사용하여 데이터를 하위 컴포넌트로 전달하는 방법 이해
컴포넌트 이벤트를 발생시켜 부모 컴포넌트로 이벤트를 전달하는 방법 이해
Props 및 이벤트를 활용하여 Vue 애플리케이션에서 유연한 데이터 흐름을 구축하는 방법 습득


학습 개념

•	Dynamic propsv-bind와 함께 사용하여 동적으로 할당된 props를 사용할 수 있습니다.(단, 선언 및 템플릿 참조 시에는 camelCase, 자식 컴포넌트 전달 시에는 kebab-case를 사용합니다)
부모 컴포넌트에서 Dynamic props 정의하기(템플릿에서는 kebab case로 전달하기)  
import { ref } from 'vue'

const name = ref('Alice')﻿

<!-- Parent.vue -->

<ParentChild :dynamic-props="name" />﻿﻿

자식 컴포넌트에서 Dynamic props 선언 및 출력하기(스크립트에서는 camel case로 받아오기) 
<!-- ParentChild.vue -->

<p>{{ dynamicProps }}</p>

defineProps({
  dynamicProps: String
})﻿﻿

학습 방향
문제
학습 문제

Maria는 상품 목록을 보여주는 화면을 만드는 데 성공했다. 하지만 각 상품 목록을 개별 컴포넌트로 관리하고 싶어 하위 컴포넌트를 생성해 전체적인 구조를 수정하고자 한다. 요구 사항에 맞게 애플리케이션을 작성하시오.
이전 문제 'Props를 이용한 v-for 연습하기'에서 풀이한 프로젝트 또는 제공된 스켈레톤 프로젝트에서 진행한다.
ProductList 컴포넌트
App 컴포넌트로부터 전달받은 props인 products를 순회하여, 개별 객체 요소를 props로 하위 컴포넌트에 전달한다.
ProductListItem 컴포넌트
ProductList 컴포넌트의 하위 컴포넌트이다.
ProductList 컴포넌트로부터 products의 개별 객체 요소를 props로 전달받는다.
전달받은 각 객체의 name 속성과 price 속성을 출력한다.
출력된 개별 요소와 함께 '장바구니 추가' 버튼을 출력한다.