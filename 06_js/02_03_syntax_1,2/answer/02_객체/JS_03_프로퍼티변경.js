// 프로퍼티 변경

let student = {
    name: "김싸피",
    age: 20,
    hobby: ["공부", "숙면"],
    "favorite singer": "뉴진스",
  };

console.log(student.name);
console.log(student[age]); // 에러
console.log(student.hobby);
console.log(student["favorite singer"]);


var member = {};
member ["id"] = "ssafy";
member.name = "싸피";

  