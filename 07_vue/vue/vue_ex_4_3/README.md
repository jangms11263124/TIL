목표
학습 주제
Vue 및 Vite를 사용하여 웹 프로젝트 초기 설정 및 컴포넌트 구조를 활용한 애플리케이션을 만드는 방법


학습 목표
컴포넌트 상속과 재사용의 개념 이해
기존 컴포넌트를 확장하여 새로운 컴포넌트를 생성하는 방법을 습득
컴포넌트를 재사용하여 코드의 중복을 줄이고 유지보수성을 향상


학습 개념

• 웹 페이지는 여러 개의 Component로 구성될 수 있습니다.
• Vite 프로젝트 구조src/App.vue는 Vue 앱의 최상위 Root 컴포넌트로 다른 하위 컴포넌트들을 포함합니다. App.vue에서는 어플리케이션 전체의 레이아웃과 공통적인 요소를 정의합니다.
특정 컴포넌트(*.vue)에 다른 컴포넌트를 등록하면 부모(상위)-자식(하위) 관계가 형성됩니다.

학습 방향
문제
학습 문제

마지막으로 Emily는 기존 컴포넌트 구성이 마음에 들지 않아 다시 재구성하려고 한다. 컴포넌트의 상속과 재사용성 특징을 활용하여 현재 프로젝트의 컴포넌트 구성을 조금 더 세부적으로 나누려 한다. 요구 사항에 맞게 애플리케이션을 작성하시오.
"프로젝트 컴포넌트 구조 재구성"- 이전 문제 'Bootstrap 컴포넌트 배치 연습하기'에서 풀이한 프로젝트 또는 제공된 스켈레톤 프로젝트를 사용한다.
MyComponent 해체 및 부분별 역할에 따라 컴포넌트를 재구성
4개의 신규 컴포넌트가 생성된다. (Header, GalleryList, GalleryListItem, GalleryListItemButton)
Header 컴포넌트
App 컴포넌트의 하위 컴포넌트이다.
기존 MyComponent의 header 요소 부분을 담당한다.
GalleryList 컴포넌트
App 컴포넌트의 하위 컴포넌트이다.
기존 MyComponent의 main 요소 부분을 담당한다.
Card의 반응형 레이아웃 부분을 담당한다.
GalleryListItem 컴포넌트
GalleryList의 하위 컴포넌트이다.
Bootstrap Card 부분을 담당한다.
GalleryListItemButton 컴포넌트
GalleryListItem의 하위 컴포넌트이다.
Bootstrap Card의 버튼을 담당한다.
요구사항 외 스타일링은 실행결과를 참고해 자유롭게 구성한다.

참고