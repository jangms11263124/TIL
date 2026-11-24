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
CORS 
특정 출처에서 실행 중인 웹 애플리케이션이 다른 출처의 자원에 접근할 수 있는 권한을 부여하도록 브라우저에 알려주는 체제 다른 출처의 리소스를 가져오기 위해서는 이를 제공하는 서버가 브라우저에게 다른 출처지만 접근해도 된다는 사실을 알려야 함 “CORS policy (교차 출처 리소스 공유 정책)
CORS Headers 
$ pip install django-cors-headers

# settings.py 
INSTALLED_APPS = [ 
  ... 
  'corsheaders', 
  ... 
] 

MIDDLEWARE = [ 
  ... 
  'corsheaders.middleware.CorsMiddleware', 
  'django.middleware.common.CommonMiddleware', 
  ... 
]

CORS_ALLOWED_ORIGINS = [ 
  'http://127.0.0.1:5173', 
  'http://localhost:5173', 
]

학습 방향
Django 프로젝트와 앱을 생성하고 관리하는 경험을 쌓는다. 
Django 모델을 사용하여 데이터베이스 모델을 정의하고 관리하는 방법을 이해한다. 
Vue.js와 Pinia를 사용하여 프로젝트를 초기화하고 관리하는 경험을 쌓는다.

문제
학습 문제
제공된 DRF 프로젝트 'django-pjt' 는 할 일 목록을 반환하는 기능이 구현된 API다. 함께 제공된 ‘vue-project’ 를 수정하여 API가 반환하는 결과를 화면에 출력하는 애플리케이션을 완성하시오.
제공된 스켈레톤 프로젝트에서 진행한다.
'django-pjt'
가상 환경을 설정하고 gitignore를 생성한다.
프로젝트 실행에 필요한 라이브러리를 설치한다.
API 서버를 실행하고 Postman을 사용하여 'http://127.0.0.1:8000/api/v1/todos/' 경로에 GET 요청을 보내 응답 결과를 확인한다.
'vue-project'에 미리 작성된 프로젝트 구조를 파악한 뒤 아래 요구사항에 따라 진행한다.
'TodoStore' store
현재 프로젝트의 store이다.
useTodoStore에 할 일 목록을 담을 'todos' state를 정의한다.
todos의 데이터 타입은 빈 배열로 정의한다.
API서버 요청시 사용될 'BASE_URL'을 정의한다.
기본 요청 주소는 'http://127.0.0.1:8000'이다.
useTodoStore에 할 일 목록을 API 서버로 요청하는 'getTodos' action을 정의한다.
axios를 설치 및 활용한다.
'TodoView.vue'을 수정한다.
vue 프로젝트의 루트경로 'http://127.0.0.1/:5173/' 에 접속시 보여지도록 라우터 설정이 되어있다.
TodoView.vue가 화면에 mount 될 때, 앞서 작성한 'useTodoStore'의 getTodos를 호출한다.
template 안에 store에 정의한 todos를 출력한다.
corsheaders 설정
getTodos 호출시 발생하는 에러를 확인하고 프론트엔드에서 API 서버로 보내는 요청이 정상 처리 되도록 API서버를 수정한다.
'django-cors-headers' 를 설치 및 활용한다.
'http://127.0.0.1/:5173/'에 다시 접속하여 결과를 확인한다.