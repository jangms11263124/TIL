// 함수의 호출

function func(callFn) {
  callFn("hello");
} 
function fn( msg ) {
  console.log(msg);
}

func(fn);
