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
Vue Router 사용 예시
index.js에 라우터 관련 설정 작성하기
RouterLink 및 RouterView 추가하기


학습 방향
Django 프로젝트와 앱을 생성하고 관리하는 경험을 쌓는다.
Django 모델을 사용하여 데이터베이스 모델을 정의하고 관리하는 방법을 이해한다.
Vue.js와 Pinia를 사용하여 프로젝트를 초기화하고 관리하는 경험을 쌓는다.

문제
학습 문제
현재 프로젝트에는 단일 객체 조회와 관련된 API 기능은 구현되어있다.이를 활용할 수 있도록 프론트엔드를 수정하여 상세보기 페이지와 기능을 구현하고자 한다.주어진 요구사항을 만족하는 코드를 작성하시오.
제공된 스켈레톤 프로젝트에서 진행한다.
'django-pjt'
가상 환경을 설정하고 gitignore를 생성한다.
프로젝트 실행에 필요한 라이브러리를 설치한다.
'vue-project'에 미리 작성된 프로젝트 구조를 파악한 뒤 아래 요구사항에 따라 진행한다.
상세보기 화면 구현
단일 객체 정보를 화면에 출력하는 페이지를 구성한다.
src/views에 'DetailView.vue' 파일을 생성한다.
Route 추가
src/router/index.js를 수정한다.
'/todo/id' 로 요청이 들어왔을 때 DetailView로 이동하도록 작성한다.
route name 은 'DetailView'로 작성한다.
상세보기 버튼 작성
src/components/TodoListItem.vue를 수정한다.
DetailView로 이동하기 위한 RouterLink를 작성한다.
앞서 추가한 Route 형태에 맞춰 RouterLink에 해당 할 일의 pk 값을 함께 전달한다.
API 요청 작성
DetailView가 화면에 mount 될 때 API 서버로 요청을 보낸다.
API 요청 주소는 'http://127.0.0.1/:8000/api/v1/todos/pk/'
axios를 설치 및 활용한다.
콘솔 출력을 통해 응답 결과를 확인 후 화면에 적절히 출력한다.
화면 스타일링은 자유롭게 진행한다.
네비게이션 바 수정
할 일 목록으로 돌아갈 수 있는 버튼을 구성한다.
RouterLink 를 활용한다.
