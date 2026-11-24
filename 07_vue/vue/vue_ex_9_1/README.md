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
DRF 에서의 인증
인증은 항상 view 함수 시작 시, 권한 및 제한 확인이 발생하기 전, 다른 코드의 진행이 허용되기 전에 실행됨 인증 자체로는 들어오는 요청을 허용하거나 거부할 수 없으며, 단순히 요청에 사용된 자격 증명만 식별한다는 점에 유의
인증 체계 설정
1. 전역 설정 DEFAULT_AUTHENTICATION_CLASSES를 사용 사용 예시 
REST_FRAMEWORK = { 
  'DEFAULT_AUTHENTICATION_CLASSES': [ 
    'rest_framework.authentication.BasicAuthentication', 
    'rest_framework.authentication.TokenAuthent'
  ], 
﻿}﻿

2. View 함수 별 설정 authentication_classes 데코레이터를 사용 사용 예시
from rest_framework.decorators import authentication_classes
from rest_framework.authentication import TokenAuthentication, BasicAuthentication

@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
def article_list(request):
  pass

학습 방향
Django 프로젝트와 앱을 생성하고 관리하는 경험을 쌓는다.
Django 모델을 사용하여 데이터베이스 모델을 정의하고 관리하는 방법을 이해한다.
Vue.js와 Pinia를 사용하여 프로젝트를 초기화하고 관리하는 경험을 쌓는다.

문제
학습 문제
제공된 ‘django-project’ 프로젝트에는 할 일 목록 및 단일 조회, 그리고 ‘dj-rest-auth’ 를 활용한 인증 기능이 구현되어있다. ‘vue-project’ 를 수정하여 API가 제공하는 인증 기능을 사용할 수 있도록 주어진 요구사항을 만족하는 코드를 작성하시오
제공된 스켈레톤 프로젝트에서 진행한다.
'django-pjt'
가상 환경을 설정하고 gitignore를 생성한다.
프로젝트 실행에 필요한 라이브러리를 설치한다.
'vue-project'에 미리 작성된 프로젝트 구조를 파악한 뒤 아래 요구사항에 따라 진행한다.
API 인증 기능 확인
제공된 'django-project'에 구현되어 있는 인증 관련 기능을 확인한다.
'dj-rest-auth' 공식문서를 통해 회원가입에 필요한 데이터를 확인한다.
https://dj-rest-auth.readthedocs.io/en/latest/api_endpoints.html#registration
postman을 통해 구현된 기능에 대한 테스트를 수행한다.
회원가입 요청 테스트를 진행한다.
로그인 요청 테스트를 진행한다.
컴포넌트 작성
src/views에 컴포넌트를 생성한다.
SignUpView.vue
LogInView.vue
route 생성
src/router/index.js를 수정한다.
'/login'로 요청이 들어왔을 때 LogInView로 이동하도록 작성한다.
route name 은 'LogInView'로 작성한다.
'/signup'로 요청이 들어왔을 때 SignUpView로 이동하도록 작성한다.
route name 은 'SignUpView'로 작성한다.
네비게이션 바 수정
RouterLink를 활용해 '/login'와 '/signup'로 이동할 수 있는 버튼을 작성한다.
회원가입 기능 구현
SignUpView.vue에 작성한다.
API 요청에 필요한 데이터를 정의한다.
API 요청을 구성한다.
axios를 설치 및 활용한다.
응답 결과를 콘솔 출력하여 결과를 확인한다.
로그인 기능 구현
LogInView.vue에 작성한다.
API 요청에 필요한 데이터를 정의한다.
API 요청을 구성한다.
axios를 설치 및 활용한다.
응답 결과를 콘솔 출력하여 결과를 확인한다.