/* 기본 데이터 타입 (Primitive Type) */ 
// String, Number, Boolean, null, undefined

var num1 = 10; // number
var num2 = 10.2; // number
var msg = "kailey"; // string
var bool = true; // boolean
var nullVal = null; // null
var unVal; // undefined



/* 객체 타입 (Reference Type) */
// Object – function, array 등

var obj = {}; // object
var obj2 = new Object(); //object

/* Symbol */
var symbol = Symbol(); // Symbol(변경 불가능한 기본 타입)
// new 연산자를 사용하면 TypeError 발생
// 같은 심볼을 두번 만들 수 없다


// 심벌 타입의 값은 Symbol 함수를 통해 생성
// 이 때 생성된 심벌 값은 외부에 노출되지 않으며
// 다른 값과 중복되지 않는 유일무이한 값
console.log(typeof symbol);

// 이름이 충돌할 위험이 없는 유일무이한 값인 심벌을 프로퍼티 키로 사용
obj[symbol] = 'value';
console.log(obj[symbol]);
