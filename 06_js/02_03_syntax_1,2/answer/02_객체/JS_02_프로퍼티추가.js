// 객체 생성 시 프로퍼티 추가

let member1 = {id: "valentina", email: "ssafy@a.com"}
function Member(id, email) {
    this.id = id;
    this.email = email;
}
let member2 = new Member("eevee", "ssafy@a.com");
