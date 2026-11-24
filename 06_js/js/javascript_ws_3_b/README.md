목표
학습 주제
JavaScript 함수와 객체 활용하기

학습 목표
JavaScript에서 함수를 객체의 메서드로 정의하고 활용하는 방법 이해
객체 내부에 함수를 포함시켜 객체의 동작을 정의하고 활용하는 방법 습득
함수와 객체를 적절히 조합하여 프로그램을 구현하고 코드의 가독성을 높이는 연습

학습 개념
function
참조 자료형에 속하며 모든 함수는 Function object
return 값이 없다면 undefined를 반환

함수 선언식
function name ([param[, param,[..., param]]]) { 
  statements
  return value
}

함수 표현식
 함수 이름이 없는 ‘익명 함수’를 사용할 수 있음
호이스팅 되지 않으므로 함수를 정의하기 전에 먼저 사용할 수 없음
const funcName = function () {
  statements
}

Object
키로 구분된 데이터 집합을 저장하는 자료형
중괄호(‘{}’)를 이용해 작성
중괄호 안에는 key: value 쌍으로 구성된 속성(property)를 여러 개 작성 가능
key는 문자형만 허용
value는 모든 자료형 허용
const user = {
  name: 'Alice',
  'key with space': true,
  greeting: function () {
    return 'hello'
  }
}

user.greeting()  // 'hello'

학습 방향
JavaScript에서 함수를 객체의 메서드로 정의하고 사용하는 방법을 학습하여 객체 지향적인 프로그래밍을 실현하는 능력을 키운다.
객체 내부에 함수를 포함시켜 객체의 행동을 정의하고 동작을 제어하는 방법을 익힌다.
다양한 예제를 통해 함수와 객체를 적절히 조합하여 프로그램을 구현하고, 객체 지향적인 코드를 작성하는 연습을 한다.
문제
JavaScript의 함수와 객체 간의 관계를 연습을 하고자 한다. 주어진 코드를 참고하여 요구 사항을 만족하는 코드를 작성하시오.
요구사항
다음 요구사항을 갖춘 객체와 함수를 작성하시오.
객체 person
속성 3개(name, age, city)와 메서드 1개(introduce)를 가진다.
속성 name은 이름을 표기할 수 있는 문자열 값을 가진다.
속성 age는 나이를 표기할 수 있는 숫자 값을 가진다.
속성 city는 지역을 표기할 수 있는 문자열 값을 가진다.

메서드 introduce는 속성 name, age, city 값을 활용하여 아래와 같은 문구를 반환한다.
안녕하세요 New York에 거주하는 30살 Alice입니다.

함수 printPersonInfo
구조 분해 할당을 활용하여 매개변수를 정의한다.
person 객체를 인자로 받는다.

함수는 아래와 같은 양식으로 출력한다.
Alice / 30 / New York
