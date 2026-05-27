/* 문자열 (String) */
// “ ” 로 감싼다.
// ‘ ’ 로 감싼다.
// ` ` (backtick) 으로 감싼다. 
//    -> Template Literal (ES6)
//    -> 여러 줄 입력이 가능 
//      – 공백, 줄 넘김 유지 문자열 내 
//      - `${변수명}`을 이용하여 변수와 문자열을 결합
// UTF-16 형식


let msg = "자바스크립트 문자열";
msg = '자바스크립트 문자열';
msg = `자바스크립트 문자열`;

let name = "이준호";
msg = `나의 이름은 ${name}입니다.`;

let msg2 = `저의
이름은
이준호 입니다.`;
console.log(msg);
console.log(msg2);

