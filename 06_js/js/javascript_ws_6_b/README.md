목표
학습 주제
Ajax를 사용한 클라이언트와 서버 간의 비동기 통신

학습 목표
Ajax를 사용하여 클라이언트와 서버 간의 비동기 통신을 구현하는 방법 이해
axios를 활용하여 JavaScript에서 HTTP 요청을 보내는 방법 습득
Django 서버에서 axios로 보낸 요청을 처리하고 응답하는 방법 익힘

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
https://github.com/axios/axios
https://docs.djangoproject.com/en/4.2/howto/csrf/#acquiring-the-token-if-csrf-use-sessions-or-csrf-cookie-httponly-is-true

학습 방향
Ajax를 활용하여 클라이언트와 서버 간의 상호작용을 구현하는 방법을 학습한다.
axios를 사용하여 클라이언트에서 HTTP 요청을 보내고 서버에서 응답을 처리하는 과정을 익힌다.
Django에서 axios로 보낸 요청을 받아 처리하고, 적절한 응답을 보내는 방법을 익힌다.
문제
Ajax 기술을 사용해 Django의 좋아요 버튼을 페이지 새로고침 없이 변경하고자 한다. 제공된 Django 스켈레톤 프로젝트와 요구 사항에 따라 기능을 구현하시오.
요구사항
시작하기 전에
제공된 스켈레톤 프로젝트는 이전 문제 Ajax를 활용한 좋아요 구현하기 1 - axios 요청이 풀이된 프로젝트이다.
Database migrate 후 계정과 게시글을 생성한다.
articles/index.html와 articles/views.py에서 진행한다.


실시간 좋아요 버튼 조작
좋아요 추가 혹은 취소 상태에 따라 좋아요 input 요소의 value 속성 값을 토글 해야 한다.
Javascript 측에서 좋아요 상태를 알 수 있도록 하는 추가 데이터를 django 측에서 정의한다.
django의 likes view 함수에서 추가 데이터를 정의 후 JSON 데이터 타입으로 응답 데이터를 반환한다.
추가 데이터에 따라 좋아요 input 요소의 value 속성 값을 토글 한다.
어떤 게시글의 좋아요 input인지 알기 위해 article의 pk 값을 활용하여 HTML id 속성 값을 지정한다.
새로 정의한 id 속성 값을 통해 좋아요 input요소를 선택 후 value 속성 값을 토글 한다.


결과 확인
좋아요 버튼 클릭 후 새로고침 없이 정상적으로 토글 되는지 확인한다.