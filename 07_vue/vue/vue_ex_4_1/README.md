목표
학습 주제
Vite를 사용하여 웹 프로젝트 초기 설정 및 컴포넌트 구조를 활용한 애플리케이션을 만드는 방법


학습 목표
Vite를 이용하여 Vue 프로젝트를 초기화하고 필요한 파일 및 폴더를 구성하는 방법
생성한 컴포넌트를 메인 애플리케이션 파일에 등록하여 화면에 렌더링


학습 개념

Single-File Components(SFC)
Component란?UI를 독립적이고 재사용 가능한 일부분으로 분할한 요소SFC는 컴포넌트의 템플릿, 로직 및 스타일을 하나의 파일로 묶어낸 특수한 파일 형식입니다. (*.vue 파일)
SFC 구성
각 *.vue 파일은 세 가지 유형의 최상위 언어 블록 <template>, <script>, <style>으로 구성되며, 언어 블록의 작성 순서는 상관 없으나 일반적으로 template, script, style 순서로 작성합니다.
<template>
  <div class="greeting">{{ msg }}</div>
</template>

<script setup>
  import { ref } from 'vue'

  const msg = ref('Hello World!')
</script>

<style scoped>
  .greeting {
    color: red;
  }
</style>﻿﻿﻿﻿﻿﻿

<template>각 *.vue 파일은 최상위 <template> 블록을 하나만 포함 할 수 있습니다.
<script setup>각 *.vue 파일은 하나의 <script setup> 블록만 포함할 수 있습니다(일반 <script> 제외).컴포넌트의 setup() 함수로 사용되며 컴포넌트의 각 인스턴스에 대해 실행됩니다.
<style scoped>*.vue 파일은 여러 <style> 태그가 포함될 수 있으며, scoped가 지정되면 CSS는 현재 컴포넌트에만 적용됩니다.

학습 방향
문제
학습 문제

사진 촬영을 취미로 가진 Emily는 자신이 찍은 사진을 관리하기 위해 갤러리 웹 페이지를 만들기로 결정했다. 그녀는 Vue.js와 Vite를 사용하여 애플리케이션을 개발할 계획이다.Emily는 페이지 상단에 제목이 표시되는 Header와, 사진들이 보이는메인 Gallery를 구성하려고 한다. 가장 먼저 프로젝트의 구조를 설정하고자 한다. 요구 사항에 맞게 애플리케이션을 작성하시오.
"초기 생성된 프로젝트 정리 및 레이아웃 구성"
프로젝트 명은 vue-project로 생성한다.
불필요한 컴포넌트와 assets들을 모두 삭제한다.
components/ 폴더의 모든 컴포넌트
assets/ 폴더의 모든 파일
관련된 코드를 삭제한다.
App.vue에 작성된 불필요한 컴포넌트 components
main.js에 작성된 main.css import 문
components/ 폴더에 MyComponent 컴포넌트를 생성한다.
MyComponent는 App 컴포넌트의 하위 컴포넌트이다.
MyComponent는 크게 HTML header와 main 요소 2개로 구성된다.
제공된 sample 이미지는 assets/ 폴더에 위치한다.