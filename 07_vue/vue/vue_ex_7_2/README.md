목표
학습 주제
Pinia를 사용한 Vue 애플리케이션의 상태 관리와 상태 공유 방법에 대한 학습


학습 목표
Pinia를 사용하여 상태 관리 애플리케이션에서 getters와 actions를 정의하는 방법 이해
getters를 사용하여 상태 저장소의 데이터를 가져오고 필요한 형식으로 가공하는 방법 습득
actions를 사용하여 상태 저장소의 데이터를 변경하고 비동기 작업을 수행하는 방법 익힘

학습 개념

Pinia를 사용하여 배열 요소 삭제하기

1.	배열의 요소를 삭제하는 메서드를 정의- stores/*.js에서 배열의 요소를 삭제하는 메서드를 정의합니다. 

2.	기능이 필요한 컴포넌트에서의 메서드 호출- Pinia의 store에서 배열의 요소를 삭제하는 메서드를 불러와서 사용합니다.


<결과 화면>- Delete 버튼을 누르면 store.deleteTodo(todo.id)가 작동하여,해당 요소가 삭제됩니다.



학습 방향
문제
학습 문제

모든 상품을 한데 모으는 데 성공한 개발자 Ben은 이제 판매 가치가 없는 불필요한 상품을 골라 제거하고자 한다.그리고 창고 문 앞에 항상 전체 상품의 개수를 표기하고자 한다.
요구 사항에 맞게 애플리케이션을 작성하시오
이전 문제 'Pinia State 연습하기'에서 풀이한 프로젝트 또는 제공된 스켈레톤 프로젝트에서 진행한다.
ProductListItem 컴포넌트
ProductList 컴포넌트의 하위 컴포넌트이다.
ProductList 컴포넌트로부터 개별 상품 객체를 prop 데이터로 전달받는다.
각 상품 데이터마다 삭제 버튼이 함께 출력된다.
삭제 버튼을 클릭하면 선택된 상품의 id를 전달하며 함수 'deleteProduct'를 호출한다.
함수 'deleteProduct'는 store의 'deleteProduct' action를 호출한다.
 store의 'deleteProduct' action은 'products' state에서 선택된 상품 찾아 목록에서 제거하는 기능을 담당한다.
Notice 컴포넌트 
App 컴포넌트의 하위 컴포넌트이다.
 src/components 폴더 내에 위치한다.
 현재 전체 상품 개수를 계산한 결과를 출력한다.
 상품 개수 계산은 'useProductStore' store에서 진행한다.
 상품 개수 계산의 결과 값은 'productCount' getter에 저장하고 Notice 컴포넌트에서 출력한다.

