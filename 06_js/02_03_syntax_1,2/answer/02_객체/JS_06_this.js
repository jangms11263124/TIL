var m1 = {name: "이준호"};
var m2 = {name: "손석구"};

function msg () {
    console.log(this);
    console.log(this.name + "님이 입장함...");
}

m1.msg = msg;
m2.msg = msg;
m1.msg();
m2.msg();
