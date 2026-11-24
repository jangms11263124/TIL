목표
학습 주제
DOM API를 사용한 HTML 속성 및 클래스 속성 조작 

학습 목표
DOM API를 활용하여 HTML 요소의 속성을 읽고 수정하는 방법을 이해
HTML 요소의 클래스 속성을 추가, 제거, 토글하는 방법을 습득
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

자식 결합자
> 결합자는 첫 번째 요소의 바로 아래 자식인 노드를 선택
구문: A > B 
예제: ul > li는 <ul> 요소 바로 아래에 위치하는 모든 <li> 요소

Document.querySelector(selector)
제공한 선택자 또는 선택자 뭉치와 일치하는 문서 내 첫 번째 Element 를 반환
일치하는 요소가 없으면 null을 반환

Document.querySelectorAll(selector)
제공한 선택자 또는 선택자 뭉치와 일치하는 모든 Element List 반환

console.log()
웹 콘솔에 메시지를 출력

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


학습 방향
DOM API를 사용하여 HTML 요소의 속성을 조작하는 과정을 익히고, 실제로 적용해 보며 이해도를 높인다.
클래스 속성을 추가, 제거, 토글하는 방법을 습득하여 웹 페이지의 스타일링을 동적으로 변경하는 능력을 키운다.
실습을 통해 HTML 속성 및 클래스 속성을 조작하는 것이 어떻게 활용되는지를 이해하고, 실제 웹 개발에 적용할 수 있는 능력을 기른다.
문제
JavaScript를 사용하여 DOM을 조작하는 연습을 해보고자 한다. 요구 사항을 만족하는 코드를 작성하시오.
요구사항
querySelector 혹은 querySelectorAll 중 적절한 메서드를 사용하여 문제를 해결하여야 한다.
Hello world! 콘텐츠를 가지는 p 태그를 선택하여 pTag 변수에 할당하시오.
pTag 클래스에 'text-red' 클래스를 추가하여 스타일을 적용하시오.
a 태그를 선택하여 aTag 변수에 할당하시오.
aTag의 속성 href에 'https://www.google.com/'를 적용하시오.
