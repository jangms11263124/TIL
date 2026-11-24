목표
학습 주제
Ajax를 사용한 클라이언트와 서버 간의 비동기 통신

학습 목표
Font Awesome 아이콘을 활용하여 좋아요 버튼을 스타일링하는 방법 습득
사용자가 버튼을 클릭할 때마다 버튼의 상태를 변경하고 스타일을 적절히 조절

학습 개념
data-*’ 속성
사용자 지정 데이터 특성을 만들어 임의의 데이터를 HTML과 DOM사이에서 교환 할 수 있는 방법
<div data-my-id="my-data"></div>
<script>
  const myId = event.target.dataset.myId
</script>

event
 DOM에서 이벤트가 발생했을 때 생성되는 객체
모든 DOM 요소는 이러한 event를 만들어 냄

.addEventListener()
대표적인 이벤트 핸들러 중 하나
특정 이벤트를 DOM 요소가 수신할 때마다 콜백 함수를 호출

.preventDefault()
해당 이벤트에 대한 기본 동작을 실행하지 않도록 지정

Axios
JavaScript에서 사용되는 HTTP 클라이언트 라이브러리
클라이언트 및 서버 사이에 HTTP 요청을 만들고 응답을 처리하는 데 사용되는 자바스크립트 라이브러리
서버와의 HTTP 요청과 응답을 간편하게 처리할 수 있도록 도와주는 도구
브라우저를 위한 XHR 객체 생성
간편한 API를 제공하며, Promise 기반의 비동기 요청을 처리
주로 웹 애플리케이션에서 서버와 통신할 때 사용



참고 문서
https://developer.mozilla.org/en-US/docs/Web/HTML/Element/button
https://getbootstrap.com/docs/5.3/components/buttons/#base-class
https://fontawesome.com/icons


학습 방향
Ajax를 활용하여 클라이언트와 서버 간의 상호작용을 구현하는 방법을 학습한다.
Font Awesome를 사용하여 아이콘을 적용하고, 버튼에 스타일을 적용하는 방법을 익힌다.
사용자가 버튼을 클릭할 때마다 버튼의 상태를 변경하고, 스타일을 조절하여 시각적인 피드백을 제공하는 기능을 구현한다.

문제
Django 좋아요 기능에 Ajax 기술 적용이 완료된 프로젝트를 꾸미고자 한다. 제공된 Django 스켈레톤 프로젝트와 요구 사항에 따라 기능을 구현하시오.
요구사항
시작하기 전에
제공된 스켈레톤 프로젝트는 이전 문제 <code>Ajax를 활용한 좋아요 구현하기 2 - json 응답 및 DOM 조작</code>이 풀이된 프로젝트이다.
Database migrate 후 계정과 게시글을 생성한다.
<code>articles/index.html</code>에서 진행한다.
Bootstrap과 Font Awesome을 활용한다.

좋아요 버튼 스타일링
Bootstrap CDN과 Font Awesome CDN을 올바른 위치에 작성한다.
Font Awesome CDN은 <code>https://cdnjs.com/libraries/font-awesome</code>의 첫 번째 링크를 사용한다.
<code>좋아요/좋아요 취소</code> input 요소를 Font Awesome이 제공하는 heart icon으로 변경한다.
좋아요 상태일 때는 class 속성 값이 <code>fa-solid</code>인 heart icon을 사용한다.
좋아요 상태가 아닐 때는 class 속성 값이 <code>fa-regular</code>인 heart icon을 사용한다.
class 속성 값이 <code>fa-solid</code>인 heart icon은 빨간 계열의 색으로 설정한다.
Bootstrap Button을 사용해서 불필요한 버튼 스타일을 제거한다.
요구사항 외 스타일은 자유롭게 적용한다.

결과 확인
heart icon 클릭 후 새로고침 없이 정상적으로 토글 되는지 확인한다.