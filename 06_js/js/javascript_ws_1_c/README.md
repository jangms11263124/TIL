목표
학습 주제
DOM API를 활용한 문서 조작

학습 목표
DOM API를 활용하여 새로운 HTML 요소를 동적으로 생성하는 방법을 이해
JavaScript를 사용하여 Article(기사) 요소의 구조를 생성하고 콘텐츠를 채우는 방법을 습득
동적으로 생성된 Article 요소를 웹 페이지에 삽입하여 보여주는 방법을 익힘

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

Element.classList
엘리먼트의 클래스 속성 DOMTokenList 를 반환

element.classList.add()
지정한 클래스 값을 추가

element.classList.remove()
지정한 클래스 값을 제거

element.classList.toggle()
클래스가 존재한다면 제거하고 false를 반환
존재하지 않으면 클래스를 추가하고 true를 반환

Element.setAttribute(name, value)
지정된 요소의 속성 값을 설정
속성이 이미 있으면 기존 값을 갱신 (그렇지 않으면 지정된 이름과 값으로 새 속성이 추가

document.createElement(tagName)
﻿﻿﻿﻿작성한 tagName의 HTML 요소를 생성하여 반환


학습 방향
DOM API를 사용하여 동적으로 HTML 요소를 생성하는 과정을 익히고, 웹 페이지에 적용해 보며 이해도를 높인다.
Article 요소의 구조를 생성하고 콘텐츠를 채워서 동적으로 만드는 과정을 실습하여 실제 웹 개발에 적용할 수 있는 기술을 습득한다.
실습을 통해 Article 요소를 생성하는 것이 어떻게 활용되는지를 이해하고, 실제 웹 애플리케이션에서 Article 요소를 동적으로 생성하여 표시하는 능력을 기른다.
문제
JavaScript를 활용하여 첨부된 실행 결과와 동일한 구조의 Article 구조를 생성하시오. 본문 내용은 자유롭게 구성하시오.
요구사항
실행 결과를 참고하여 동일한 구조가 될 수 있도록 코드를 작성한다.
HTML 마크업을 직접 수정하지 않는다.
JS를 작성하여 필요한 요소를 생성하고, 적절한 속성을 부여한다.
