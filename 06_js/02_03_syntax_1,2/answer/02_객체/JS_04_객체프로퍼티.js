// 추가
var member = {"id": "kim", "email": "kim@a.com"};
// 동적인 프로퍼티 추가
member.name = "김싸피";
console.log(member);



// 수정 
let member = {id: "abc", email: "ssafy@a.com"}
member["id"] = "ssafy"; 
member.email = "ssafy@ssafy.com"; 


// 삭제
let member = { id: "abc", email: "ssafy@a.com" };
delete member.id;
console.log(member);
