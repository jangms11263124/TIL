// 함수 매개변수

// 함수는 호출 시 매개변수의 영향을 받지 않음
// arguments 라는 함수 내부의 프로퍼티를 이용하여 매개변수의 처리가 가능
// 자바스크립트의 함수는 오버로딩 개념을 지원하지 않음
// 기본 인자 (default arguments)를 사용할 수 있음

function fn1(num) {
  console.log("fn1 ", num)
} 

fn1( );  // undefined
fn1(100);  // 100
fn1(100, 100);  // 100



function fn( ) {
  console.log(arguments.length);
  for (let i = 0; i < arguments.length; i++) {
      console.log(arguments[i]);
  }
}


fn(1); // 1 1

fn(1, 10, 100); // 3 1 10 100


