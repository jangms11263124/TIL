목표
학습 주제
Django REST framework를 사용한 API 서버
개발 Vue.js와 Pinia를 사용한 애플리케이션 프론트 엔드 개발


학습 목표
Django 프로젝트를 생성하고 관리하는 방법을 익힌다.
Django REST framework를 활용하여 API 서버를 구축하는 방법을 습득한다.
Vue.js와 Pinia를 활용하여 프론트 엔드 프로젝트를 구축하는 방법을 익힌다.
기존 스켈레톤 코드를 기반으로 프로젝트를 생성하고 불필요한 컴포넌트와 코드를 삭제하는 능력을 키운다.


학습 개념
Fixtures 데이터 로드 
$ python manage.py loaddata articles.json

AJAX(Asynchronous JavaScript and XML)
비 동기식 JavaScript와 XML로 서버와 통신을 하기 위해서 XMLHttpRequest 객체를 활용합니다.
JSON, XML, HTML 그리고 일반 텍스트 형식 등을 포함한 다양한 포맷을 주고받을 수 있습니다.
페이지 전체를 ‘새로고침’하지 않고서도 수행되는 “비동기성”을 가집니다.(일부만 업데이트도 가능)
axios
브라우저와 nods.js에서 사용할 수 있는 Promise 기반 HTTP 클라이언트 라이브러리로 Vue에서 권고하는 HTTP 통신 라이브러리입니다.
Pinia 사용 예시

1.	stores/*.js 에 필요한 상태를 정의하기- defineStore 메서드를 호출하며, 필요한 상태를 저장합니다.


2.	필요한 컴포넌트에서 상태 불러오기- store 객체를 가져온 뒤, 그 속에 정의한 상태를 가져옵니다.



학습 방향
Django 프로젝트와 앱을 생성하고 관리하는 경험을 쌓는다.
Django 모델을 사용하여 데이터베이스 모델을 정의하고 관리하는 방법을 이해한다.
Vue.js와 Pinia를 사용하여 프로젝트를 초기화하고 관리하는 경험을 쌓는다.

문제
학습 문제
API 에서 받아온 할 일 목록 데이터를 적절한 컴포넌트를 생성하여 출력하고, 상세 페이지 구현을 위한 단일 객체 조회 API 기능을 구현하고자 한다. 주어진 요구사항을 만족하는 코드를 작성하시오.
제공된 스켈레톤 프로젝트에서 진행한다.
'django-pjt'
가상 환경을 설정하고 gitignore를 생성한다.
프로젝트 실행에 필요한 라이브러리를 설치한다.
'vue-project'에 미리 작성된 프로젝트 구조를 파악한 뒤 아래 요구사항에 따라 진행한다.
목록 페이지 수정
'vue-project'를 수정한다.
컴포넌트 생성
src/components에 할 일 목록 출력에 사용할 컴포넌트를 생성한다.
TodoList.vue
TodoList 컴포넌트는 'todos' props를 갖는다.
TodoListItem.vue
TodoList 컴포넌트는 'todo' props를 갖는다.
컴포넌트 등록 
TodoView 컴포넌트에 TodoList 컴포넌트를 등록한다. 
TodoView 컴포넌트가 mount 될 때 실행되는 store.getTodos 응답값으로 채워진 store.todos를 TodoList에 todos props를 전달한다.
TodoList 컴포넌트에 TodoListItem 컴포넌트를 등록한다. 
TodoListItem는 props로 내려받은 할 일 목록 개체수 만큼 반복되며 TodoListItem에 todo props를 전달한다.
수정된 화면 구성을 확인한다. 
컴포넌트의 스타일링은 자유롭게 진행한다.
단일 객체 조회 기능 구현
'django-pjt'를 수정한다.
'todos/urls.py'를 수정한다.
'/todos/{todo_id}/' 경로로 요청이 들어올 때, 'fetch_todo' view 함수가 실행되도록 코드를 작성한다.
'fetch_todo'는 'GET' 요청만 받을 수 있도록 작성한다.
postman을 활용해 'http://127.0.0.1/:8000/api/v1/todos/{todo_id}/'의 요청 결과를 확인한다.