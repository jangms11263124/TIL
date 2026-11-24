목표
학습 주제
DOM API를 사용한 HTML 요소 선택과 출력

학습 목표
DOM API를 이용하여 HTML 문서에서 요소를 선택하는 방법 이해
선택한 요소를 효과적으로 조작하여 웹 페이지에 출력하는 방법을 습득
JavaScript를 사용하여 동적으로 웹 페이지를 변경하는 기술을 연습

학습 개념
CSS 선택자
CSS 선택자는 CSS 규칙을 적용할 요소를 정의

클래스 선택자
주어진 class 특성을 가진 모든 요소를 선택
구문: .classname
예제: .index는 "index" 클래스를 가진 모든 요소

ID 선택자
id 특성에 따라 요소를 선택
문서 내에는 주어진 ID를 가진 요소가 하나만 존재해야 함
구문: #idname
예제: #toc는 "toc" ID를 가진 요소

Document.querySelector(selector)
제공한 선택자 또는 선택자 뭉치와 일치하는 문서 내 첫 번째 Element 를 반환
일치하는 요소가 없으면 null을 반환

Document.querySelectorAll(selector)
제공한 선택자 또는 선택자 뭉치와 일치하는 모든 Element List 반환
<body>
  <h1 class="heading">DOM 선택</h1>
  <!-- <a href="https://www.google.com/">google</a> -->
  <!-- <p class="content">content1</p> -->
  <ul> 
    <li>list1</li> 
    <li>list2</li> 
  </ul>﻿﻿
  <script>
    console.log(document.querySelector('.heading'))
    console.log(document.querySelector('.content'))
    // console.log(document.querySelectorAll('.content'))
    // console.log(document.querySelectorAll('ul > li'))
  </script>
</body>


console.log()
웹 콘솔에 메시지를 출력
console.log(obj1 [, obj2, ..., objN]);
console.log(msg [, subst1, ..., substN]);


학습 방향
DOM API를 사용하여 HTML 요소를 선택하는 과정을 익히고, 선택한 요소를 조작하는 방법을 연습한다.
JavaScript를 통해 웹 페이지를 동적으로 조작할 수 있는 능력을 키우며, 이를 통해 웹 개발에 필수적인 기술을 습득한다.

문제
JavaScript를 사용하여 DOM을 조작하는 연습을 해보고자 한다. 요구 사항을 만족하는 코드를 작성하시오.
요구사항
querySelector 혹은 querySelectorAll 중 적절한 메서드를 사용하여 문제를 해결하여야 한다. 
Hello world! 콘텐츠를 가지는 p 태그를 선택하여 pTag 변수에 할당하시오.
li 태그를 모두 선택하여 liTags 변수에 할당하시오.
pTag, liTags를 각각 브라우저 console 창에 출력하시오.