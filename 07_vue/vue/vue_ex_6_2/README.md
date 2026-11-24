목표
학습 주제
Vue Router의 동적 라우팅, 내비게이션 가드에 대한 이해와 적용


학습 목표
Vue Router를 사용하여 동적 라우팅을 설정하는 방법 이해
URL에서의 동적 변수를 활용하여 프로필 페이지의 다양한 사용자를 구분하는 방법 습득
내비게이션 가드를 이용하여 라우트 전환 전에 인증 및 권한 확인을 구현하는 방법 익힘

학습 개념

Router를 통해 Parameter 가져오기
부모 컴포넌트에서 반응형 변수를 정의하고, 자식 컴포넌트에 전달할 수 있습니다.
부모 컴포넌트 측반응형 변수를 정의하고, params 속에 전달합니다.  

자식 컴포넌트 측전달받은 자식 컴포넌트 측에서는 route.params.(key)로 받아와서 사용이 가능합니다.  
Navigation Guard
Vue router를 통해 특정 URL에 접근할 때 다른 URL로 redirect를 하거나 취소하여 네비게이션을 보호할 수 있습니다.ex) 인증 정보가 없으면 특정 페이지에 접근하지 못하게 함
Globally (전역 가드)어플리케이션 전역에서 동작하며 index.js에서 정의합니다.
 router.beforeEach()다른 URL로 이동하기 직전에 실행되는 함수입니다.
router.beforeEach() 사용 예시아래의 코드에서 만약 로그인이 되어있지 않고, 이동하는 주소 이름이 login이 아니라면 login 페이지로 redirect 합니다. 
Per-route (라우터 가드)특정 route에서만 동작하며 index.js에서 각 routes에 정의합니다.
router.beforeEnter()route에 진입했을 때만 실행되는 함수입니다.
router.beforeEach() 사용 예시아래의 코드에서 이미 로그인 상태라면 HomeView로 이동하고, 로그인 상태가 아니라면 LoginView로 이동합니다.

In-component (컴포넌트 가드)특정 컴포넌트 내에서만 동작하며 컴포넌트 script에서 정의합니다.
onBeforeRouteLeave현재 라우트에서 다른 라우트로 이동하기 전에 실행되며, 사용자가 현재 페이지를 떠나는 동작에 대한 로직을 처리합니다.
onBeforeRouteUpdate이미 렌더링된 컴포넌트가 같은 라우트 내에서 업데이트 되기 전에 실행되며, 라우트 업데이트 시 추가적인 로직을 처리합니다.

학습 방향
문제
학습 문제

Alan은 두 번째 단계로 프로필 페이지와 간단한 사용자 인증 로직을 추가하려고 한다. 우선 개발단계이다 보니 관리자가 아니라면 개인 프로필 페이지에 접근할 수 없도록 하려고 한다. 요구 사항에 맞게 애플리케이션을 작성하시오.
이전 문제 'Router 설치 및 페이지 이동 연습하기'에서 풀이한 프로젝트 또는 제공된 스켈레톤 프로젝트에서 진행한다.
UserView 컴포넌트를 생성한다.
src/views 폴더 내에 위치한다.
router의 주소 '/user'에 매핑되며 주소 이름은 'user'이다.
해당 주소는 '/user' 뒤에 동적 파라미터 username을 갖는다.
파라미터 username 값을 템플릿에 출력한다.
App 컴포넌트에 UserView 컴포넌트를 렌더링 한다.
RouterLink를 사용해 두 컴포넌트에 대한 HTML a요소를 생성한다.
Named Routes 개념을 사용해 경로에 대한 주소가 아닌 주소의 이름을 활용한다.
반응형 변수 username을 선언 후 해당 변수를 주소의 파라미터 값으로 활용한다.
반응형 변수 username의 값은 문자열 'admin'으로 지정한다.
RouterView를 사용해 컴포넌트를 표시하는 위치를 지정한다.
다른 주소에서 UserView 컴포넌트 주소로 진입할 때 admin이 아니면 진입을 금지한다.
beforeEnter 내비게이션 가드를 활용한다.
router/index.js에서 UserView 컴포넌트 주소에 작성한다.
동적 파라미터 username이 admin이 아니라면 경고 대화상자를 출력한다.
admin이 아니라면 HomeView 컴포넌트 주소로 이동시킨다.
