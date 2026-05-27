let member1 = {id: "kim", email: " kim @a.com"}
let member2 = member1;

member2.id = "oh";
console.log(member1.id); // oh
console.log(member2.id); // oh
