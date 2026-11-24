목표
학습 주제
Pinia와 axios를 활용한 Vue 애플리케이션 개발


학습 목표
Pinia의 기본 개념 및 동작 방식 이해
axios를 활용하여 API 통신을 수행하는 방법 이해
Pinia를 axios를 결합하여 Vue.js 애플리케이션 개발

학습 개념

AJAX(Asynchronous JavaScript and XML)
비 동기식 JavaScript와 XML로 서버와 통신을 하기 위해서 XMLHttpRequest 객체를 활용합니다.
JSON, XML, HTML 그리고 일반 텍스트 형식 등을 포함한 다양한 포맷을 주고받을 수 있습니다.
페이지 전체를 ‘새로고침’하지 않고서도 수행되는 “비동기성”을 가집니다.(일부만 업데이트도 가능)

Promise Methods

.then(callback)Promise 객체를 반환하고, 이행했을 때와 거부했을 때 총 두 개의 콜백 함수를 인수로 받습니다.콜백 함수는 이전 작업의 성공 결과를 인자로 전달받습니다.
.catch(callback).then 이 하나라도 실패(거부)하면 동작되며, 이전 작업의 실패로 생성된 error 객체는 catch 블록 안에서 사용 가능합니다.
.finally(callback)Promise 객체를 반환하며, 결과 상관없이 무조건 실행됩니다.
axios
브라우저와 nods.js에서 사용할 수 있는 Promise 기반 HTTP 클라이언트 라이브러리로 Vue에서 권고하는 HTTP 통신 라이브러리입니다.
axios API
axios( config )axios( url [, config] )axios.get( url [, config] )axios.delete( url [, config] )axios.post( url [,data [, config]] )axios.put( url [,data [, config]] )


학습 방향
문제
학습 문제

개발자 Ben은 자체 상품들에 대한 재고 관리를 끝내고 판매까지 모두 마치게 되었다. 마지막으로 이제는 자체 상품이 아닌 외부 업체에 발주를 넣어서 새로운 상품을 받아 창고를 채우려고 한다. 
요구 사항에 맞게 애플리케이션을 작성하시오.
이전 문제 'Getters, Actions 연습하기'에서 풀이한 프로젝트 또는 제공된 스켈레톤 프로젝트에서 진행한다.
API를 활용한 외부 데이터 활용
axios를 설치 및 활용한다.
안내된 API로 요청을 보낸 후 받은 응답 데이터를 활용한다.
기존의 직접 작성했던 'products' state 값은 이 응답 데이터로 대체된다.
API에 요청을 보내고 응답 데이터를 'products' state에 할당하는 action은 'useProductStore'에 작성한다.
애플리케이션이 실행되면서 상품 목록 또한 함께 출력되어야 한다.


참고
https://jsonplaceholder.typicode.com/posts